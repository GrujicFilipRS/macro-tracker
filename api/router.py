from fastapi import FastAPI

def configure_routing(app: FastAPI) -> None:
    from .services.user import router as user_router
    from .services.plan import router as plan_router

    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(plan_router, prefix='/plan', tags=['plan'])