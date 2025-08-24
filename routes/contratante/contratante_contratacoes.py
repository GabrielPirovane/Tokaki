from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from data.usuario import usuario_repo

router = APIRouter(prefix='/minhas-contratacoes')
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get_contratacoes(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/contratante/minhas_contratacoes.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/solicitacoes", response_class=HTMLResponse)
async def get_solicitacoes_contratacoes(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/contratante/solicitacoes_contratacao.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response


@router.get("/solicitacoes/cancelar", response_class=HTMLResponse)
async def get_cancelar_solicitacoes(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/contratante/cancelar_solicitacao.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/solicitacoes/detalhes", response_class=HTMLResponse)
async def get_detalhes_solicitacoes(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/contratante/detalhes_solicitacao.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

