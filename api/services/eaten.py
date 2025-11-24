from fastapi.responses import JSONResponse
from fastapi import Header
from typing import Annotated

from ..db.db_session import create_session

from ..models.eaten import Eaten

from ..utils import jwt_tokens
from .authorization import AuthorizationHeader

from fastapi import APIRouter


router = APIRouter()
@router.get('/get_eaten/')
def get_eaten(
    eaten_id: int | None, 
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()

    if eaten_id is None:
        return JSONResponse(content={'message': '`eaten_id` parameter is necessary'}, status_code=400)
    
    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        eaten = db_session.get(Eaten, eaten_id)

        if not eaten:
            return JSONResponse(content={'message': 'Eaten record not found'}, status_code=404)
        
        if eaten.user_id != user_id:
            return JSONResponse(content={'message': 'Unauthorized access to this record'}, status_code=403)

        content: dict = {
            'message': 'Eaten record found',
            'eaten': eaten.to_dict()
        }

        return JSONResponse(content=content, status_code=200)

    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.get('/user_ate_today/')
def user_ate_today(
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()

    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        from datetime import datetime, timedelta, timezone

        today_start = datetime.combine(
            datetime.now(timezone.utc).date(),
            datetime.min.time()
        )

        today_end = today_start + timedelta(days=1)

        eaten_exists = db_session.query(Eaten).filter(
            Eaten.user_id == user_id,
            Eaten.datetime_eaten >= today_start,
            Eaten.datetime_eaten < today_end
        ).first() is not None

        content: dict = {
            'message': 'Eaten records for today checked',
            'ate_today': eaten_exists
        }

        return JSONResponse(content=content, status_code=200)

    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()

@router.get('/get_user_eaten/')
def get_user_eaten(
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()

    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        eaten_records = db_session.query(Eaten).filter(Eaten.user_id == user_id).all()

        eaten_list = [eaten.to_dict() for eaten in eaten_records]

        content: dict = {
            'message': 'Eaten records retrieved',
            'eaten': eaten_list
        }

        return JSONResponse(content=content, status_code=200)

    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.get('/get_today_eaten/')
def get_today_eaten(
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    from datetime import datetime, timedelta, timezone

    db_session = create_session()

    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        today_start = datetime.combine(
            datetime.now(timezone.utc).date(),
            datetime.min.time()
        )

        today_end = today_start + timedelta(days=1)

        eaten_records = db_session.query(Eaten).filter(
            Eaten.user_id == user_id,
            Eaten.datetime_eaten >= today_start,
            Eaten.datetime_eaten < today_end
        ).all()

        eaten_list = [eaten.to_dict() for eaten in eaten_records]

        content: dict = {
            'message': 'Today\'s eaten records retrieved',
            'eaten': eaten_list
        }

        return JSONResponse(content=content, status_code=200)

    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.post('/create_eaten/')
def create_eaten(
    eaten_data: dict,
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()

    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        from datetime import datetime, timezone

        new_eaten = Eaten(
            user_id=user_id,
            food_name=eaten_data.get('food_item'),
            datetime_eaten=datetime.now(timezone.utc),
            num_proteins=eaten_data.get('num_proteins'),
            num_carbs=eaten_data.get('num_carbs'),
            num_fats=eaten_data.get('num_fats')
        )

        db_session.add(new_eaten)
        db_session.commit()

        content: dict = {
            'message': 'Eaten record created',
            'eaten': new_eaten.to_dict()
        }

        return JSONResponse(content=content, status_code=201)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()
    

@router.delete('/delete_eaten/')
def delete_eaten(
    eaten_id: int,
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()

    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        eaten = db_session.get(Eaten, eaten_id)

        if not eaten:
            return JSONResponse(content={'message': 'Eaten record not found'}, status_code=404)
        
        if eaten.user_id != user_id:
            return JSONResponse(content={'message': 'Unauthorized access to this record'}, status_code=403)

        db_session.delete(eaten)
        db_session.commit()

        content: dict = {
            'message': 'Eaten record deleted successfully'
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.put('/update_eaten/')
def update_eaten(
    eaten_id: int,
    eaten_data: dict,
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()

    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        eaten = db_session.get(Eaten, eaten_id)

        if not eaten:
            return JSONResponse(content={'message': 'Eaten record not found'}, status_code=404)
        
        if eaten.user_id != user_id:
            return JSONResponse(content={'message': 'Unauthorized access to this record'}, status_code=403)

        eaten.food_name = eaten_data.get('food_item', eaten.food_name)
        eaten.num_proteins = eaten_data.get('num_proteins', eaten.num_proteins)
        eaten.num_carbs = eaten_data.get('num_carbs', eaten.num_carbs)
        eaten.num_fats = eaten_data.get('num_fats', eaten.num_fats)

        db_session.commit()

        content: dict = {
            'message': 'Eaten record updated successfully',
            'eaten': eaten.to_dict()
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()