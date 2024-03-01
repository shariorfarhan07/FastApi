from  fastapi import FastAPI ,Depends , HTTPException

app=FastAPI()

@app.get('/')
def index():
    return {"farhan":"is the best"}