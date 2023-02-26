FROM nginx

RUN apt-get update && apt-get upgrade -y

COPY nginx.conf /etc/nginx/nginx.conf
COPY ./index.html /var/www-data/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]