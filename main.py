from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"], 
    allow_credentials=True, 
)

@app.get("/")
def get_info():
    return {
        "email": "frankizuchukwu094@gmail.com",  # my email
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Cashie11/HNG_backend_stage_0.git",  # my Git repo
    }