from  fastapi import FastAPI ,Depends , HTTPException
app=FastAPI()

# /feeds
@app.get('/')
def index():
    result = getNewsFeedData()
    return {"farhan":"is the best"}




@app.post('/register')
def register(auth:AuthDetails):
    return {"farhan":"is the best"}


@app.post('/login')
def login(auth:AuthDetails):
    return {"farhan":"is the best"}


@app.get('/follow/{user_id}')
def follow(user_id:int):
    return {"farhan":"is the best"}


@app.get('/search')
def search():
    return {"farhan":"is the best"}


