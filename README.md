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
In a network where every millisecond counts, this is a major speed improvement
and the biggest reason for choosing Node.js as our HTTP server.

##### DNS Server

For our DNS Server, we decided to use python as the language of choice. We simply used sockets and c-structs to parse and build DNS requests/responses. This is very similar to the other projects in the class except with a different protocol. We also used a 3rd party website to retrieve geolocation data about IP addresses. We want this so we know the closest replica server to the client making the request. Although this is a naive solution, it will be part of the final solution that we will be building. Some future improvements we will make is to have the HTTP server ping the DNS server with stats about their payload. The DNS server will then have enough knowledge to send new clients to a better replica based on how close they are to the replica and the load the replica is under.





