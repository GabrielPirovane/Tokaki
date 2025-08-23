from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/perfil", response_class=HTMLResponse)
async def get_perfil_usuario(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/usuario/perfil.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/perfil/alterar-dados", response_class=HTMLResponse)
async def get_alterar_dados_usuario(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/usuario/alterar_dados.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response
    
@router.get("/perfil/alterar-senha", response_class=HTMLResponse)
async def get_alterar_senha_usuario(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/usuario/alterar_senha.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/perfil/encerrar-conta", response_class=HTMLResponse)
async def get_encerrar_conta_usuario(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/usuario/encerrar_conta.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/sair", response_class=HTMLResponse)    
def get_sair(request: Request):
    request.session.clear()
    response = RedirectResponse("/login", 303)
    return response