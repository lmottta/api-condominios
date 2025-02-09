from fastapi import APIRouter
from app.api.v1.endpoints import condominios

api_router = APIRouter()
api_router.include_router(condominios.router, prefix="/condominios", tags=["condominios"]) 