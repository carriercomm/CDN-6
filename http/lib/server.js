
// Dependencies
var fs = require("fs");
var http = require("http");
var net = require("net");
var util = require("util");
var request = require("request");

// Modules
var cache = require("./cache");
var metrics = require("./metrics");

// Constants
var PORT = process.argv[3];
var ORIGIN = process.argv[5];

// Create server
var server = http.createServer(function(req, res){

	// origin url
 	var url = util.format("http://%s%s", ORIGIN, req.url);

 	// check cache
 	var data = cache.get(url);

 	// if we have data return it
 	// otherwise fetch from origin
 	if (data) {
 		res.end(data);
 	} else {
 		request(url)
 			.pipe(cache.set(url))
 			.pipe(res);
 	}
});

// Setup metrics
metrics.bind(server);

// DNS socket
var options = {
	host: 'cs5700cdnproject.ccs.neu.edu',
	port: PORT
};

// connect to DNS server and send metrics
var socket = net.connect(options, function(err){
	setInterval(function(){
		var json = JSON.stringify(metrics.toJSON());
		socket.write(json);
	}, 10 * 1000);
});

socket.on('error', function(){
	console.log('Failed to connect to DNS server.');
});

// Start listening
server.listen(PORT);
console.log("HTTP Server " + PORT);
