
var Cache = function(){
	this.cache = {};
};

Cache.prototype.get = function(key) {
	return this.cache[key];
};

Cache.prototype.set = function(key, value) {
	return this.cache[key] = value;
};

module.exports = new Cache();