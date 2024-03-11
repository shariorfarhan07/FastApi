from  fastapi import FastAPI ,Depends , HTTPException
from starlette.middleware.cors import CORSMiddleware

from auth import AuthHandeler
from view import AuthDetails , tweet

import model
auth_handler = AuthHandeler()
app=FastAPI()


# /feeds
@app.get('/')
def index(username=Depends(auth_handler.auth_wrapper)):
    result = model.getNewsFeedData(username)
    return result


@app.post('/register')
async def register(auth:AuthDetails):
    print(AuthDetails)
    users = model.searchUser(auth.username)
    if users :
        raise HTTPException(status_code=400, detail='Username is taken')
    if '@' in auth.username or '@' in auth.password:
        raise HTTPException(status_code=400, detail='Cant contain @ in username or password')
    model.insertUser(auth.username, auth.password)
    return {"message":"account created successfully"}


@app.post('/login')
async def login(auth:AuthDetails):
    u = model.searchUser(auth.username)
    print(u)
    if u == None:
        if  not (u.name==auth.username or u.password == auth.password ):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
    return {'token': u.name+'@'+u.password}


@app.get('/follow/{user_id}')
async def follow(user_id:int,username=Depends(auth_handler.auth_wrapper)):
     return model.follow(username,user_id)


@app.get('/search/')
async def search(search:str ,username=Depends(auth_handler.auth_wrapper)):
    return model.search(search)


@app.post('/post/')
async def post(tweet:tweet ,username=Depends(auth_handler.auth_wrapper)):
    if model.postTweet(tweet, username):
        return  {'message':'successfully tweet posted'}


@app.get('/myprofile')
def index(username=Depends(auth_handler.auth_wrapper)):
    result = model.getmytweetData(username)
    return result

