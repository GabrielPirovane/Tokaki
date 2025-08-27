from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from data.usuario import usuario_repo

router = APIRouter(prefix="/conversas")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_conversas_usuario(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/usuario/conversas.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/detalhes", response_class=HTMLResponse)
async def get_detalhes_conversa_usuario(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/usuario/detalhes_conversa.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response