from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from fastapi.middleware.cors import CORSMiddleware
from .routers import user_routes as user, image_routers as image
from .configurations import configure_cors


app = FastAPI()
uploads_directory = "/mnt/data/uploads"


configure_cors(app)

@app.get("/list-uploads")
async def list_uploads():
    files = os.listdir(uploads_directory)
    return {"files": files}

if not os.path.exists(uploads_directory):
    os.makedirs(uploads_directory)

app.mount("/uploads", StaticFiles(directory=uploads_directory), name="uploads")


app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(image.router, prefix="/image", tags=["image"])
