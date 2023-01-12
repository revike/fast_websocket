import uvicorn as uvicorn
from fastapi import FastAPI

from endpoints import sending

app = FastAPI()
app.include_router(sending.router, tags=['sending'])

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
