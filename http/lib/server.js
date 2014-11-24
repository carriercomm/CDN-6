
// Dependencies
var fs = require("fs");
var http = require("http");
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
 	
 	// start time
 	var start = Date.now();

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

// Start listening
server.listen(PORT);
console.log("HTTP Server " + PORT);