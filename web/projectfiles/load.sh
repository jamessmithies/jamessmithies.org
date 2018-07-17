#!/bin/sh
python manage.py migrate
python manage.py loaddata --settings=settings.base ./fixtures/jsorg_dev.json
python manage.py rebuild_index --settings=settings.base --noinput