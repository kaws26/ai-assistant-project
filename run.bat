@echo off

REM Build the Docker image
docker build -t ai-assistant .

REM Stop and remove existing container if it exists
docker stop ai-assistant 2>nul
docker rm ai-assistant 2>nul

REM Run the container
docker run -d ^
  --name ai-assistant ^
  -p 8000:8000 ^
  -p 8501:8501 ^
  -v "%cd%/data:/app/data" ^
  -e GROQ_API_KEY=%GROQ_API_KEY% ^
  -e USER_ID=%USER_ID% ^
  ai-assistant

echo Application is running!
echo Frontend: http://localhost:8501
echo Backend API: http://localhost:8000
echo API Documentation: http://localhost:8000/docs 