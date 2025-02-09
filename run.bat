@echo off

REM Verificar se o ambiente virtual existe
if not exist ".venv" (
    echo Criando ambiente virtual...
    python -m venv .venv
)

REM Ativar o ambiente virtual
call .venv\Scripts\activate

REM Instalar dependências se necessário
if not exist ".venv\installed" (
    echo Instalando dependências...
    pip install -r requirements.txt
    type nul > .venv\installed
)

REM Rodar o projeto
echo Iniciando o servidor...
uvicorn app.main:app --reload

REM Desativar ambiente virtual ao sair
deactivate 