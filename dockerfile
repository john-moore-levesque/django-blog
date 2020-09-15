FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirement.txt ./
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev mariadb-connector-c-dev apache2
RUN pip install --no-cache-dir -r requirement.txt


COPY . .
