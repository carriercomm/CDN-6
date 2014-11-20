
// Dependencies
var fs = require('fs');
var http = require('http');
var request = require('request');

// Constants
var PORT = process.argv[2] || 8080;

// Create server
var server = http.createServer(function (req, res) {
 	request('http://www.google.com').pipe(res);
});

// start listening
server.listen(PORT, '127.0.0.1');
console.log('HTTP Server ' + PORT);