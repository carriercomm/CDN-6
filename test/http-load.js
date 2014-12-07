
var util = require("util");
var _ = require("../http/node_modules/underscore");
var request = require("../http/node_modules/request");
var wiki = require("../http/lib/wiki-en.json");

var BASE = "http://ec2-54-174-6-90.compute-1.amazonaws.com:40080/wiki/";

_.each(wiki, function(val, path){
	request
		.get(BASE+path)
		.on("response", function(res){
			var status = res.statusCode;
			var cache = res.headers['x-cache'];
			var print = util.format("%s %s %s", path, status, cache);
			console.log(print);
		})
		.on("error", function(){
			console.log(path + " error");
		});
});
