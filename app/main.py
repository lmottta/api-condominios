from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """
    Redireciona para a documentação da API
    """
    return RedirectResponse(url="/docs")

@app.get("/api/v1")
async def api_root():
    """
    Informações sobre a API
    """
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "endpoints": {
            "documentação": "/docs",
            "condomínios": "/api/v1/condominios/",
            "estatísticas": "/api/v1/condominios/estatisticas",
            "busca": {
                "por_nome": "/api/v1/condominios/busca/nome/{nome}",
                "por_cidade": "/api/v1/condominios/busca/cidade/{cidade}",
                "por_bairro": "/api/v1/condominios/busca/bairro/{bairro}"
            }
        }
    }

app.include_router(api_router, prefix=settings.API_V1_STR) 