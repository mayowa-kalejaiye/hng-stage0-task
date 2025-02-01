from fastapi import FastAPI  # Import FastAPI class from the fastapi module
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware class from the fastapi.middleware.cors module
from datetime import datetime  # Import datetime class from the datetime module
import pytz  # Import pytz module for timezone handling

app = FastAPI()  # Create an instance of the FastAPI class

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins 
    allow_credentials=True,
    allow_methods=["GET"], # Only allow GET requests
    allow_headers=["*"] # Allow all headers
)

@app.get("/")  # GET endpoint at the root URL
def get_info():
    """
    This endpoint returns a JSON object containing the email, current datetime in UTC, and GitHub URL.
    """
    return {
        "email": 'kalejaiyemayowa3@gmail.com',  # Get the email 
        "current_datetime": datetime.now(pytz.utc).replace(microsecond=0).isoformat()[:-6] + "Z",  # Fix the current datetime format (ISO 8601 without microseconds, add "Z")
        "github_url": 'https://github.com/mayowa-kalejaiye/hng-stage0-task'  # Get the GitHub URL
    }
