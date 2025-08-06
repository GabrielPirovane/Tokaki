from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.uf import uf_repo


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_root():
    response = templates.TemplateResponse("home.html", {"request": {}})
    return response

@router.get("/cadastro")
async def get_cadastro():
    uf = uf_repo.UfRepo("dados.db").get_all()
    response = templates.TemplateResponse("cadastro.html", {"request": {}, "uf":uf})
    return response

@router.get("/login")
async def get_login():
    response = templates.TemplateResponse("login.html", {"request": {}})
    return response