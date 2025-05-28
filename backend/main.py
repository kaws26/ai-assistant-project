from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import schemas, models, database
from database import get_db
from models import generate_responses
from datetime import datetime
import uuid
import os

app = FastAPI(
    title="AI Assistant API",
    description="API for AI Assistant with Groq/Llama3 integration",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    """Root endpoint that returns API information"""
    return {
        "message": "Welcome to AI Assistant API",
        "version": "1.0.0",
        "endpoints": {
            "root": "/",
            "generate": "/generate",
            "history": "/history",
            "docs": "/docs"
        },
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/generate", response_model=schemas.GenerateResponse)
async def generate_response(
    request: schemas.GenerateRequest, 
    db: Session = Depends(get_db)
):
    """Generate AI responses for a given query"""
    try:
        # Generate AI responses
        casual, formal = generate_responses(request.query)
        
        # Save to database
        prompt = database.Prompt(
            user_id=request.user_id,
            query=request.query,
            casual_response=casual,
            formal_response=formal
        )
        db.add(prompt)
        db.commit()
        db.refresh(prompt)
        
        return {
            "casual_response": casual,
            "formal_response": formal
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history", response_model=schemas.HistoryResponse)
async def get_history(user_id: str, db: Session = Depends(get_db)):
    """Get conversation history for a user"""
    try:
        history = db.query(database.Prompt).filter(
            database.Prompt.user_id == user_id
        ).order_by(database.Prompt.created_at.desc()).all()
        
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {
        "error": "Not Found",
        "message": "The requested resource was not found",
        "path": request.url.path
    }

@app.exception_handler(500)
async def server_error_handler(request, exc):
    return {
        "error": "Internal Server Error",
        "message": str(exc),
        "path": request.url.path
    }