# Stage 1: Build the application
FROM node:14-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Copy the rest of the application code
COPY . .

# Remove unnecessary files
RUN rm -rf /app/.git /app/tests /app/docs

# Build the application (if there is a build step, e.g., TypeScript)
# RUN npm run build

# Stage 2: Create the final image
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy necessary files from the build stage
COPY --from=builder /app ./

# Remove npm cache and other unnecessary files
RUN rm -rf /root/.npm /tmp/* /var/cache/apk/*

# Expose the application port (assuming the backend runs on port 5000)
EXPOSE 5000

# Command to run the backend application
CMD ["node", "server.js"]
