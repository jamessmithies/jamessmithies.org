#!/bin/sh

# Save site
wget --directory-prefix="../docs" host.docker.internal \
    --no-host-directories \
    --recursive -l100 \
    --content-disposition \
    --trust-server-names \
    --adjust-extension \
    --no-clobber \
    --page-requisites \
    --html-extension \
    --convert-links \
    --no-check-certificate \
    --no-parent \
         host.docker.internal \

#Clean
cd ../docs
mv robots.txt tmp
mv tmp/index.html tmp/robots.txt
cp tmp/robots.txt ./
rm -rf tmp

#Fix url in RSS feed
cd blog/feed
sed -i 's/example.com/www.jamessmithies.org/g' index.html




