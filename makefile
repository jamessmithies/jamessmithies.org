build-up:
	docker-compose build && docker-compose up -d

makemigrations:
	docker-compose exec web python3 manage.py makemigrations

zotwriting:
	docker-compose exec web python3 manage.py updatezoterowriting

zottalks:
	docker-compose exec web python3 manage.py updatezoterotalks

load:
	docker-compose exec web "./load.sh"  

destroy:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all

rebuild:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all && docker-compose build && docker-compose up -d

dump-fixtures:
	python3 manage.py dumpdata --settings=settings.base --exclude auth.permission --exclude contenttypes --natural-primary --indent 4 > fixtures/jsorg_dev.json

load-fixtures:
	python3 manage.py loaddata --settings=settings.base ./web/projectfiles/fixtures/jsorg_dev.json

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

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  



