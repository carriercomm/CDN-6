
// Dependencies
var net = require("net");
var spawn = require("child_process").spawn;

// Connect to DNS server
var options = {
	host: "localhost",
	port: 44446
};
var dsocket = net.connect(options);

dsocket.on("close", function(){
	dsocket = null;
});

dsocket.on("error", function(err){
	console.log(err);
});

// Open port for DNS to connect to
var server = net.createServer(function(socket){
	socket.on("data", function(data){
		var text = data.toString("utf8");
		var json = null;
		try {
			json = JSON.parse(text);
		} catch(err) {
			return socket.end();
		}
		var ip = json.ip;
		rtt(ip, function(err, time){
			if (!err) {
				var res = JSON.stringify({
					ip: ip,
					rtt: time
				});
				if (dsocket) {
					dsocket.write(res);
				}
			}
		});
	});

	socket.on("end", function(){
		console.log("Socket closed");
	});
}).listen(44446);

function rtt(ip, next) {
	scamper = spawn("scamper", ["-i", ip]);
	
	var text = "";

	scamper.stdout.on("data", function(data){
	 	text += data.toString("utf8").trim();
	});

	scamper.stderr.on("data", function(err){
	 	console.log("stderr: " + err);
	 	next(null, -1);
	});

	scamper.on("close", function (code) {
	 	var lines = text.split("\n");
	 	var sum = 0;
	 	var count = 0;
	 	for (var i = 1; i < lines.length; i++) {
	 		var line = lines[i].trim().split(" ");
	 		var time = parseFloat(line[line.length-2]);
	 		if (!isNaN(time)) {
	 			sum += time;
	 			count++;
	 		}
	 	}
	 	var avg = sum / count;
	 	next(null, isNaN(avg) ? -1 : 0);
	});
}