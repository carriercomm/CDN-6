/*============================================================================*
 * Dependencies                                                               *
 *============================================================================*/

var fs = require("fs");
var stream = require("stream");
var util = require("util");
var _ = require('underscore');

/*============================================================================*
 * Metrics                                                                      *
 *============================================================================*/

var Metrics = function() {
	this.responseTime = 100;
	this.rpm = 0;
};

/*============================================================================*
 * Initialize                                                                 *
 *============================================================================*/

Metrics.prototype.bind = function(server) {
	// monitor response time
	responseTime(this, server);
	// monitor requests per minute
	requestsPerMinute(this, server);
};

/*============================================================================*
 * Monitors                                                                   *
 *============================================================================*/

function responseTime(self, server) {
 	
	var SAMPLE = 10;
	var times = [];

	// listen for incoming request
 	server.on('request', function(req, res){
 		var start = Date.now();
 		res.on('finish', function(){
 			var diff = Date.now() - start;
 			times.push(diff);
 		});
 	});

 	// run a sample every 10 seconds
 	setInterval(function(){
 		var total = _.reduce(times, function(a, b){
 			return a + b;
 		}, 0);
 		self.responseTime = total / times.length;
 		times = [];
 	}, SAMPLE * 1000);
};

function requestsPerMinute(self, server) {
	
	var SAMPLE = 10; // sample every x seconds
	var count = 0; // request count for current sample

	// listen for incoming request
	server.on('request', function(req, res){
		count++;	
	});

	// run a sample every 10 seconds
	setInterval(function(){
		self.rpm = count * (60 / SAMPLE);
		count = 0;
	}, SAMPLE * 1000);
};



module.exports = new Metrics();
