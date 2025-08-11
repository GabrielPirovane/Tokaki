from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.categoria import categoria_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias")
async def get_categorias():
    categorias = categoria_repo.get_all()
    response = templates.TemplateResponse("admin/categorias.html", {"requesst": {}, "categorias": categorias})
    return response