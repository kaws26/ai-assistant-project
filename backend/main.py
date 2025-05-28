from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
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

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Read the Streamlit app file
    with open(frontend_path / "app.py", "r") as f:
        app_content = f.read()
    
    # Create HTML that will run the Streamlit app
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>AI Assistant</title>
            <script src="https://cdn.jsdelivr.net/npm/streamlit-component-lib@1.5.0/dist/index.js"></script>
            <script>
                // Initialize Streamlit
                window.streamlit = new Streamlit();
                
                // Load the app
                async function loadApp() {{
                    const response = await fetch('/static/app.py');
                    const appCode = await response.text();
                    window.streamlit.runPython(appCode);
                }}
                
                // Start the app when the page loads
                window.onload = loadApp;
            </script>
        </head>
        <body>
            <div id="root"></div>
        </body>
    </html>
    """
    return html_content

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/generate", response_model=schemas.GenerateResponse)
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

@app.get("/api/history", response_model=schemas.HistoryResponse)
async def get_history(user_id: str, db: Session = Depends(get_db)):
    try:
        history = db.query(database.Prompt).filter(
            database.Prompt.user_id == user_id
        ).order_by(database.Prompt.created_at.desc()).all()
        
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))