# API de Condomínios

API REST para gerenciamento de informações de condomínios em Feira de Santana.

## Estrutura do Projeto

```
app/
├── api/
│   └── v1/
│       ├── api.py
│       └── endpoints/
│           └── condominios.py
├── core/
│   └── config.py
├── models/
│   └── condominio.py
├── schemas/
│   └── condominio.py
├── services/
│   └── condominio_service.py
└── main.py
```

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório
2. Crie um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a API

Para iniciar o servidor:
```bash
uvicorn app.main:app --reload
```

A API estará disponível em:
- API: `http://localhost:8000/api/v1`
- Documentação Swagger: `http://localhost:8000/docs`
- Documentação ReDoc: `http://localhost:8000/redoc`

## Endpoints Disponíveis

### Condomínios

- `POST /api/v1/condominios/` - Criar novo condomínio
- `GET /api/v1/condominios/` - Listar todos os condomínios
- `GET /api/v1/condominios/{uuid}` - Obter um condomínio específico
- `PUT /api/v1/condominios/{uuid}` - Atualizar um condomínio
- `DELETE /api/v1/condominios/{uuid}` - Deletar um condomínio

### Busca e Filtros

- `GET /api/v1/condominios/?nome=&cidade=&bairro=` - Filtrar condomínios
- `GET /api/v1/condominios/busca/nome/{nome}` - Buscar por nome
- `GET /api/v1/condominios/busca/cidade/{cidade}` - Buscar por cidade
- `GET /api/v1/condominios/busca/bairro/{bairro}` - Buscar por bairro

### Estatísticas

- `GET /api/v1/condominios/estatisticas` - Obter estatísticas dos condomínios

## Exemplo de Payload

```json
{
    "nome_do_condominio": "Residencial Exemplo",
    "endereco": "Avenida Artêmia Pires Freitas",
    "num": "1200",
    "bairro": "SIM",
    "cidade": "Feira de Santana",
    "UF": "BA"
}
```

O campo `uuid` é gerado automaticamente pelo sistema. 