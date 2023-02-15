rebuild:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all && docker-compose build && docker-compose up -d 

load:
	docker-compose exec web "./load.sh"

dump:
	docker-compose exec web "./dump.sh"

static:
	"./web/projectfiles/makestatic.sh"

zotero:
	docker-compose exec web python3 manage.py zotcommand

destroy:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all

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

start:
	docker-compose start

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker-compose exec nginx sh

shell-postgres:
	docker-compose exec postgres sh

shell-db:
	docker exec -ti pz01 bash




