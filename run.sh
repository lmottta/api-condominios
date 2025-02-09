#!/bin/bash

# Ativar ambiente virtual
if [ ! -d ".venv" ]; then
    echo "Criando ambiente virtual..."
    python -m venv .venv
fi

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar dependências se necessário
if [ ! -f ".venv/installed" ]; then
    echo "Instalando dependências..."
    pip install -r requirements.txt
    touch .venv/installed
fi

# Rodar o projeto
echo "Iniciando o servidor..."
uvicorn app.main:app --reload

# Desativar ambiente virtual ao sair
deactivate 