from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status
from fastapi import Query
from fastapi.requests import Request
from fastapi import Form
from fastapi.templating import Jinja2Templates
from data.categoria.categoria_repo import CategoriaRepo
from data.categoria.categoria_model import Categoria

router = APIRouter()
templates = Jinja2Templates(directory="templates")

categoria_repo = CategoriaRepo(db_path="dados.db")

@router.get("/admin/categorias")
async def get_categorias(
    request: Request, 
    mensagem: str | None = Query(None), 
    tipo_msg: str = Query("info")
):
    categorias = categoria_repo.get_all()
    response = templates.TemplateResponse(
        "admin/categorias.html",
        {
            "request": request,
            "categorias": categorias,
            "mensagem": mensagem,
            "tipo_msg": tipo_msg,
        }
    )
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
        url = "/admin/categorias?mensagem=Esta categoria já existe!&tipo_msg=danger"
        return RedirectResponse(url=url, status_code=303)
    categoria_id = categoria_repo.insert(categoria)
    if categoria_id:
        url = "/admin/categorias?mensagem=Categoria cadastrada com sucesso!&type_msg=success"
        return RedirectResponse(url=url, status_code=303)
    url = "/admin/categorias?mensagem=Esta categoria já existe!&tipo_msg=danger"

    return RedirectResponse(url=url,  status_code=303)

@router.get("/admin/categorias/alterar/{id}")
async def get_alterar_categorias(request: Request, id: int, mensagem: str = None, tipo_msg: str = "info"):
    categoria = categoria_repo.get_by_id(id)
    if categoria:
        return templates.TemplateResponse(
            "admin/alterar_categoria.html",
            {
                "request": request,
                "categoria": categoria,
                "mensagem": mensagem,
                "tipo_msg": tipo_msg
            }
        )
    else:
        return templates.TemplateResponse(
            "admin/alterar_categoria.html",
            {
                "request": request,
                "mensagem": "Categoria não encontrada.",
                "tipo_msg": "danger"
            }
        )

@router.post("/admin/categorias/alterar/{id}")
async def post_categoria_alterar(id: int, nome: str = Form(...), descricao: str = Form(...)):
    categorias_encontradas = categoria_repo.search_paged(nome)
    categoria_atual = categoria_repo.get_by_id(id)
    if categorias_encontradas:
        # Redireciona para a página GET com mensagem de erro
        url = "/admin/categorias?mensagem=Categoria já cadastrada.&tipo_msg=danger"
        return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    categoria = Categoria(id=id, nome=nome, descricao=descricao)
    atualizacao = categoria_repo.update(categoria)
    if atualizacao:
        url = "/admin/categorias?mensagem=Categoria alterada com sucesso!&tipo_msg=success"
        return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    
    url = "/admin/categorias?mensagem=Erro ao alterar categoria.&tipo_msg=danger"
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@router.post("/admin/categorias/excluir/{id}")
async def get_excluir_categorias(id: int, mensagem: str = None, tipo_msg: str = "info"):
    if categoria_repo.delete(id):
        url = "/admin/categorias?mensagem=Categoria excluida com sucesso!&tipo_msg=success"
        return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    url = "/admin/categorias?mensagem=Erro ao excluir categoria.&tipo_msg=danger"
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)