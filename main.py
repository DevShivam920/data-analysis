# main.py (in root folder)
from fastapi import FastAPI
from app.api.routes import router  # absolute import works now

app = FastAPI()
app.include_router(router)