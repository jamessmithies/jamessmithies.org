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

#Clean
cd ../jsorg-static
mv robots.txt tmp
mv tmp/index.html tmp/robots.txt
cp tmp/robots.txt ./
rm -rf tmp

#find -type f -exec bash -c 'fp=$(dirname "$1");fn=$(basename "$fp");px="${1##*.}";mv "$1" "$fp"/"$fn"."$px"' sh "{}" \;

