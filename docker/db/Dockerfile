FROM mysql:8.1.0

ENV MYSQL_ROOT_PASSWORD=plcsoftrel

ADD init.sql /docker-entrypoint-initdb.d

EXPOSE 3306

CMD ["mysqld"]