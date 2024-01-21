FROM alpine:3.18

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update wget python3 python3-dev py3-pip postgresql-client postgresql-dev build-base gettext jpeg-dev zlib-dev 

# Create a virtual environment and use it
# RUN python3 -m venv /venv
# ENV PATH="/venv/bin:$PATH"

# Now you can safely upgrade pip and install other packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Clean
WORKDIR /data/web
RUN apk del -r python3-dev postgresql

# Prepare
COPY . /data/web/
RUN mkdir -p projectfiles/static/admin