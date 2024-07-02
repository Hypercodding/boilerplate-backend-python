from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def configure_cors(app: FastAPI):
    # origins = [
    #     "http://localhost",
    #     "http://localhost:3000",  # Adjust this to your frontend URL
    #     "http://localhost:3001",  # Adjust this to your frontend URL
    #     "http://localhost:8000",  # Adjust this to your backend URL
    #     "http://localhost:8080",  # Adjust this to your backend URL
    #     "http://127.0.0.1:8000",   # Allow requests from FastAPI running locally
    # ]

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
