from fastapi.responses import JSONResponse
from fastapi import Header
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Annotated

from ..db.db_session import create_session

from ..models.users import User

from ..utils import jwt_tokens
from .authorization import AuthorizationHeader

from fastapi import APIRouter

router = APIRouter()

class UserAuth(BaseModel):
    username: str
    password: str

@router.get('/get_user/')
async def get_user(
    user_id: int | None
) -> JSONResponse:
    db_session = create_session()

    if user_id is None:
        return JSONResponse(content={'message': '`user_id` parameter is necessary'}, status_code=400)

    try:
        user = db_session.get(User, user_id)

        if not user:
            return JSONResponse(content={'message': 'User not found'}, status_code=404)
        
        content: dict = {
            'message': 'User found',
            'user': user.to_dict()
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.get('/get_current_user/')
def get_current_user(headers: Annotated[AuthorizationHeader, Header()]) -> JSONResponse:
    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        db_sess = create_session()
        if not db_sess.get(User, user_id):
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        content: dict[str, str | int] = {
            'message': 'Successful verification',
            'user_id': user_id
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'Error while creating user: {e}'}, status_code=500)


@router.post('/register/')
async def register(user_data: UserAuth) -> JSONResponse:
    username: str = user_data.username
    password: str = user_data.password

    if not username or not password:
        return JSONResponse(content={'message': 'Username and password required'}, status_code=400)

    if not User.validate_username(username) or not User.validate_password(password):
        return JSONResponse(content={'message': 'Invalid username or password format'}, status_code=400)
    
    db_sess = create_session()

    try:
        if db_sess.query(User).filter_by(username=username).first():
            return JSONResponse(content={'message': 'User with such username already exists'}, status_code=400)
        
        user = User(username=username)
        user.set_password(password)

        db_sess.add(user)
        db_sess.commit()
        
        token: str = jwt_tokens.encode_token(user.id)

        content: dict = {
            'message': 'User created and logged in',
            'user': user.to_dict(),
            'token': token
        }

        return JSONResponse(content=content, status_code=201)
    
    except Exception as e:
        return JSONResponse(content={'message': f'Error while creating user: {e}'}, status_code=500)
    
    finally:
        db_sess.close()


@router.post('/login/')
async def login(user: UserAuth) -> JSONResponse:
    username = user.username
    password = user.password

    if not username or not password:
        return JSONResponse(content={'message': 'Username and password required'}, status_code=400)

    db_sess = create_session()

    try:
        user = db_sess.query(User).filter_by(username=username).first()

        if not user:
            return JSONResponse(content={'message': 'Incorrect credentials'}, status_code=400)
        
        if not user.check_password(password):
            return JSONResponse(content={'message': 'Incorrect credentials'}, status_code=400)
        
        token = jwt_tokens.encode_token(user.id)

        content: dict = {
            'message': 'User logged in',
            'user': user.to_dict(),
            'token': token
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'Error while logging in: {e}'}, status_code=500)

    finally:
        db_sess.close()