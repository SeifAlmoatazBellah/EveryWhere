import uuid
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from config.database import connectDB

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = 'SECRET'

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        db = connectDB()
        token = uuid.uuid4().hex
        db['tokens'].insert_one({
                "token": token,
                "userId": user_id
            })
        return token

    def decode_token(self, token):
        db = connectDB()
        theToken = db['tokens'].find_one({"token": token})
        return theToken['userId']

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)