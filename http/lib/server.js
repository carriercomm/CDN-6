
// Dependencies
var fs = require("fs");
var http = require("http");
var net = require("net");
var util = require("util");
var request = require("request");
var _ = require("underscore");

// Modules
var cache = require("./cache");
var metrics = require("./metrics");
var scamper = require("./scamper");

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
 		var meta = cache.getMeta(url);
 		setMetadata(res, meta, true);
 		res.end(data);
 	} else {
 		request(url)
 			.on("response", function(meta){
 				cache.setMeta(url, meta);
 				setMetadata(res, meta);
 			})
 			.pipe(cache.set(url))
 			.pipe(res);
 	}

 	// Helper function for setting response metadata
 	// like statusCode and headers
 	function setMetadata(res, meta, cacheHit) {
 		if (!res || !meta) return;
 		res.statusCode = meta.statusCode;
 		_.each(meta.headers, function(val, key){
 			res.setHeader(key, val);
 		});
 		res.setHeader("x-cache", cacheHit ? "hit" : "miss");
 	}
});

// Setup metrics
metrics.bind(server);

// Start listening
server.listen(PORT);
console.log("HTTP Server " + PORT);
