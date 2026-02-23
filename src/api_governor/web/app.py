from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api_governor.web.routes import router
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="API Governor")

app.include_router(router)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")