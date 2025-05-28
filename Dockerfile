FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create necessary directories
RUN mkdir -p /app/frontend /app/backend /app/data

# Copy requirements files
COPY frontend/requirements.txt /app/frontend-requirements.txt
COPY backend/requirements.txt /app/backend-requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/frontend-requirements.txt -r /app/backend-requirements.txt

# Copy application files
COPY frontend/ /app/frontend/
COPY backend/ /app/backend/

# Create startup script
RUN echo '#!/bin/bash\n\
echo "Starting application..."\n\
cd /app/backend && uvicorn main:app --host 0.0.0.0 --port $PORT\n\
' > /app/start.sh && chmod +x /app/start.sh

# Expose port (will be overridden by Render)
EXPOSE 10000

# Set environment variables
ENV GROQ_API_KEY=""
ENV USER_ID="default_user"
ENV DATABASE_URL="sqlite:///./data/assistant.db"
ENV ENVIRONMENT="production"
ENV DEBUG="False"
ENV PORT=10000
ENV BACKEND_URL=""

# Run the startup script
CMD ["/app/start.sh"] 