from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.create_house import router as create_house_router
from routes.get_houses import router as get_houses_router
from routes.filter_houses import router as filter_houses_router

app = FastAPI(
    title="API de Viviendas",
    description="Sistema de predicción de precios y generación de descripciones",
    version="1.2"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False, 
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(create_house_router)
app.include_router(get_houses_router)
app.include_router(filter_houses_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}