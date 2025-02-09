from mangum import Mangum
from fastapi import FastAPI
from app.main import app

# Configurar o handler para o Netlify
handler = Mangum(app, lifespan="off")

# Para desenvolvimento local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 