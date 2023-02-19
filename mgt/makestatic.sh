#!/bin/sh

start=`date +%s`
# Save site
wget --directory-prefix="../docs" localhost\
    --no-host-directories \
    --recursive -l100 \
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
cd ../docs
mv robots.txt tmp
mv tmp/index.html tmp/robots.txt
cp tmp/robots.txt ./
rm -rf tmp

#Fix url in RSS feed
cd blog/feed
sed -i 's/example.com/www.jamessmithies.org/g' index.html

end=`date +%s`

runtime=$((end-start))

echo "Runtime: $runtime seconds"


