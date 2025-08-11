from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.categoria.categoria_repo import CategoriaRepo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

categoria_repo = CategoriaRepo(db_path="dados.db")

@router.get("/admin/categorias")
async def get_categorias():
    categorias = categoria_repo.get_all()
    response = templates.TemplateResponse("admin/categorias.html", {"request": {}, "categorias": categorias})
    return response

@router.get("/admin/categorias/inserir")
async def get_inserir_categorias():
    response = templates.TemplateResponse("admin/inserir_categoria.html", {"request": {}})
    return response