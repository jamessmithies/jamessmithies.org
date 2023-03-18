#!/bin/bash

# Publish primary static docs
echo "Publishing primary static docs to GitHub live..."

cd ~/Dropbox/Technical/dev/jamessmithies.org/docs

git commit -m 'Static docs published via QT console' -- ../docs/

git push origin master

# Push Zotero templates to GitHub
echo "Publishing Zotero templates to GitHub..."

cd ~/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles/templates/zotero

git commit -m 'Zotero template updated via QT console' -- ../zotero/

git push origin master