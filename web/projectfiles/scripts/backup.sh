#!/bin/sh
python3 manage.py dumpdata --settings=settings.base --exclude auth.permission --exclude contenttypes --natural-primary --indent 4 > ./fixtures/jsorg_backup.json