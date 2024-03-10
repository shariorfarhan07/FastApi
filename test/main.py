from typing import List
from uuid import uuid4,UUID

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from models import User, Gender, Role

from fastapi import FastAPI, HTTPException, Depends, Security
import logging
logging.basicConfig( level=logging.INFO)


app=FastAPI()
security=HTTPBearer()

db: List[User] = [
        User(
            id='cb53f63d-d2c6-49d3-a10d-44e982d4a2ef',
            first_name='farhan',
            last_name='sharior',
            gender=Gender.male,
            roles=[Role.admin]
        ),
        User(
            id='985e0473-0956-4dd0-b037-f95d5e3c8cde',
            first_name='alisa',
            last_name='milman',
            gender=Gender.female,
            roles=[Role.student,Role.user]
        ),

    ]


def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
    return self.decode_token(auth.credentials)


@app.get("/")
def root(username=Depends(auth_wrapper)):
    logging.info('test')
    return {"hello":"world"}

@app.get('/api/v1/users')
async def fetch_users():
    return db;

@app.post('/api/v1/users')
async def register_user(user:User):
    db.append(user)
    return {'id':user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db. remove (user)
        return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
)