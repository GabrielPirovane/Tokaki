from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.foto.foto_repo import FotoRepo

router = APIRouter(prefix="/admin/fotos")
templates = Jinja2Templates(directory="templates")

foto_repo = FotoRepo(db_path="dados.db")

@router.get("/")
async def get_fotos():
    fotos = foto_repo.get_all()
    response = templates.TemplateResponse("admin/fotos.html", {"request": {}, "fotos": fotos})
    return response

@router.get("/moderar")
async def get_moderar_fotos():
    fotos = foto_repo.get_all()
    response = templates.TemplateResponse("admin/moderar_fotos.html", {"request": {}, "fotos": fotos})
    return response