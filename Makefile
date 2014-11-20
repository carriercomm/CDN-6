
default:
	chmod +x ./httpserver
	chmod +x ./dnsserver

deploy-http:
	rm -rf ./HTTP/node_modules
	scp -r -i ~/.ssh/cs5700_rsa ./HTTP abarba@ec2-54-174-6-90.compute-1.amazonaws.com:http
	ssh abarba@ec2-54-174-6-90.compute-1.amazonaws.com 'cd http; npm install;' -i ~/.ssh/cs5700_rsa 

test-http-server:
	./httpserver -p 40080 -o assets.tablelist.com

abarba-ssh:
	ssh abarba@ec2-54-174-6-90.compute-1.amazonaws.com -i ~/.ssh/cs5700_rsa