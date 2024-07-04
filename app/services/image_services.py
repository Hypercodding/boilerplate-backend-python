from fastapi import HTTPException, UploadFile
from typing import List
from ..configurations import cur as cursor, conn
import os
import shutil

UPLOAD_DIR = "/mnt/data/uploads" 

def save_image(user_id: int, file: UploadFile) -> dict:
    try:
        # Save image to volume
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            print("uploaded")
        
        # Store image details in database
        cursor.execute(
            "INSERT INTO images (user_id, filename) VALUES (%s, %s) RETURNING image_id",
            (user_id, file.filename)
        )
        result = cursor.fetchone()
        image_id = result['image_id']
        conn.commit()
        
        return {"image_id": image_id, "user_id": user_id, "filename": file.filename}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save image: {str(e)}")


def get_images(user_id: int) -> List[dict]:
    try:
        cursor.execute("SELECT image_id, filename FROM images WHERE user_id = %s", (user_id,))
        images = cursor.fetchall()
        print(images)
        image_data = []
        for image in images:
            image_id = image['image_id']
            filename = image['filename']
            file_path = os.path.join(UPLOAD_DIR, filename)
            print(file_path)
            if os.path.exists(file_path):
                image_data.append({
                    "image_id": image_id,
                    "filename": filename,
                    "url": f"https://boilerplate-backend-python-production.up.railway.app/mnt/data/uploads/{filename}"  # Update this to your production URL
                })
            else:
                # Handle case where file is not found
                raise HTTPException(status_code=404, detail=f"Image '{filename}' not found.")
        
        return image_data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve images: {str(e)}")