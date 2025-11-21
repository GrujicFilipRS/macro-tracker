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
def get_plan():
    pass