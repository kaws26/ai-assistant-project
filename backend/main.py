from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import schemas, models, database
from database import get_db
from models import generate_responses
from datetime import datetime
import uuid
import os
from pathlib import Path

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the frontend static files
frontend_path = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")

@app.get("/")
async def read_root():
    return FileResponse(str(frontend_path / "app.py"))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/generate", response_model=schemas.GenerateResponse)
async def generate_response(
    request: schemas.GenerateRequest, 
    db: Session = Depends(get_db)
):
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
    try:
        history = db.query(database.Prompt).filter(
            database.Prompt.user_id == user_id
        ).order_by(database.Prompt.created_at.desc()).all()
        
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))