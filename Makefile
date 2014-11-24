
default:
	chmod +x ./httpserver
	chmod +x ./dnsserver
	chmod +x ./deployCDN
	chmod +x ./runCDN
	chmod +x ./stopCDN

http-server:
	cd ./http && npm install

http-test:
	./httpserver -p 40080 -o assets.tablelist.com

ssh:
	ssh -i ~/.ssh/cs5700_rsa abarba@ec2-54-174-6-90.compute-1.amazonaws.com