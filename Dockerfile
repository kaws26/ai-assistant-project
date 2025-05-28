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
echo "Starting backend..."\n\
cd /app/backend && uvicorn main:app --host 0.0.0.0 --port 8000 &\n\
echo "Starting frontend..."\n\
cd /app/frontend && streamlit run app.py --server.port=8501 --server.address=0.0.0.0\n\
' > /app/start.sh && chmod +x /app/start.sh

# Expose ports
EXPOSE 8000 8501

# Set environment variables
ENV GROQ_API_KEY=""
ENV USER_ID="default_user"
ENV DATABASE_URL="sqlite:///./data/assistant.db"
ENV ENVIRONMENT="production"
ENV DEBUG="False"
ENV BACKEND_URL="http://localhost:8000"

# Run the startup script
CMD ["/app/start.sh"] 