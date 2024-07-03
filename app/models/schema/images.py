from pydantic import BaseModel

class Image_class(BaseModel):
    image_id: int | None = None
    user_id: int
    filename: str

    class config:
        form_attribute = True

class Image_response(BaseModel):
    image_id: int
    filename: str