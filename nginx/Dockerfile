#FROM nginx
#
#RUN rm /etc/nginx/conf.d/default.conf
#
#COPY nginx/default.conf /etc/nginx/conf.d/
#
#EXPOSE 80
FROM jwilder/nginx-proxy:1.2

COPY nginx/default_location /etc/nginx/vhost.d/default_location
