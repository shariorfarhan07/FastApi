from pydantic import BaseModel,Field

class AuthDetails(BaseModel):
    username: str
    password: str

class tweet(BaseModel):
    id : int
    user : str
    text : str