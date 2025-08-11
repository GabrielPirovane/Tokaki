from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.adm.adm_repo import AdmRepo


router = APIRouter()
templates = Jinja2Templates(directory="templates")

adm_repo = AdmRepo(db_path="dados.db")

@router.get("/admin/administradores")
async def get_administradores():
    administradores = adm_repo.get_all()
    response = templates.TemplateResponse("/admin/administradores.html", {"request": {}, "administradores": administradores})
    return response

@router.get("/admin/administradores/inserir")
async def get_administradores_inserir():
    response = templates.TemplateResponse("/admin/inserir_adm.html", {"request": {}})
    return response
