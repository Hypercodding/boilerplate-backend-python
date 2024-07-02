from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from ..routers import user_routes as user

def configure_cors(app: FastAPI):
    origins = [
        "http://localhost",
        "http://localhost:3000",  # Adjust this to your frontend URL
        "http://localhost:3001",  # Adjust this to your frontend URL
        "http://localhost:8000",  # Adjust this to your backend URL
        "http://localhost:8080",  # Adjust this to your backend URL
        "http://127.0.0.1:8000",  # Allow requests from FastAPI running locally
        "https://figma-login-signup.vercel.app"  # Allow your Vercel frontend
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

