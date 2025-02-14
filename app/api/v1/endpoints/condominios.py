from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Dict

from app.schemas.condominio import Condominio, CondominioCreate, CondominioUpdate
from app.services.condominio_service import CondominioService

router = APIRouter()
condominio_service = CondominioService()

@router.post("/", response_model=Condominio)
async def criar_condominio(condominio: CondominioCreate):
    return condominio_service.create(condominio)

@router.get("/", response_model=List[Condominio])
async def listar_condominios(
    nome: Optional[str] = Query(None, description="Filtrar por nome do condomínio"),
    cidade: Optional[str] = Query(None, description="Filtrar por cidade"),
    bairro: Optional[str] = Query(None, description="Filtrar por bairro"),
    skip: int = Query(0, description="Número de registros para pular (paginação)"),
    limit: int = Query(100, description="Número máximo de registros para retornar (paginação)")
):
    return condominio_service.get_all(
        nome=nome, 
        cidade=cidade, 
        bairro=bairro, 
        skip=skip, 
        limit=limit
    )

@router.get("/estatisticas")
async def obter_estatisticas():
    return condominio_service.get_statistics()

@router.get("/busca/nome/{nome}", response_model=List[Condominio])
async def buscar_por_nome(nome: str):
    return condominio_service.get_all(nome=nome)

@router.get("/busca/cidade/{cidade}", response_model=List[Condominio])
async def buscar_por_cidade(cidade: str):
    return condominio_service.get_all(cidade=cidade)

@router.get("/busca/bairro/{bairro}", response_model=List[Condominio])
async def buscar_por_bairro(bairro: str):
    return condominio_service.get_all(bairro=bairro)

@router.get("/{uuid}", response_model=Condominio)
async def obter_condominio(uuid: str):
    condominio = condominio_service.get_by_uuid(uuid)
    if not condominio:
        raise HTTPException(status_code=404, detail="Condomínio não encontrado")
    return condominio

@router.put("/{uuid}", response_model=Condominio)
async def atualizar_condominio(uuid: str, condominio: CondominioUpdate):
    updated_condominio = condominio_service.update(uuid, condominio)
    if not updated_condominio:
        raise HTTPException(status_code=404, detail="Condomínio não encontrado")
    return updated_condominio

@router.delete("/{uuid}")
async def deletar_condominio(uuid: str):
    if not condominio_service.delete(uuid):
        raise HTTPException(status_code=404, detail="Condomínio não encontrado")
    return {"mensagem": "Condomínio deletado com sucesso"} 