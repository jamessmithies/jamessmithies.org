
# Dev basics
rebuild:
	docker-compose stop && docker-compose rm --force && docker-compose down --rmi all && docker-compose build && docker-compose up -d 

load:
	docker-compose exec web "./load.sh"

# Publishing
# Make the updates in the localhost browser
# Back up fixtures
dump:
	docker-compose exec web "./dump.sh"
# Optionally, update Mastodon (will update on a GitHub push or every hour regardless.)
mastodon:
	docker-compose exec web python3 manage.py mastocommand
# Optionally, update Zotero
zotero:
	docker-compose exec web python3 manage.py zotcommand
# Make static
static:
	"./web/projectfiles/makestatic.sh"
# Then push to GitHub

# Dev Extras
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




