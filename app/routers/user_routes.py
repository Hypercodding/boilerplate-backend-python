from fastapi import APIRouter
from ..services import create_user_service, get_users, validate_user
from ..models import User_class, User_create, User_login, User_response

router = APIRouter()

@router.get("/", response_model=list[User_class])
def get_user():
    users = get_users()
    return users

@router.post("/", response_model=User_class)
def create_user(user: User_create):
    new_user = create_user_service(user)
    return new_user 

@router.post("/user-login", response_model=User_response)
def login_validation(user: User_login):
    validated_user = validate_user(user.email, user.password)
    return validated_user