
// Dependencies
var net = require("net");
var spawn = require("child_process").spawn;

// Constants
var DNS_OPTIONS = {
	host: "localhost",
	port: 44446
};

// Open port for DNS to connect to
var server = net.createServer(function(socket){
	socket.on("data", function(data){
		var json = null;
		try {
			json = JSON.parse(data.toString("utf8"));
		} catch(err) {
			return socket.end();
		}
		rtt(json.ip, function(err, time){
			if (err) return;
			sendRtt(json.ip, time);
		});
	});
}).listen(44447);

function sendRtt(ip, time) {
	var socket = net.connect(DNS_OPTIONS, function(){
		var res = JSON.stringify({
			ip: ip,
			rtt: time
		});
		socket.write(res);
	}).on("close", function(){
		socket = null;
	}).on("error", function(err){
		console.log(err);
		socket = null;
	});
}

function rtt(ip, next) {

	var text = "";

	scamper = spawn("scamper", ["-c", "ping -c 1", "-i", ip]);

	scamper.stdout.on("data", function(data){
	 	text += data.toString("utf8").trim();
	});

	scamper.stderr.on("data", function(err){
	 	console.log("stderr: " + err);
	 	next(null, -1);
	});

	scamper.on("close", function (code) {
		console.log(text);
	 	var lines = text.split("\n");
	 	console.log(lines);
	 	var line = lines.pop();
	 	var parts = line.split(" ");
	 	var stats = parts[parts.length - 2];
	 	var sparts = stats ? stats.split("/") : [];
	 	var avg = parseFloat(sparts[0]);
	 	console.log(avg);
	 	next(null, isNaN(avg) ? -1 : 0);
	});
}