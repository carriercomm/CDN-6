
// Dependencies
var fs = require('fs');
var http = require('http');
var util = require('util');
var request = require('request');
var cache = require('./cache');

// Constants
var PORT = process.argv[3];
var ORIGIN = process.argv[5];

// Create server
var server = http.createServer(function (req, res) {
 	
	// origin url
 	var url = util.format("http://%s%s", ORIGIN, req.url);

 	// check cache
 	var data = cache.get(url);

 	// if we have data, return it
 	// else fetch from origin and cache it
 	if (data) {
 		console.log('Cached.');
 		res.end(data);
 	} else {
 		console.log('No cache.');
 		request(url)
 			.pipe(cache.set(url))
 			.pipe(res);
 	}
});

// start listening
server.listen(PORT, '127.0.0.1');
console.log('HTTP Server ' + PORT);