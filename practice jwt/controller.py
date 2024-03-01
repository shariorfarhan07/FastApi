from  fastapi import FastAPI ,Depends , HTTPException
app=FastAPI()

# /feeds
@app.get('/')
def index(username=Depends(auth_handler.auth_wrapper)):
    result = getNewsFeedData()
    return result




@app.post('/register')
def register(auth:AuthDetails):
    return {"farhan":"is the best"}


@app.post('/login')
def login(auth:AuthDetails):
    return {"farhan":"is the best"}


@app.get('/follow/{user_id}')
def follow(user_id:int,username=Depends(auth_handler.auth_wrapper)):
    return {"farhan":"is the best"}


@app.get('/search/')
def search(search:str ,username=Depends(auth_handler.auth_wrapper)):
    return {"farhan":"is the best"}


