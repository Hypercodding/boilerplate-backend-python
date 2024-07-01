from fastapi import HTTPException
from ..models import User_create, User_class, User_login, User_response
from ..configurations import conn, cur


def get_users():
   
        cur.execute("SELECT id, name, email FROM users")
        user = cur.fetchall()
        if user is None:
            raise HTTPException(status_code=404, detail="Users not found")
        return user

def create_user_service(user: User_create):
      cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id, name, email, password", (user.name, user.email, user.password))
      new_user = cur.fetchone()
      conn.commit()
      return new_user

def validate_user(email: str, password: str) -> User_response:
    query = "SELECT id, name, email FROM users WHERE email = %s AND password = %s"
    cur.execute(query, (email, password))
    user = cur.fetchone()
    if user:
        return user
    else:
        return None
      
