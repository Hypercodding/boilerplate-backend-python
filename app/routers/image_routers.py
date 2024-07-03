from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from typing import List
from ..services import save_image, get_images
from ..models import Image_class as Image, Image_response

router = APIRouter()

@router.post("/images/", response_model=Image)
async def upload_image(user_id: int, file: UploadFile = File(...)):
    return save_image( user_id,file)

@router.get("/images/", response_model=List[Image_response])
async def read_images(user_id: int):
    return get_images(user_id)
