FROM alpine

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev py3-pip postgresql-client postgresql-dev build-base gettext jpeg-dev zlib-dev 
RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl
RUN apk add ca-certificates
RUN update-ca-certificates
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Clean
WORKDIR /data/web
RUN apk del -r python3-dev postgresql

# Prepare
COPY . /data/web/
RUN mkdir -p projectfiles/static/admin