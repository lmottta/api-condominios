from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel
from typing import List, Optional, Dict
import uuid

app = FastAPI()

class CondominioBase(BaseModel):
    nome_do_condominio: str
    endereco: str
    num: str
    bairro: str
    cidade: str
    UF: str

class CondominioCreate(CondominioBase):
    pass

class Condominio(CondominioBase):
    uuid: str

# Lista para armazenar os condomínios
condominios: List[Condominio] = []

@app.get("/")
async def root():
    return {"message": "API de Condomínios"}

@app.get("/condominios", response_model=List[Condominio])
async def listar_condominios():
    return condominios

@app.post("/condominios", response_model=Condominio)
async def criar_condominio(condominio: CondominioCreate):
    novo_condominio = Condominio(
        uuid=str(uuid.uuid4()),
        **condominio.dict()
    )
    condominios.append(novo_condominio)
    return novo_condominio

@app.get("/condominios/{uuid}", response_model=Condominio)
async def obter_condominio(uuid: str):
    for condominio in condominios:
        if condominio.uuid == uuid:
            return condominio
    raise HTTPException(status_code=404, detail="Condomínio não encontrado")

@app.put("/condominios/{uuid}", response_model=Condominio)
async def atualizar_condominio(uuid: str, condominio_atualizado: CondominioCreate):
    for i, condominio in enumerate(condominios):
        if condominio.uuid == uuid:
            novo_condominio = Condominio(
                uuid=uuid,
                **condominio_atualizado.dict()
            )
            condominios[i] = novo_condominio
            return novo_condominio
    raise HTTPException(status_code=404, detail="Condomínio não encontrado")

@app.delete("/condominios/{uuid}")
async def deletar_condominio(uuid: str):
    for i, condominio in enumerate(condominios):
        if condominio.uuid == uuid:
            del condominios[i]
            return {"message": "Condomínio deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Condomínio não encontrado")

# Handler para Netlify
handler = Mangum(app, lifespan="off") 