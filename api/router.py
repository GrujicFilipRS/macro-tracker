from fastapi import FastAPI

def configure_routing(app: FastAPI) -> None:
    from .services.user import router as user_router
    from .services.plan import router as plan_router
    from .services.eaten import router as eaten_router

    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(plan_router, prefix='/plan', tags=['plan'])
    app.include_router(eaten_router, prefix='/eaten', tags=['eaten'])