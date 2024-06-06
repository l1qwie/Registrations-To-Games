rm:
	docker compose stop \
	&& docker compose rm \
	&& sudo rm -rf pgdata/

start:
	docker-compose -f docker-compose.yml up --force-recreate
