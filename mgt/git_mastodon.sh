#!/bin/bash

# Fetch latest Toots from Mastodon API and print them into template
echo "Fetching latest Toots from Mastodon API.."
cd ~/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles/

python3 mastodon.py

# Copy the updated mastodon_sidebar template to the static files docs directory
cp -f ~/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles/templates/index/mastodon_sidebar.html ~/Dropbox/Technical/dev/jamessmithies.org/docs/mastodonsidebar/

rm ~/Dropbox/Technical/dev/jamessmithies.org/docs/mastodonsidebar/index.html

mv ~/Dropbox/Technical/dev/jamessmithies.org/docs/mastodonsidebar/mastodon_sidebar.html ~/Dropbox/Technical/dev/jamessmithies.org/docs/mastodonsidebar/index.html
 
    
# Publish latest Mastodon toots
echo "Updating Toots to GitHub live..."

cd ~/Dropbox/Technical/dev/jamessmithies.org/docs

git commit -m 'Toots updated via QT console' -- ../docs/

git push origin master

