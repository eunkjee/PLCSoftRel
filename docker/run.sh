#!/bin/bash
cd ..

cp -r init.sql ./docker/db
cp -r requirements.txt ./server ./docker/backend
cp -r ./assets ./public ./src .eslintrc.json next.config.js package-lock.json package.json tsconfig.json ./docker/frontend

cd docker

docker-compose up --build