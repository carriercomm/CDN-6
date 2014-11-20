
default:
	chmod +x ./httpserver
	chmod +x ./dnsserver

test-http-server:
	./httpserver -p 40080 -o assets.tablelist.com

abarba-ssh:
	ssh abarba@ec2-54-174-6-90.compute-1.amazonaws.com -i ~/.ssh/cs5700_rsa