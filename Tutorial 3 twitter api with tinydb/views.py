from pydantic import BaseModel, Field


class AuthDetails(BaseModel):
    username: str
    password: str


class tweets(BaseModel):
    user_id:int
    userName:str
    tweet:str =Field(max_length=255)