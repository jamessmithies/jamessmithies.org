#!/bin/sh
python3 manage.py migrate
python3 manage.py loaddata --settings=settings.base ./fixtures/jsorg_backup.json