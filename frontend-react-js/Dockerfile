FROM node:16.19.1

ENV PORT=3000

WORKDIR /frontend-react-js
COPY . /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
