from http.server import BaseHTTPRequestHandler
from fastapi import FastAPI, HTTPException, Query
from mangum import Mangum
from pydantic import BaseModel
from typing import List, Optional, Dict
import json
import uuid

app = FastAPI(
    title="API de Condomínios",
    description="API para gerenciamento de informações de condomínios",
    version="1.0.0"
)

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

class Estatisticas(BaseModel):
    total_condominios: int
    condominios_por_bairro: Dict[str, int]

# Lista para armazenar os condomínios (simulando um banco de dados)
condominios: List[Condominio] = []

# Função para popular o banco com dados iniciais
def popular_dados_iniciais():
    # Dados base para geração de condomínios
    condominios_existentes = [
        {
            "nome": "Residencial Vila Olímpia",
            "endereco": "Rua Frei Aureliano de Grotamare",
            "bairro": "SIM",
            "num": "251"
        },
        # ... outros condomínios ...
    ]

    # Adicionar os condomínios existentes
    for cond in condominios_existentes:
        condominio = Condominio(
            uuid=str(uuid.uuid4()),
            nome_do_condominio=cond["nome"],
            endereco=cond["endereco"],
            num=cond["num"],
            bairro=cond["bairro"],
            cidade="Feira de Santana",
            UF="BA"
        )
        condominios.append(condominio)

# Popular dados ao iniciar a aplicação
popular_dados_iniciais()

@app.post("/condominios/", response_model=Condominio)
async def criar_condominio(condominio: CondominioCreate):
    novo_condominio = Condominio(
        uuid=str(uuid.uuid4()),
        nome_do_condominio=condominio.nome_do_condominio,
        endereco=condominio.endereco,
        num=condominio.num,
        bairro=condominio.bairro,
        cidade=condominio.cidade,
        UF=condominio.UF
    )
    condominios.append(novo_condominio)
    return novo_condominio

@app.get("/condominios/", response_model=List[Condominio])
async def listar_condominios(
    nome: Optional[str] = Query(None, description="Filtrar por nome do condomínio"),
    cidade: Optional[str] = Query(None, description="Filtrar por cidade"),
    bairro: Optional[str] = Query(None, description="Filtrar por bairro")
):
    resultados = condominios

    if nome:
        resultados = [c for c in resultados if nome.lower() in c.nome_do_condominio.lower()]
    if cidade:
        resultados = [c for c in resultados if cidade.lower() in c.cidade.lower()]
    if bairro:
        resultados = [c for c in resultados if bairro.lower() in c.bairro.lower()]

    return resultados

@app.get("/condominios/busca/nome/{nome}", response_model=List[Condominio])
async def buscar_por_nome(nome: str):
    resultados = [c for c in condominios if nome.lower() in c.nome_do_condominio.lower()]
    return resultados

@app.get("/condominios/busca/cidade/{cidade}", response_model=List[Condominio])
async def buscar_por_cidade(cidade: str):
    resultados = [c for c in condominios if cidade.lower() in c.cidade.lower()]
    return resultados

@app.get("/condominios/busca/bairro/{bairro}", response_model=List[Condominio])
async def buscar_por_bairro(bairro: str):
    resultados = [c for c in condominios if bairro.lower() in c.bairro.lower()]
    return resultados

@app.get("/condominios/{uuid}", response_model=Condominio)
async def obter_condominio(uuid: str):
    for condominio in condominios:
        if condominio.uuid == uuid:
            return condominio
    raise HTTPException(status_code=404, detail="Condomínio não encontrado")

@app.put("/condominios/{uuid}", response_model=Condominio)
async def atualizar_condominio(uuid: str, condominio_atualizado: Condominio):
    for i, condominio in enumerate(condominios):
        if condominio.uuid == uuid:
            condominio_atualizado.uuid = uuid
            condominios[i] = condominio_atualizado
            return condominio_atualizado
    raise HTTPException(status_code=404, detail="Condomínio não encontrado")

@app.delete("/condominios/{uuid}")
async def deletar_condominio(uuid: str):
    for i, condominio in enumerate(condominios):
        if condominio.uuid == uuid:
            del condominios[i]
            return {"mensagem": "Condomínio deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Condomínio não encontrado")

@app.get("/condominios/estatisticas", response_model=Estatisticas)
async def obter_estatisticas():
    contagem_por_bairro = {}
    for condominio in condominios:
        if condominio.bairro in contagem_por_bairro:
            contagem_por_bairro[condominio.bairro] += 1
        else:
            contagem_por_bairro[condominio.bairro] = 1
    
    return Estatisticas(
        total_condominios=len(condominios),
        condominios_por_bairro=contagem_por_bairro
    )

# Handler para Netlify
handler = Mangum(app)

# Função para ser chamada pelo Netlify
def handler(event, context):
    return Mangum(app)(event, context) 