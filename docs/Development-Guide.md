# Development Guide

## Development Environment Setup

### Prerequisites
- Python 3.10+
- Git
- Docker and Docker Compose
- A code editor (VS Code recommended)
- Groq API key

### Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kaws26/ai-assistant-project.git
   cd ai-assistant-project
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv env
   
   # Activate virtual environment
   # On Windows:
   env\Scripts\activate
   # On Unix or MacOS:
   source env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   # Install frontend dependencies
   cd frontend
   pip install -r requirements.txt
   
   # Install backend dependencies
   cd ../backend
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   # Copy example environment file
   cp .env.example .env
   
   # Edit .env with your configuration
   # Required variables:
   # - GROQ_API_KEY
   # - USER_ID
   ```

### Development Workflow

1. **Running Services Locally**

   **Backend:**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

   **Frontend:**
   ```bash
   cd frontend
   streamlit run app.py
   ```

2. **Running with Docker**
   ```bash
   # Build and run all services
   docker-compose up --build
   
   # Run specific service
   docker-compose up backend
   docker-compose up frontend
   ```

## Code Structure

### Frontend (`frontend/`)
- `app.py`: Main Streamlit application
- `requirements.txt`: Frontend dependencies
- `Dockerfile`: Frontend container configuration

### Backend (`backend/`)
- `main.py`: FastAPI application and routes
- `database.py`: Database models and operations
- `requirements.txt`: Backend dependencies
- `Dockerfile`: Backend container configuration

## Development Guidelines

### Code Style
- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

### Git Workflow
1. Create a new branch for each feature/fix
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. Push changes and create a pull request
   ```bash
   git push origin feature/your-feature-name
   ```

### Testing
- Write unit tests for new features
- Run tests before committing
- Ensure all tests pass before creating a PR

### Documentation
- Update documentation for new features
- Keep API documentation up to date
- Add comments for complex logic

## Common Tasks

### Adding a New Feature
1. Create a new branch
2. Implement the feature
3. Add tests
4. Update documentation
5. Create a pull request

### Debugging
1. Check logs:
   ```bash
   # Backend logs
   docker-compose logs backend
   
   # Frontend logs
   docker-compose logs frontend
   ```

2. Use debug mode:
   ```bash
   # Backend
   uvicorn main:app --reload --log-level debug
   
   # Frontend
   streamlit run app.py --logger.level=debug
   ```

### Database Management
1. Access SQLite database:
   ```bash
   sqlite3 data/assistant.db
   ```

2. Common SQLite commands:
   ```sql
   .tables                    -- List all tables
   .schema table_name         -- Show table schema
   SELECT * FROM table_name;  -- Query data
   ```

## Performance Optimization

### Frontend
- Minimize API calls
- Use caching where appropriate
- Optimize Streamlit components

### Backend
- Implement proper indexing
- Use connection pooling
- Optimize database queries

## Security Best Practices

1. **API Security**
   - Never expose API keys
   - Implement rate limiting
   - Validate all inputs

2. **Data Security**
   - Encrypt sensitive data
   - Use secure connections
   - Implement proper authentication

3. **Environment Variables**
   - Never commit .env files
   - Use secure defaults
   - Validate environment variables

## Troubleshooting

### Common Issues

1. **Port Conflicts**
   ```bash
   # Check if ports are in use
   netstat -ano | findstr :8000
   netstat -ano | findstr :8501
   ```

2. **Database Issues**
   ```bash
   # Check database file
   ls -l data/assistant.db
   
   # Check permissions
   chmod 644 data/assistant.db
   ```

3. **Docker Issues**
   ```bash
   # Clean up Docker
   docker-compose down
   docker system prune
   ```

## Getting Help

- Check the [GitHub Issues](https://github.com/kaws26/ai-assistant-project/issues)
- Review the [API Documentation](http://localhost:8000/docs)
- Contact the maintainers

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 