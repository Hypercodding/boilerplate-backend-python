from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user_routes as user
from configurations import configure_cors

app = FastAPI()
configure_cors(app)



app.include_router(user.router, prefix="/users", tags=["users"])
