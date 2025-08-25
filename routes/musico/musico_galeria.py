from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from data.usuario import usuario_repo

router = APIRouter(prefix="/galeria")
templates = Jinja2Templates(directory="templates")



@router.get("/", response_class=HTMLResponse)
async def get_galeria_musico(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/galeria.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/detalhes", response_class=HTMLResponse)
async def get_detalhes_galeria_musico(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/detalhes_galeria.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/cadastrar", response_class=HTMLResponse)
async def get_cadastrar_galeria(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/cadastrar_galeria.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/alterar", response_class=HTMLResponse)
async def get_alterar_galeria(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/alterar_galeria.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/excluir", response_class=HTMLResponse)
async def get_excluir_galeria(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/excluir_galeria.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/foto", response_class=HTMLResponse)
async def get_foto_galeria(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/ampliar_foto.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/foto/upload", response_class=HTMLResponse)
async def get_upload_foto(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/cadastrar_foto.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response

@router.get("/foto/alterar", response_class=HTMLResponse)
async def get_alterar_foto(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        return RedirectResponse(url="/login", status_code=303)

    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    response = templates.TemplateResponse(
        "/musico/alterar_foto.html",
        {
            "request": request, 
            "nome_usuario": nome_usuario,
            "usuario": usuario 
        }
    )
    return response


