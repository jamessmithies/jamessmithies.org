rebuild:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all && docker-compose build && docker-compose up -d 

load:
	docker-compose exec web "./scripts/load.sh"

zotero:
	bash web/projectfiles/scripts/zotero.sh

static:
	web/projectfiles/scripts/static.sh

destroy:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all

build-up:
	docker-compose build && docker-compose up -d

shell-web:
	docker-compose exec web sh

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

migrations:
	docker-compose exec web python3 manage.py makemigrations

migrate:
	docker-compose exec web python3 manage.py migrate


collect:
	docker-compose exec python3 manage.py collectstatic --settings=settings.base

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker-compose exec nginx sh

shell-postgres:
	docker-compose exec postgres sh

remove:
	docker-compose rm --force

build:
	docker-compose build

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

shell-db:
	docker exec -ti pz01 bash




