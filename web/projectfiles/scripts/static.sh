#!/bin/sh

# Save site
wget --directory-prefix="../jsorg-static" localhost\
    --no-host-directories \
    --recursive \
    --content-disposition \
    --trust-server-names \
    --adjust-extension \
    --no-clobber \
    --page-requisites \
    --html-extension \
    --convert-links \
    --no-check-certificate
    --no-parent \
         localhost \

#cp -r web/projectfiles/collectstatic* ../jsorg-static

#Clean
cd ../jsorg-static
mv robots.txt tmp
mv tmp/index.html tmp/robots.txt
cp tmp/robots.txt ./
rm -rf tmp




