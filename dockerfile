FROM centos:latest

RUN yum update -y
RUN yum install -y httpd
RUN yum install -y python38
RUN yum install -y python38-mod_wsgi

ENV APACHE_RUN_USER apache
ENV APACHE_RUN_GROUP apache
ENV APACHE_LOG_DIR /var/log/apache

EXPOSE 80
