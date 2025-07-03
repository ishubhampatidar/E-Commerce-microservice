from fastapi import FastAPI
from app.routes import user_route

app = FastAPI(title="API Gateway")

app.include_router(user_route.router, prefix="/api")