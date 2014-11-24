CDN
===

authors: Andrew Barba and Gary Soeller

DNS Server
=========

```./dnsserver -p <port> -n <name>```

HTTP Server
===========

```./httpserver -p <port> -o <origin>```

Everything else
===============

```./[deploy|run|stop]CDN -p <port> -o <origin> -n <name> -u <username> -i <keyfile>```

Milestone 2014/11/24
====================

#### HTTP Server
We chose to implement the HTTP server in Node.js. Node is a perfect fit for
highly concurrent web servers that do little computation but a lot of I/O. The
replica servers for our CDN do precisely this. They need to quickly download
and serve content to clients with little to no computation on the data they
are serving. They also need to implement a caching policy and monitor basic
metrics such as response time and requests per minute. Metrics are monitored
by running a sample every 10 seconds and then reporting that data to the DNS
server over a TCP socket. A sample payload looks something like:
```
{
	"id": "CD5B-4F68-27AA-438E",
	"ipAddress": "234.56.45.455",
	"rpm": 93,
	"responseTime": 84 // miliseconds,
	"cacheSize": 6745 // bytes
}
```
The biggest optimaztion made in the HTTP server is its use of Node.js Streams.
Streams allow us to download data, cache it, and respond to the client 
simultaneously. As chunks of data come in, it is passed through a caching stream
which immediately passes the chunk to the response stream. This allows total
response time to go from:
```
totalTime = downloadTime() + responseTime()
```
to:
```
totalTime = MAX(downloadTime(), responseTime())
```
In a network where every milisecond counts, this is a major speed improvement
and the biggest reason for choosing Node.js as our HTTP server.







