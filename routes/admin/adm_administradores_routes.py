from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status
from fastapi import Query
from fastapi.requests import Request
from fastapi import Form
from fastapi.templating import Jinja2Templates
from data.adm.adm_repo import AdmRepo
from data.usuario.usuario_repo import UsuarioRepo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

adm_repo = AdmRepo(db_path="dados.db")
usuario_repo = UsuarioRepo(db_path="dados.db")



@router.get("/admin")
async def get_administradores(  request: Request, 
    mensagem: str | None = Query(None), 
    tipo_msg: str = Query("info")
):
    administradores = adm_repo.get_all()
    response = templates.TemplateResponse(
        "admin/categorias.html",
        {
            "request": request,
            "administradores": administradores,
            "mensagem": mensagem,
            "tipo_msg": tipo_msg,
        }
    )
    return response
    

@router.get("/admin/administradores")
async def get_administradores():
    administradores = adm_repo.get_all()
    response = templates.TemplateResponse("/admin/administradores.html", {"request": {}, "administradores": administradores})
    return response

@router.get("/admin/administradores/inserir")
async def get_administradores_inserir():
    response = templates.TemplateResponse("/admin/inserir_adm.html", {"request": {}})
    return response

@router.post("/admin/administradores/inserir")
async def post_administradores_inserir(request: Request, nome: str = Form(...), email: str = Form(...)):
    usuario = usuario_repo.search_paged()
    adm = adm_repo.insert(nome=nome, email=email)
    if adm:
        url = "/admin/administradores?mensagem=Administrador cadastrado com sucesso!"
        return RedirectResponse(url=url, status_code=303)
    url = "/admin/administradores/inserir?mensagem=Erro ao cadastrar administrador."
    return RedirectResponse(url=url, status_code=303)
