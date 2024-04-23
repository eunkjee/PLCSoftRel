FROM node:18.16.0

WORKDIR /PLCSoftRel

COPY assets assets
COPY public public
COPY src src
COPY .eslintrc.json next.config.js package-lock.json package.json tsconfig.json .

RUN npm install

RUN npm run build

EXPOSE 3000

ENTRYPOINT ["npm", "run", "start"]