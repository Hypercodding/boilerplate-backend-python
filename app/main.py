from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user_routes as user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



def configure_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # This allows all origins, you can restrict it to specific origins if needed
        allow_credentials=True,
        allow_methods=["*"],  # This allows all HTTP methods
        allow_headers=["*"],  # This allows all headers
    )

# Apply CORS settings
configure_cors(app)



app.include_router(user.router, prefix="/users", tags=["users"])
