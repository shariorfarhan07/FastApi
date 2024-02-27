from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID,uuid4,uuid3
from enum import Enum


class Gender(str, Enum):
    male  ='Male'
    female='Female'

class Role(str, Enum):
    admin  = 'admin'
    user   = 'user'
    student= 'student'


class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:str
    last_name:str
    gender:Gender
    roles:List[Role]

