#!/bin/bash

cd Dropbox/Technical/dev/jamessmithies.org/docs

#git remote set-url origin git@hostname:jamessmithies/jamessmithies.org.git

git commit -m 'Static docs published via QT console' -- ../docs/

git push origin master