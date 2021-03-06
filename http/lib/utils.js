/*============================================================================*
 * Dependencies                                                               *
 *============================================================================*/

var util = require("util");
var _ = require("./underscore");

/*============================================================================*
 * Constructor                                                                *
 *============================================================================*/

var Utils = function() {};

/*============================================================================*
 * Methods                                                                    *
 *============================================================================*/

/**
 * Returns a unique 16 digit identifier
 */
Utils.prototype.guid = function() {
	var guid = [];
	for (var i = 0; i < 4; i++) {
		guid.push(Math.floor((1 + Math.random()) * 0x10000)
		              .toString(16)
		              .substring(1));
	}
	return guid.join("-").toUpperCase();
};

/*============================================================================*
 * Export                                                                     *
 *============================================================================*/

module.exports = new Utils();
