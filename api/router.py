from fastapi import FastAPI

def configure_routing(app: FastAPI) -> None:
    from .services.user import router as user_router

    app.include_router(user_router, prefix='/user', tags=['user'])