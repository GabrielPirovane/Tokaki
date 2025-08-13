from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status
from fastapi import Query
from fastapi.requests import Request
from fastapi import Form
from fastapi.templating import Jinja2Templates
from data.adm.adm_repo import AdmRepo
from data.adm.adm_model import Administrador
from data.usuario.usuario_repo import UsuarioRepo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

adm_repo = AdmRepo(db_path="dados.db")
usuario_repo = UsuarioRepo(db_path="dados.db")

def confirmar_usuario(nome: str, email: str):
    #Conferindo se o nome e o email existem no banco de dados
    if not usuario_repo.search_paged_nome(nome) or not usuario_repo.search_paged_email(email):
        return None
    usuario_id_nome = usuario_repo.search_paged_nome(nome)[0].id
    usuario_id_email = usuario_repo.search_paged_email(email)[0].id
    #Conferindo se o email e o nome pertence ao mesmo usuário
    if usuario_id_nome == usuario_id_email:
        return usuario_id_email
        
@router.get("/admin")
async def get_administradores():
    response = templates.TemplateResponse("admin/area_adm.html", {"request": {}})
    return response

@router.get("/admin/administradores")
async def get_administradores(
    request: Request, 
    mensagem: str | None = Query(None), 
    tipo_msg: str = Query("info")
):
    administradores = adm_repo.get_all()
    response = templates.TemplateResponse(
        "admin/administradores.html",
        {
            "request": request,
            "administradores": administradores,
            "mensagem": mensagem,
            "tipo_msg": tipo_msg,
        }
    )
    return response

@router.get("/admin/administradores/inserir")
async def get_administradores_inserir():
    response = templates.TemplateResponse("/admin/inserir_adm.html", {"request": {}})
    return response

@router.post("/admin/administradores/inserir")
async def post_administradores_inserir(request: Request, nome: str = Form(...), email: str = Form(...)):
    adm_id = confirmar_usuario(nome, email)
    if adm_id is not None:
        adm = Administrador(id=adm_id)
        id_inserido = adm_repo.insert(adm)
        if adm_id == id_inserido and id_inserido is not None:
            url = "/admin/administradores?mensagem=Administrador cadastrado com sucesso!&type_msg=success"
            return RedirectResponse(url=url, status_code=303)
        url = "/admin/administradores/inserir?mensagem=Erro ao cadastrar administrador.&tipo_msg=danger"
        return RedirectResponse(url=url, status_code=303)
    return RedirectResponse(url="/admin/administradores?mensagem=Usuário não encontrado.&tipo_msg=danger", status_code=303)

@router.post("/admin/administradores/excluir/{id}")
async def post_administradores_excluir(id: int):
    if adm_repo.delete(id):
        url = "/admin/administradores?mensagem=Administrador excluído com sucesso!&tipo_msg=success"
        return RedirectResponse(url=url, status_code=303)
    url = "/admin/administradores?mensagem=Algo deu errado na exclusão.&tipo_msg=danger"
    return RedirectResponse(url=url, status_code=303)