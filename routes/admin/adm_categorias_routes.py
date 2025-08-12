from fastapi import APIRouter
from fastapi import Request
from fastapi import Form
from fastapi.templating import Jinja2Templates
from data.categoria.categoria_repo import CategoriaRepo
from data.categoria.categoria_model import Categoria
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

categoria_repo = CategoriaRepo(db_path="dados.db")

@router.get("/admin/categorias")
async def get_categorias():
    categorias = categoria_repo.get_all()
    response = templates.TemplateResponse("admin/categorias.html", {"request": {}, "categorias": categorias})
    return response

@router.get("/admin/categorias/inserir")
async def get_inserir_categorias(request: Request, mensagem: str = None):
    response = templates.TemplateResponse("admin/inserir_categoria.html", {"request": request, "mensagem": mensagem})
    return response

@router.post("/admin/categorias/inserir")
async def post_categoria_inserir(request: Request, nome: str = Form(...), descricao: str = Form(...)):
    categoria = Categoria(id=0, nome=nome, descricao=descricao)
    categorias_encontradas = categoria_repo.search_paged(nome)
    if categorias_encontradas:
        return templates.TemplateResponse("admin/inserir_categoria.html", {"request": request, "mensagem": "Categoria já cadastrada."})
    categoria_id = categoria_repo.insert(categoria)
    if categoria_id:
        url = "/admin/categorias?mensagem=Categoria cadastrada com sucesso!"
        return RedirectResponse(url=url, status_code=303)
    url = "/admin/inserir_categoria?mensagem=Erro ao cadastrar categoria."
    return RedirectResponse(url=url, status_code=303)

@router.get("/admin/categorias/alterar/{id}")
async def get_alterar_categorias(id: int):
    categoria = categoria_repo.get_by_id(id)
    if categoria:
        response = templates.TemplateResponse("admin/alterar_categoria.html", {"request": {}, "categoria": categoria})
        return response
    return templates.TemplateResponse("admin/alterar_categoria.html", {"request": {}, "mensagem": "Categoria não encontrada."})

@router.post("/admin/categorias/alterar")
async def post_categoria_alterar(request: Request, nome: str = Form(...), descricao: str = Form(...)):
    categorias_encontradas = categoria_repo.search_paged(nome)
    if categorias_encontradas:
        categorias = categoria_repo.get_all()
        return templates.TemplateResponse(
            "admin/categorias.html", 
            {
                "request": request,
                "categorias": categorias,
                "mensagem": "Categoria já cadastrada.",
                "tipo_msg": "danger"
            }
        )
    categoria = Categoria(id=0, nome=nome, descricao=descricao)
    if categoria_repo.update(categoria):
        categorias = categoria_repo.get_all()
        return templates.TemplateResponse(
            "admin/categorias.html", 
            {
                "request": request,
                "categorias": categorias,
                "mensagem": "Categoria alterada com sucesso!",
                "tipo_msg": "success"
            }
        )
    categorias = categoria_repo.get_all()
    return templates.TemplateResponse(
        "admin/categorias.html", 
        {
            "request": request,
            "categorias": categorias,
            "mensagem": "Erro ao alterar categoria!",
            "tipo_msg": "danger"
        }
    )
