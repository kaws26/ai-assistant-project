#!/bin/bash

# Build the Docker image
docker build -t ai-assistant .

# Stop and remove existing container if it exists
docker stop ai-assistant 2>/dev/null || true
docker rm ai-assistant 2>/dev/null || true

# Run the container
docker run -d \
  --name ai-assistant \
  --network host \
  -v "$(pwd)/data:/app/data" \
  -e GROQ_API_KEY="$GROQ_API_KEY" \
  -e USER_ID="$USER_ID" \
  ai-assistant

echo "Application is running!"
echo "Frontend: http://localhost:8501"
echo "Backend API: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs" 