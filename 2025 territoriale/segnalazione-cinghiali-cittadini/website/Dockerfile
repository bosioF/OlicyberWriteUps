FROM node:22

RUN mkdir /app
WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm ci

COPY . .

RUN npm run build

CMD ["node", "build"]