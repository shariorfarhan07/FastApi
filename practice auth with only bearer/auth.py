from datetime import datetime, timedelta

from fastapi import HTTPException,Security
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from passlib.context import CryptContext

import jwt

class AuthHandeler():
    security=HTTPBearer()
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # secret = "farhan0125is584the4874best"
    # def get_password_hash(self,password):
    #     return  self.pwd_context.hash(password)
    # def verify_password(self,plain_password,hashed_password):
    #     return  self.pwd_context.verify(plain_password,hashed_password)

    # def encode_token(self, user_id):
    #     payload = {
    #         'exp': datetime.utcnow() + timedelta(days=0, minutes=30),
    #         'iat': datetime.utcnow(),
    #         'sub': user_id
    #     }
    #     return jwt.encode(payload, self.secret, algorithm='HS256')
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        credentials=auth.credentials.split('@')
        return credentials[0]

    # def decode_token(self, token):
    #     try:
    #         payload = jwt.decode(token, self.secret, algorithms=['HS256'])
    #         return payload['sub']
    #     except jwt.ExpiredSignatureError:
    #         raise HTTPException(status_code=401, detail='Signature has expired')
    #     except jwt.InvalidTokenError as e:
    #         raise HTTPException(status_code=401, detail='Invalid token')

