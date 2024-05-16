FROM mysql

ENV MYSQL_DATABASE=user
ENV MYSQL_USER=jean
ENV MYSQL_PASSWORD=1234
ENV MYSQL_ROOT_PASSWORD=root

COPY init.sql /docker-entrypoint-initdb.d/
