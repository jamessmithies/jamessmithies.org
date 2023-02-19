#!/bin/bash

echo "$(pwd)"
ls
cd /home/jamessmithies/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles/fixtures

rm jsorg_backup.json.bak
mv jsorg_backup.json jsorg_backup.json.bak
 
cd /home/jamessmithies/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles
docker-compose exec -T web "./dump.sh"


git commit -m 'Fixtures updated via QT console' -- fixtures/