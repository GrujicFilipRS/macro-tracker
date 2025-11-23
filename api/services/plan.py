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

        plans_list = [plan.to_dict(no_owner=True) for plan in plans]

        content: dict = {
            'message': 'User plans retrieved',
            'plans': plans_list
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.post('/create_plan/')
def create_plan(
    plan_data: dict,
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

        name: str = plan_data.get('name', '')
        num_proteins: int = plan_data.get('num_proteins', 0)
        num_carbs: int = plan_data.get('num_carbs', 0)
        num_fats: int = plan_data.get('num_fats', 0)

        if not name or num_proteins < 0 or num_carbs < 0 or num_fats < 0:
            return JSONResponse(content={'message': 'Invalid plan data'}, status_code=400)

        new_plan = Plan(
            name=name,
            owner_id=user_id,
            num_proteins=num_proteins,
            num_carbs=num_carbs,
            num_fats=num_fats
        )

        db_session.add(new_plan)
        db_session.commit()

        content: dict = {
            'message': 'Plan created successfully',
            'plan': new_plan.to_dict()
        }

        return JSONResponse(content=content, status_code=201)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.delete('/delete_plan/')
def delete_plan(
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

        db_session.delete(plan)
        db_session.commit()

        return JSONResponse(content={'message': 'Plan deleted successfully'}, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()


@router.put('/update_plan/')
def update_plan(
    plan_id: int | None,
    plan_data: dict,
    headers: Annotated[AuthorizationHeader, Header()]
) -> JSONResponse:
    db_session = create_session()
    if plan_id is None:
        return JSONResponse(content={'message': '`plan_id` parameter is necessary'}, status_code=400)

    try:
        plan = db_session.get(Plan, plan_id)
        if not plan:
            return JSONResponse(content={'message': 'Plan not found'}, status_code=404)
        
        token: str = headers.Authorization
        if not token:
            return JSONResponse(content={'message': 'Token required'}, status_code=401)
        
        user_id: int = jwt_tokens.get_user_from_token(token)
        if user_id == -1:
            return JSONResponse(content={'message': 'Invalid token'}, status_code=401)
        
        if plan.owner_id != user_id:
            return JSONResponse(content={'message': 'Unauthorized access to this plan'}, status_code=403)
        
        name: str = plan_data.get('name', plan.name)
        num_proteins: int = plan_data.get('num_proteins', plan.num_proteins)
        num_carbs: int = plan_data.get('num_carbs', plan.num_carbs)
        num_fats: int = plan_data.get('num_fats', plan.num_fats)

        if not name or num_proteins < 0 or num_carbs < 0 or num_fats < 0:
            return JSONResponse(content={'message': 'Invalid plan data'}, status_code=400)
        
        plan.name = name
        plan.num_proteins = num_proteins
        plan.num_carbs = num_carbs
        plan.num_fats = num_fats

        db_session.commit()
        content: dict = {
            'message': 'Plan updated successfully',
            'plan': plan.to_dict()
        }

        return JSONResponse(content=content, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={'message': f'An error occured: {str(e)}'}, status_code=500)
    
    finally:
        db_session.close()