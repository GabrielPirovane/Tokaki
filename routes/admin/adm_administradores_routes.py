from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status
from fastapi import Query
from fastapi.requests import Request
from fastapi import Form
from fastapi.templating import Jinja2Templates
from data.adm.adm_repo import AdmRepo
from data.adm.adm_model import Administrador
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import UsuarioRepo
from data.util import get_connection

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

adm_repo = AdmRepo(db_path="dados.db")
usuario_repo = UsuarioRepo(db_path="dados.db")


def confirmar_usuario(nome_completo: str, email: str):
    nome_completo = nome_completo.strip()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id
            FROM usuario
            WHERE (TRIM(nome) || ' ' || TRIM(sobrenome)) = ?
              AND email = ?
        """,
            (nome_completo, email),
        )
        row = cursor.fetchone()
        if row:
            return row["id"]
        return None
    return None


@router.get("/")
async def get_administradores():
    response = templates.TemplateResponse("admin/area_adm.html", {"request": {}})
    return response


@router.get("/administradores")
async def get_administradores(
    request: Request, mensagem: str | None = Query(None), tipo_msg: str = Query("info")
):
    administradores = adm_repo.get_all()
    response = templates.TemplateResponse(
        "admin/administradores.html",
        {
            "request": request,
            "administradores": administradores,
            "mensagem": mensagem,
            "tipo_msg": tipo_msg,
        },
    )
    return response


@router.get("/administradores/inserir")
async def get_administradores_inserir():
    response = templates.TemplateResponse("/admin/inserir_adm.html", {"request": {}})
    return response


@router.post("/administradores/inserir")
async def post_administradores_inserir(
    request: Request, nome: str = Form(...), email: str = Form(...)
):
    adm_id = confirmar_usuario(nome, email)
    if adm_id is not None:
        # Verifica se já é administrador
        existing_adm = adm_repo.get_by_id(adm_id)
        if existing_adm:
            url = "/admin/administradores?mensagem=Usuário já é administrador.&tipo_msg=warning"
            return RedirectResponse(url=url, status_code=303)

        # Inserir novo administrador
        adm = Administrador(id=adm_id)
        id_inserido = adm_repo.insert(adm)

        usuario_adm = usuario_repo.get_by_id(adm_id)
        if usuario_adm is None:
            url = "/admin/administradores?mensagem=Usuário não encontrado.&tipo_msg=danger"
            return RedirectResponse(url=url, status_code=303)

        update_usuario = usuario_repo.update(Usuario(
            id=adm_id,
            id_cidade=usuario_adm.id_cidade if usuario_adm.id_cidade else None,
            nome=usuario_adm.nome,
            sobrenome=usuario_adm.sobrenome,
            nome_usuario=usuario_adm.nome_usuario,
            senha=usuario_adm.senha,
            email=usuario_adm.email,
            cpf=usuario_adm.cpf if usuario_adm.cpf else None,
            telefone=usuario_adm.telefone if usuario_adm.telefone else None,
            genero=usuario_adm.genero if usuario_adm.genero else None,
            logradouro=usuario_adm.logradouro if usuario_adm.logradouro else None,
            numero=usuario_adm.numero if usuario_adm.numero else None,
            bairro=usuario_adm.bairro if usuario_adm.bairro else None,
            complemento=usuario_adm.complemento if usuario_adm.complemento else None,
            cep=usuario_adm.cep if usuario_adm.cep else None,
            data_nascimento=usuario_adm.data_nascimento if usuario_adm.data_nascimento else None,
            verificado=usuario_adm.verificado if usuario_adm.verificado else None,
            tipo_usuario="administrador",
        ))

        if id_inserido is not None and update_usuario:
            url = "/admin/administradores?mensagem=Administrador cadastrado com sucesso!&type_msg=success"
        else:
            url = "/admin/administradores/inserir?mensagem=Erro ao cadastrar administrador.&tipo_msg=danger"
        return RedirectResponse(url=url, status_code=303)


@router.post("/administradores/excluir/{id}")
async def post_administradores_excluir(id: int):
    if adm_repo.delete(id):
        url = "/admin/administradores?mensagem=Administrador excluído com sucesso!&tipo_msg=success"
        return RedirectResponse(url=url, status_code=303)
    url = "/admin/administradores?mensagem=Algo deu errado na exclusão.&tipo_msg=danger"
    return RedirectResponse(url=url, status_code=303)
