FROM: python:3-alpine

WORKDIR: /usr/src/app

COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
RUN apk add apache2

COPY . .
