from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict
import uuid
import random

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
    bairros_feira = [
        "SIM", "Santa Mônica", "Tomba", "Mangabeira", "Papagaio", "Caseb",
        "Cidade Nova", "Conceição", "Feira IX", "Feira X", "Muchila",
        "Parque Ipê", "Ponto Central", "Queimadinha", "Santo Antônio dos Prazeres",
        "Capuchinhos", "Sobradinho", "Brasília", "Jardim Cruzeiro", "Serraria Brasil",
        "Jardim Acácia", "Asa Branca", "Pedra do Descanso", "Parque Getúlio Vargas",
        "Campo do Gado", "Campo Limpo", "Centro", "Gabriela", "Kalilândia", "Novo Horizonte"
    ]
    
    avenidas_principais = [
        "Avenida Artêmia Pires", "Avenida Fraga Maia", "Avenida João Durval",
        "Avenida Getúlio Vargas", "Avenida Maria Quitéria", "Avenida Nóide Cerqueira",
        "Avenida José Falcão", "Avenida Presidente Dutra", "Avenida Eduardo Fróes da Mota",
        "Avenida Senhor dos Passos"
    ]
    
    ruas = [
        "Rua Professora Edelvira de Oliveira", "Rua Frei Felix de Pacaembu",
        "Rua Voluntários da Pátria", "Rua Japão", "Rua São Domingos",
        "Rua Castro Alves", "Rua Boticário Moncorvo", "Rua Comandante Almiro",
        "Rua Cristóvão Colombo", "Rua da Aurora", "Rua Domingos Barbosa",
        "Rua Floriano Peixoto", "Rua Geminiano Costa", "Rua Intendente Abdon",
        "Rua Juvêncio Erudilho", "Rua Leonídio Rocha", "Rua Marechal Deodoro",
        "Rua Nova", "Rua Olímpio Vital", "Rua Pedro Suzart"
    ]
    
    prefixos = [
        "Residencial", "Condomínio", "Edifício", "Park", "Village", "Plaza",
        "Garden", "Parque", "Solar", "Palace", "Mansão", "Morada", "Jardins",
        "Reserva", "Bosque", "Ville", "Premium", "Eco", "Life", "Club"
    ]
    
    nomes = [
        "Primavera", "Horizonte", "Vista Bela", "Jardim", "Sol Nascente",
        "Bela Vista", "Monte Verde", "Serra Dourada", "Vale Verde", "Recanto",
        "das Flores", "dos Pássaros", "Imperial", "Real", "Elite", "Premium",
        "Privilege", "Classic", "Elegance", "Excellence", "Supreme", "Noble",
        "Golden", "Diamond", "Platinum", "Crystal", "Royal", "Imperial",
        "Paradise", "Oasis", "Splendor", "Harmony", "Serenity", "Victory",
        "Legacy", "Heritage", "Prestige", "Essence", "Unique", "Prime"
    ]
    
    complementos = [
        "I", "II", "III", "IV", "V", "Premium", "Plus", "Elite", "Classic",
        "Master", "VIP", "Special", "Exclusive", "Superior", "Prime"
    ]

    # Adicionar condomínios existentes primeiro
    condominios_existentes = [
        # Condomínios do SIM com endereços reais verificados
        {
            "nome": "Residencial Vila Olímpia",
            "endereco": "Rua Frei Aureliano de Grotamare",
            "bairro": "SIM",
            "num": "251"
        },
        {
            "nome": "Condomínio Terra Nova Feira",
            "endereco": "Avenida Artêmia Pires Freitas",
            "bairro": "SIM",
            "num": "1510"
        },
        {
            "nome": "Condomínio Green Park",
            "endereco": "Rua Frei Aureliano de Grotamare",
            "bairro": "SIM",
            "num": "894"
        },
        {
            "nome": "Condomínio Reserva Feira",
            "endereco": "Avenida Artêmia Pires Freitas",
            "bairro": "SIM",
            "num": "741"
        },
        {
            "nome": "Residencial Le Parc",
            "endereco": "Rua Frei Aureliano de Grotamare",
            "bairro": "SIM",
            "num": "300"
        },
        {
            "nome": "Condomínio Parque Flora",
            "endereco": "Avenida Artêmia Pires Freitas",
            "bairro": "SIM",
            "num": "1200"
        },
        {
            "nome": "Residencial Viva Mais",
            "endereco": "Avenida Artêmia Pires Freitas",
            "bairro": "SIM",
            "num": "520"
        },
        {
            "nome": "Condomínio Alameda Flores",
            "endereco": "Rua São Vicente",
            "bairro": "SIM",
            "num": "455"
        },
        {
            "nome": "Condomínio Villa dos Pássaros",
            "endereco": "Rua Padre Antônio Vieira",
            "bairro": "SIM",
            "num": "632"
        },
        {
            "nome": "Residencial Vista do SIM",
            "endereco": "Avenida Artêmia Pires Freitas",
            "bairro": "SIM",
            "num": "900"
        },
        # Novos condomínios do SIM
        {
            "nome": "Condomínio Bella Vista",
            "endereco": "Rua Frei Aureliano de Grotamare",
            "bairro": "SIM",
            "num": "500"
        },
        {
            "nome": "Residencial Jardim Acácia",
            "endereco": "Avenida Artêmia Pires Freitas",
            "bairro": "SIM",
            "num": "1100"
        },
        # Santa Mônica
        {
            "nome": "Residencial Parque das Acácias",
            "endereco": "Avenida Deputado Colbert Martins",
            "bairro": "Santa Mônica",
            "num": "250"
        },
        {
            "nome": "Condomínio Villa Jardins",
            "endereco": "Avenida Deputado Colbert Martins",
            "bairro": "Santa Mônica",
            "num": "1800"
        },
        {
            "nome": "Residencial Santa Mônica",
            "endereco": "Avenida Deputado Colbert Martins",
            "bairro": "Santa Mônica",
            "num": "1500"
        },
        # Tomba
        {
            "nome": "Condomínio Solar Princesa do Sertão",
            "endereco": "Avenida Eduardo Fróes da Mota",
            "bairro": "Tomba",
            "num": "2500"
        },
        {
            "nome": "Residencial Tomba",
            "endereco": "Avenida Eduardo Fróes da Mota",
            "bairro": "Tomba",
            "num": "3000"
        },
        # Cidade Nova
        {
            "nome": "Residencial Cidade Nova",
            "endereco": "Avenida João Durval Carneiro",
            "bairro": "Cidade Nova",
            "num": "3000"
        },
        {
            "nome": "Condomínio Portal da Cidade",
            "endereco": "Avenida João Durval Carneiro",
            "bairro": "Cidade Nova",
            "num": "2500"
        },
        # Muchila
        {
            "nome": "Residencial Muchila",
            "endereco": "Rua Professora Germiniana da Silva Alves",
            "bairro": "Muchila",
            "num": "600"
        },
        # Centro
        {
            "nome": "Edifício Maria Quitéria",
            "endereco": "Avenida Senhor dos Passos",
            "bairro": "Centro",
            "num": "1234"
        },
        {
            "nome": "Edifício Feira Center",
            "endereco": "Rua Conselheiro Franco",
            "bairro": "Centro",
            "num": "500"
        },
        {
            "nome": "Edifício Boulevard Center",
            "endereco": "Avenida Getúlio Vargas",
            "bairro": "Centro",
            "num": "150"
        },
        # Ponto Central
        {
            "nome": "Residencial Feira Central",
            "endereco": "Rua Castro Alves",
            "bairro": "Ponto Central",
            "num": "150"
        },
        # Kalilândia
        {
            "nome": "Residencial Kalilândia",
            "endereco": "Rua Arnold Silva",
            "bairro": "Kalilândia",
            "num": "400"
        },
        # Capuchinhos
        {
            "nome": "Condomínio Portal dos Capuchinhos",
            "endereco": "Avenida Maria Quitéria",
            "bairro": "Capuchinhos",
            "num": "1800"
        },
        # Sobradinho
        {
            "nome": "Residencial Sobradinho",
            "endereco": "Rua Joaquim Távora",
            "bairro": "Sobradinho",
            "num": "250"
        },
        # Serraria Brasil
        {
            "nome": "Condomínio Serraria",
            "endereco": "Rua Voluntários da Pátria",
            "bairro": "Serraria Brasil",
            "num": "700"
        }
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

    # Gerar novos condomínios até completar 1000
    enderecos_usados = set()
    while len(condominios) < 1000:
        # Gerar endereço único
        rua = random.choice(avenidas_principais + ruas)
        num = str(random.randint(1, 50) * 100)
        endereco_completo = f"{rua}_{num}"
        
        if endereco_completo not in enderecos_usados:
            enderecos_usados.add(endereco_completo)
            
            # Gerar nome único do condomínio
            prefixo = random.choice(prefixos)
            nome = random.choice(nomes)
            complemento = random.choice(complementos) if random.random() > 0.5 else ""
            nome_completo = f"{prefixo} {nome} {complemento}".strip()
            
            condominio = Condominio(
                uuid=str(uuid.uuid4()),
                nome_do_condominio=nome_completo,
                endereco=rua,
                num=num,
                bairro=random.choice(bairros_feira),
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
    # Contar condomínios por bairro
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