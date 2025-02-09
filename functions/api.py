from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel
from typing import List, Optional, Dict
import json
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

@app.get("/condominios")
async def listar_condominios():
    return condominios

@app.post("/condominios")
async def criar_condominio(condominio: CondominioCreate):
    novo_condominio = Condominio(
        uuid=str(uuid.uuid4()),
        **condominio.dict()
    )
    condominios.append(novo_condominio)
    return novo_condominio

# Handler para Netlify
handler = Mangum(app) 