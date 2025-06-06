build-jenkins:
	docker-compose build jenkins

start-jenkins:
	docker-compose up -d jenkins

logs-jenkins:
	docker logs -f jenkins-python

test:
	pytest

run:
	python run.py

dc:
	docker compose up -d --build