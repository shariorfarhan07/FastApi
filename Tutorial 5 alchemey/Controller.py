# from fastapi import FastAPI, Depends, HTTPException
# from models import searchUser, insertUser, followUser, fetchFollowedTweets
# from auth import AuthHandler
#
#
# from views import AuthDetails
# app=FastAPI()
#
#
#
#
# auth_handler = AuthHandler()
#
# @app.post('/register', status_code=201)
# def register(auth_details: AuthDetails):
#     users=searchUser(auth_details.username)
#     if len(users)!=0:
#         raise HTTPException(status_code=400, detail='Username is taken')
#     hashed_password = auth_handler.get_password_hash(auth_details.password)
#     insertUser(auth_details.username, hashed_password)
#     return
#
# @app.post('/login')
# def login(auth_details: AuthDetails):
#     user = searchUser(auth_details.username)
#     if (len(user)==0 or (not auth_handler.verify_password(auth_details.password, user[0]['password']))):
#         raise HTTPException(status_code=401, detail='Invalid username and/or password')
#     token = auth_handler.encode_token(user['username'])
#     return {'token': token}
#
#
# @app.get('/follow/{userName}', status_code=200)
# async def follow(userName:str,username=Depends(auth_handler.auth_wrapper)):
#     followUser(username,userName)
#
# @app.get('/feeds', status_code=200)
# async def feeds(id:int,username=Depends(auth_handler.auth_wrapper)):
#     return fetchFollowedTweets(username)
#
#
# @app.get('/search', status_code=200)
# async def search(userName:int,username=Depends(auth_handler.auth_wrapper)):
#     return searchUser(userName)