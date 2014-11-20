
default:
	chmod +x ./httpserver
	chmod +x ./dnsserver

abarba-ssh:
	ssh abarba@ec2-54-174-6-90.compute-1.amazonaws.com -i ~/.ssh/cs5700_rsa