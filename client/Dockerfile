# I Build the application
FROM node:14-alpine AS builder

WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

#I  Removed unnecessary files and dependencies
RUN rm -rf /app/.git /app/test /app/docs /app/node_modules

#  Created the final image
FROM node:14-alpine

WORKDIR /app

#I Installed serve globally to serve the build
RUN npm install -g serve

#  I Copied only the built files from the build stage
COPY --from=builder /app/build ./build

# Expose the application port
EXPOSE 3000

# Command to run the application
CMD ["serve", "-s", "build"]
# Stage 1: Build the application
FROM node:14-alpine AS builder

WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

# Removed unnecessary files and dependencies
RUN rm -rf /app/.git /app/test /app/docs /app/node_modules

#Created the final image
FROM node:14-alpine

WORKDIR /app

# Installed serve globally to serve the build
RUN npm install -g serve

# Copied only the built files from the build stage
COPY --from=builder /app/build ./build

# Exposed the application port
EXPOSE 3000

# Command to run the application
CMD ["serve", "-s", "build"]
