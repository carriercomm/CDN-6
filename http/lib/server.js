
// Dependencies
var fs = require('fs');
var http = require('http');
var util = require('util');
var request = require('request');
var cache = require('./cache');

// Constants
var PORT = process.argv[3];
var ORIGIN = process.argv[5];

// Response time
var RESPONSE_TIME = 0;

// Create server
var server = http.createServer(function (req, res) {
 	
 	// start time
 	var start = Date.now();

	// origin url
 	var url = util.format("http://%s%s", ORIGIN, req.url);
 	console.log('GET ' + url);

 	// check cache
 	var data = cache.get(url);

 	// if we have data return it
 	// update response time accordingly
 	if (data) {
 		console.log('Cached.');
 		RESPONSE_TIME = Date.now() - start;
 		console.log('Complete: ' + RESPONSE_TIME + 'ms');
 		res.end(data);
 	} else {
 		console.log('Requesting...');
 		// fetch data from url
 		// simultaneously cache the data
 		// and pipe to the response
 		// update response time accordingly
 		request(url)
 			.pipe(cache.set(url, function(){
 				RESPONSE_TIME = Date.now() - start;
 				console.log('Complete: ' + RESPONSE_TIME + 'ms');
 			}))
 			.pipe(res);
 	}
});

// start listening
server.listen(PORT);
console.log('HTTP Server ' + PORT);