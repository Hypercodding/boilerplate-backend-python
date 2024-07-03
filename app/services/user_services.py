from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from ..models import User_create, User_class, User_login, User_response
from ..configurations import conn, cur, create_access_token, decoded_access_token, ACCESS_TOKEN_EXPIRY_MINUTE
from ..utilities import hash_password, verify_password
from datetime import timedelta

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


def get_users():
    cur.execute("SELECT id, name, email FROM users")
    user = cur.fetchall()
    if user is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return user

def create_user_service(user: User_create):
    cur.execute(
    "SELECT id FROM users WHERE email = %s", (user.email,)
    )
    
    existing_user = cur.fetchone()
    if existing_user:
        return {"error": "user already exists"}
    
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    cur.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id, name, email, password", (user.name, user.email, user.password))
    new_user = cur.fetchone()
    conn.commit()
    return new_user

def validate_user(email: str, password: str) -> User_response:
    query = "SELECT id, name, email, password FROM users WHERE email = %s"
    cur.execute(query, (email,))
    user = cur.fetchone()

    if user and verify_password(password, user['password']):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTE)
        access_token = create_access_token(data={"sub": user["email"]}, expires_delta=access_token_expires)
        # decoded = decoded_access_token(access_token)
        print(access_token)
        return { "access_token": access_token, "token_type": "bearer", "id": user["id"], "name": user["name"], "email": user["email"]}
    else:
        return None
    
      
