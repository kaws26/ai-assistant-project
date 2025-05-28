# 🤖 AI Assistant Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0-FF4B4B.svg)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-009688.svg)](https://fastapi.tiangolo.com/)

A full-stack AI assistant prototype that generates both casual and formal responses to user queries, powered by Groq/Llama3, FastAPI, and Streamlit.

## 🌟 Features

- **Dual Response Generation**
  - Casual responses for everyday conversations
  - Formal responses for academic/professional contexts
  - Powered by Groq/Llama3 AI model

- **Modern User Interface**
  - Clean, responsive design using Streamlit
  - Real-time response generation
  - Interactive conversation history
  - Loading indicators and animations
  - Dark/light mode compatible

- **User Management**
  - Simple authentication system
  - User-specific conversation history
  - Persistent session management

- **Backend Features**
  - FastAPI-based REST API
  - SQLite database for development
  - PostgreSQL support for production
  - Comprehensive error handling
  - API documentation (Swagger/OpenAPI)

## 🛠️ Technology Stack

- **Frontend**
  - Streamlit
  - Streamlit Extras
  - Custom CSS styling
  - Responsive design

- **Backend**
  - FastAPI
  - SQLAlchemy ORM
  - Langchain-Groq
  - Python-dotenv

- **Database**
  - SQLite (Development)
  - PostgreSQL (Production-ready)

- **Testing**
  - Pytest
  - Pytest-asyncio
  - Mock testing

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Groq API key

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaws26/ai-assistant-project.git
   cd ai-assistant-project
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv env
   .\env\Scripts\activate

   # Linux/Mac
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   BACKEND_URL=http://localhost:8000
   USER_ID=default_user
   ```

## 🏃‍♂️ Running the Application

### Development Mode

1. **Start the backend server**
   ```bash
   cd backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start the frontend**
   ```bash
   cd frontend
   streamlit run app.py
   ```

3. **Access the application**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Production Mode

1. **Set up PostgreSQL database**
   ```bash
   # Update DATABASE_URL in .env
   DATABASE_URL=postgresql://user:password@localhost:5432/assistant
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

## 🧪 Testing

Run the test suite:
```bash
cd backend
pytest tests/
```

Test coverage includes:
- API endpoint validation
- AI response generation
- Database operations
- Integration tests

## 📚 API Documentation

The API provides two main endpoints:

1. **Generate Response**
   ```
   POST /generate
   {
     "user_id": "string",
     "query": "string"
   }
   ```

2. **Get History**
   ```
   GET /history?user_id=string
   ```

Full API documentation available at `/docs` when running the backend server.

## 🔒 Security Considerations

- API key management through environment variables
- Input validation and sanitization
- Error handling and logging
- Rate limiting (to be implemented)
- CORS configuration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- [Kawaljeet Singh](https://github.com/kaws26) - Initial work

## 🙏 Acknowledgments

- [Groq/Llama3](https://groq.com/) for AI capabilities
- [Streamlit](https://streamlit.io/) for the frontend framework
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- All contributors and supporters

## 📞 Support

For support, please:
1. Check the [documentation](https://github.com/kaws26/ai-assistant-project/wiki)
2. Open an [issue](https://github.com/kaws26/ai-assistant-project/issues)
3. Contact the maintainers

---

Made with ❤️ by [Kawaljeet Singh](https://github.com/kaws26) using Streamlit, FastAPI, and Groq/Llama3
