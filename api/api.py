from mangum import Mangum
from app.main import app

handler = Mangum(app)

# Para desenvolvimento local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 