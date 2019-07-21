#!/bin/sh
python3 manage.py migrate
python3 manage.py loaddata --settings=settings.base ./fixtures/jsorg_dev.json
python3 manage.py rebuild_index --settings=settings.base --noinput