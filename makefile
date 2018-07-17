build-up:
	docker-compose build && docker-compose up -d

zot:
	docker-compose exec web python manage.py updatezotero

load:
	docker-compose exec web "./load.sh"  

dump-fixtures:
	python manage.py dumpdata --settings=settings.base --exclude auth.permission --exclude contenttypes --natural-primary --indent 4 > jsorg_dev.json

load-fixtures:
	python manage.py loaddata --settings=settings.base ./fixtures/jsorg_dev.json

destroy:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all

rebuild:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all && docker-compose build && docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-web:
	docker-compose exec web sh

shell-nginx:
	docker-compose exec nginx sh

shell-postgres:
	docker-compose exec postgres sh

build:
	docker-compose build

remove:
	docker-compose rm --force

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

shell-db:
	docker exec -ti pz01 bash

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  



