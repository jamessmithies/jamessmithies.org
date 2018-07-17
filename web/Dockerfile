FROM alpine

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update python python-dev py-pip postgresql-client postgresql-dev build-base gettext
RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl
RUN apk add ca-certificates
RUN update-ca-certificates
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#Install additional Python modules
WORKDIR /usr/lib/python2.7/site-packages/
RUN wget https://s3-eu-west-1.amazonaws.com/jamessmithies/downloads/custom_additions.zip
RUN unzip custom_additions.zip
RUN rm -rf custom_additions.zip

# Clean
WORKDIR /data/web
RUN apk del -r python-dev postgresql

# Prepare
COPY . /data/web/
RUN mkdir -p projectfiles/static/admin