# HNG Basic info Task API

This is a simple API that returns my email, the current datetime in ISO 8601 format, and the GitHub URL of the project.

## API Documentation
- **Base URL**: `https://your-api-url.com/`
- **Method**: `GET`
- **Response**:
### Endpoint
**GET** `/`

HOW TO SETUP
1.Install Python: Ensure Python 3.7+ is installed on your system.

2.Install FastAPI and Uvicorn:
pip install fastapi uvicorn

3.Create a file named main.py:
4.write your code
from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def get_info():
    return {
        "email": "your-email@example.com",  
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/yourusername/your-repo",  
    }

5.Run the API locally using Uvicorn:
uvicorn main:app --reload

6.Open your browser or use a tool like Postman or curl to test the API:
http://127.0.0.1:8000/

7.You should see the following JSON response:


### Response
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
