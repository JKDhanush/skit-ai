from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.generate import router

app = FastAPI()

# ✅ Allow frontend (Streamlit) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict to your Streamlit URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include your API routes
app.include_router(router)

# ✅ Health check (very useful)
@app.get("/")
def root():
    return {"message": "Backend is running"}