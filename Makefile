
http-test:
	./httpserver -p 40080 -o assets.tablelist.com

ssh:
	ssh -i ~/.ssh/cs5700_rsa abarba@ec2-54-174-6-90.compute-1.amazonaws.com

deploy:
	./deployCDN -u abarba -i ~/.ssh/cs5700_rsa

run:
	./runCDN -u abarba -i ~/.ssh/cs5700_rsa -p 40080 -o assets.tablelist.com -n domain.name.com

stop:
	./stopCDN -u abarba -i ~/.ssh/cs5700_rsa