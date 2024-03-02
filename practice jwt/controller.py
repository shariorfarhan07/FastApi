from  fastapi import FastAPI ,Depends , HTTPException

from auth import AuthHandeler
from view import AuthDetails

import model
auth_handler = AuthHandeler()
app=FastAPI()

# /feeds
@app.get('/')
def index(username=Depends(auth_handler.auth_wrapper)):
    result = model.getNewsFeedData(username)
    return result


@app.post('/register')
def register(auth:AuthDetails):
    users = model.searchUser(auth.username)
    if len(users) != 0:
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth.password)
    model.insertUser(auth.username, hashed_password)
    return


@app.post('/login')
def login(auth:AuthDetails):
    user = model.searchUser(auth.username)
    if (len(user) == 0 or (not auth_handler.verify_password(auth_details.password, user[0]['password']))):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return {'token': token}


@app.get('/follow/{user_id}')
def follow(user_id:int,username=Depends(auth_handler.auth_wrapper)):
     return model.follow(username,user_id)


@app.get('/search/')
def search(search:str ,username=Depends(auth_handler.auth_wrapper)):
    return model.search(search)


