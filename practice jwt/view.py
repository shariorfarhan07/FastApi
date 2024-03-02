from pydantic import BaseModel,Field

class AuthDetails(BaseModel):
    username: str
    password: str

class tweet(BaseModel):
    id : int
    user : str
    text : str


def user(BaseModel):
    id :int
    name : str
    password : str