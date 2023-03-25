#!/bin/bash

# Fetch latest Toots from Mastodon API and print them into template
echo "Fetching latest Toots from Mastodon API.."
cd ~/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles/

python3 mastodon.py
    
# Publish latest Mastodon toots
echo "Publishing latest Mastodon toots to GitHub live..."

cd ~/Dropbox/Technical/dev/jamessmithies.org/web/projectfiles/blog/

git commit -m 'Toots updated via QT console' -- ../blog/

git push origin master

