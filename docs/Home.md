# AI Assistant Project Wiki

## Overview
This project is an AI-powered assistant that combines a Streamlit frontend with a FastAPI backend, utilizing the Groq API for AI interactions. The application is containerized using Docker for easy deployment and scalability.

## Table of Contents
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Features](#features)
- [Configuration](#configuration)
- [Development](#development)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Docker and Docker Compose
- Groq API key

### Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/kaws26/ai-assistant-project.git
   cd ai-assistant-project
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. Run with Docker:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Project Structure
```
ai-assistant-project/
├── frontend/
│   ├── app.py              # Streamlit frontend application
│   ├── Dockerfile          # Frontend container configuration
│   └── requirements.txt    # Frontend dependencies
├── backend/
│   ├── main.py            # FastAPI backend application
│   ├── database.py        # Database models and operations
│   ├── Dockerfile         # Backend container configuration
│   └── requirements.txt   # Backend dependencies
├── data/                  # SQLite database storage
├── docs/                  # Documentation
├── docker-compose.yaml    # Docker services configuration
├── .env.example          # Environment variables template
└── README.md             # Project overview
```

## Features
- **Modern UI**: Clean and responsive Streamlit interface
- **Real-time AI Interactions**: Powered by Groq API
- **Persistent Storage**: SQLite database for conversation history
- **Containerized**: Easy deployment with Docker
- **API Documentation**: Auto-generated Swagger UI
- **Environment Configuration**: Flexible setup with .env files

## Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key
- `USER_ID`: User identifier (defaults to 'default_user')
- `DATABASE_URL`: SQLite database URL
- `ENVIRONMENT`: 'development' or 'production'
- `DEBUG`: Enable/disable debug mode
- `BACKEND_URL`: Backend service URL
- `STREAMLIT_SERVER_PORT`: Frontend port (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Frontend address (default: 0.0.0.0)

### Database
The project uses SQLite for data persistence. The database file is stored in the `data` directory and is mounted as a volume in Docker.

## Development

### Local Development
1. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   # Frontend
   cd frontend
   pip install -r requirements.txt

   # Backend
   cd ../backend
   pip install -r requirements.txt
   ```

3. Run services:
   ```bash
   # Backend
   cd backend
   uvicorn main:app --reload

   # Frontend
   cd frontend
   streamlit run app.py
   ```

### Docker Development
```bash
# Build and run all services
docker-compose up --build

# Run specific service
docker-compose up backend
docker-compose up frontend
```

## Deployment

### Production Deployment
1. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with production values
   ```

2. Build and run with Docker:
   ```bash
   docker-compose -f docker-compose.yaml up -d
   ```

### Health Checks
The backend service includes health checks that monitor:
- API availability
- Database connectivity
- Service responsiveness

## Troubleshooting

### Common Issues

1. **Port Conflicts**
   - Ensure ports 8000 and 8501 are available
   - Check for running services using these ports

2. **Database Issues**
   - Verify data directory permissions
   - Check database file existence
   - Ensure proper SQLite configuration

3. **API Connection**
   - Verify GROQ_API_KEY is set correctly
   - Check backend service health
   - Ensure proper network connectivity

4. **Docker Issues**
   - Check Docker service status
   - Verify Docker Compose installation
   - Ensure proper volume permissions

### Getting Help
- Check the [GitHub Issues](https://github.com/kaws26/ai-assistant-project/issues)
- Review the [API Documentation](http://localhost:8000/docs)
- Contact the maintainers

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 