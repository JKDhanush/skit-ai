# RecoverAI Copilot

## Setup

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### Frontend
cd frontend
pip install -r requirements.txt
streamlit run app.py

## Add API Key
Create .env file in backend:
OPENROUTER_API_KEY=your_key
