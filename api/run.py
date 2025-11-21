from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import traceback
from dotenv import load_dotenv

from .db import db_session
from .router import configure_routing

load_dotenv()
db_session.global_init(os.getenv('DB_FILE', 'db/database.sqlite'))

app = FastAPI()

FRONTEND_URL: str = os.getenv('FRONTEND_URL', '*')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()
    return JSONResponse(
        status_code=400,
        content={'message': str(exc)}
    )

configure_routing(app)