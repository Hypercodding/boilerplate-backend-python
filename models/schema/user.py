from pydantic import BaseModel


class User_class(BaseModel):
    id: int | None = None
    name: str
    email: str

    class config:
        from_attributes = True

class User_create(User_class):
    name: str
    email: str
    password: str

class User_login(BaseModel):
    email: str
    password: str

class User_response(BaseModel):
    id: int
    name: str
    email: str

    class config:
        form_attributes = True