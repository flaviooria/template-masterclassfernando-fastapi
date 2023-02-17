from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from db import SQLModel, engine

app = FastAPI(title='Api Fernando Responde')
PREFIX_VERSION_API = '/api/v1'

# Add cors, esto nos permite aceptar peticiones de clientes externos o al que demos acceso
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=["*"]
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Add routers, rutas que vamos a establecer para las peticiones