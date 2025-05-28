#!/bin/bash

# Build the Docker image
docker build -t ai-assistant .

# Run the container
docker run -d \
  --name ai-assistant \
  -p 8000:8000 \
  -p 8501:8501 \
  -v "$(pwd)/data:/app/data" \
  -e GROQ_API_KEY="$GROQ_API_KEY" \
  -e USER_ID="$USER_ID" \
  ai-assistant

echo "Application is running!"
echo "Frontend: http://localhost:8501"
echo "Backend API: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs" 