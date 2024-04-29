#!/bin/bash
cd ..

# copy files into docker folder
cp -r init.sql ./docker/db
cp -r requirements.txt ./server ./docker/backend
cp -r ./assets ./public ./src .eslintrc.json next.config.js package-lock.json package.json tsconfig.json ./docker/frontend

cd docker

# replace text "127.0.0.1" into "{os.getenv("DB_HOST")}" in db.py
# DB_HOST environment variable is the container name of mysql server (environment variable is defined in .env in backend folder)
sed -i 's+127.0.0.1+{os.getenv("DB_HOST")}+g' ./backend/server/comm/db.py

docker-compose up --build