# pull official base image
FROM node:lts-alpine

# set working directory
WORKDIR /frontend

# install app dependencies
ADD package*.json .
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

# add app
ADD . .

# start app
CMD ["npm", "start"]