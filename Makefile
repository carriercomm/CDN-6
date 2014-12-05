
http-test:
	./httpserver -p 40080 -o assets.tablelist.com

dns-test:
	./dnsserver -p 40080 -n test.com

ssh:
	ssh -i ~/.ssh/cs5700_rsa abarba@ec2-54-174-6-90.compute-1.amazonaws.com

ssh-dns:
	ssh -i ~/.ssh/cs5700_rsa abarba@cs5700cdnproject.ccs.neu.edu

deploy:
	./deployCDN -u abarba -i ~/.ssh/cs5700_rsa

run:
	./runCDN -u abarba -i ~/.ssh/cs5700_rsa -p 40080 -o assets.tablelist.com -n cs5700cdnproject.ccs.neu.edu

stop:
	./stopCDN -u abarba -i ~/.ssh/cs5700_rsa