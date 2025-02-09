# API de Condomínios

Esta é uma API REST para gerenciamento de informações de condomínios.

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a API

Para iniciar o servidor:
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

A documentação da API (Swagger UI) estará disponível em `http://localhost:8000/docs`

## Endpoints Disponíveis

- `POST /condominios/` - Criar novo condomínio
- `GET /condominios/` - Listar todos os condomínios
- `GET /condominios/{uuid}` - Obter um condomínio específico
- `PUT /condominios/{uuid}` - Atualizar um condomínio
- `DELETE /condominios/{uuid}` - Deletar um condomínio

## Exemplo de Payload

```json
{
    "nome_do_condominio": "Residencial Exemplo",
    "endereco": "Rua das Flores",
    "num": "123",
    "bairro": "Centro",
    "cidade": "São Paulo",
    "UF": "SP"
}
```

O campo `uuid` é gerado automaticamente pelo sistema. 