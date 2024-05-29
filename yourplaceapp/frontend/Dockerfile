# Use a base image with Node.js
FROM node:14-slim

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY ./frontend/package.json /app/package.json
RUN npm install

# Copy the rest of the frontend code
COPY ./frontend /app

# Build the frontend app
RUN npm run build

# Command to run the application
CMD ["npm", "start"]
