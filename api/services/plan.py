from fastapi.responses import JSONResponse
from fastapi import Header
from pydantic import BaseModel
from typing import Annotated

from ..db.db_session import create_session

from ..models.plans import Plan

from ..utils import jwt_tokens
from .authorization import AuthorizationHeader

from fastapi import APIRouter

router = APIRouter()


@router.get('/get_plan/')
def get_plan(
    plan_id: int | None, 
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()

    if plan_id is None:
        return JSONResponse(content={'message': '`plan_id` parameter is necessary'}, status_code=400)

    try:
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)

        plan = db_session.get(Plan, plan_id)

        if not plan:
            return JSONResponse(content={'message': 'Plan not found'}, status_code=404)
        
        if plan.owner_id != user_id:
            return JSONResponse(content={'message': 'Unauthorized access to this plan'}, status_code=403)

        content: dict = {
            'message': 'Plan found',
            'plan': plan.to_dict()
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()
    

@router.get('/get_user_plans/')
def get_user_plans(
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

        plans = db_session.query(Plan).filter(Plan.owner_id == user_id).all()

        plans_list = [plan.to_dict() for plan in plans]

        content: dict = {
            'message': 'User plans retrieved',
            'plans': plans_list
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()