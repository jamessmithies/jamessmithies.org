#!/bin/bash

cd /Users/jamessmithies/Library/CloudStorage/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles/fixtures

rm jsorg_backup.json.bak
mv jsorg_backup.json jsorg_backup.json.bak
 
cd /Users/jamessmithies/Library/CloudStorage/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles
docker-compose exec -T web "./dump.sh"

cd ../../

git commit -m 'Fixtures updated via QT console' -- web/projectfiles/fixtures/

git push origin master