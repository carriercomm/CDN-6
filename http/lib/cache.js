/*============================================================================*
 * Dependencies                                                               *
 *============================================================================*/

var fs = require("fs");
var stream = require("stream");
var util = require("util");

/*============================================================================*
 * Stream                                                                     *
 *============================================================================*/

var TransformStream = function(key, cache) {
	this.readable = true;
	this.writable = true;
	this.key = key;
	this.cache = cache;
	this.data = "";
};
util.inherits(TransformStream, stream);

TransformStream.prototype.buffer = function(data) {
 	if (data) {
 		this.data += data;
 		this.emit("data", data);
 	}
};

TransformStream.prototype.write = function () {
  this.buffer.apply(this, arguments);
};

TransformStream.prototype.end = function () {
  this.buffer.apply(this, arguments);
  this.cache[this.key] = this.data;
  this.emit("end");
};

/*============================================================================*
 * Cache                                                                     *
 *============================================================================*/

var Cache = function(){
	this.cache = {};
};

Cache.prototype.get = function(key) {
	return this.cache[key];
};

Cache.prototype.set = function(key) {
	return new TransformStream(key, this.cache);
};

module.exports = new Cache();
