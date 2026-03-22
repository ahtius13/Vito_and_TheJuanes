import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.resolve()))

from fastapi import FastAPI

from routes.create_house import router as create_house_router
from routes.get_houses import router as get_houses_router

app = FastAPI()

app.include_router(create_house_router)
app.include_router(get_houses_router)

@app.get("/")
def root():
    return {"message": "API funcionando"}