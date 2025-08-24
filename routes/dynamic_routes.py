# routes/dynamic_routes.py
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo
from data.musico import musico_repo

from routes.usuario.usuario_perfil import router as usuario_router
from routes.usuario.usuario_conversas import router as usuario_conversas_router
from routes.usuario.usuario_contratacao import router as usuario_contratacao_router
from routes.musico.musico_agenda import router as musico_agenda_router
from routes.musico.musico_galeria import router as musico_galeria_router
from routes.musico.musico_contratacoes import router as musico_contratacoes_router
from routes.musico.musico_categorias import router as musico_categorias_router

from routes.contratante.contratante_contratacoes import router as contratante_contratacoes_router
from routes.contratante.contratante_pagamento import router as contratante_pagamento_router

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="/{nome_usuario}")
router.include_router(usuario_router, tags=["usuario"])
router.include_router(usuario_conversas_router, tags=["usuario"])
router.include_router(usuario_contratacao_router, tags=["usuario"])

def get_current_usuario(request: Request, nome_usuario: str):
    sessao_usuario = request.session.get("usuario")
    if not sessao_usuario or sessao_usuario.get("nome_usuario") != nome_usuario:
        raise HTTPException(status_code=403, detail="Não autorizado")
    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_nome_usuario(nome_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home_usuario(request: Request, usuario = Depends(get_current_usuario)):
    """
    Rendeiriza a home correta diretamente em /{nome_usuario}/
    - se tipo == "musico" -> renderiza /musico/home_musico.html
    - se tipo == "contratante" -> renderiza /usuario/home_usuario.html
    """
    if usuario.tipo_usuario == "musico":
        return templates.TemplateResponse(
            "/musico/home_musico.html",
            {"request": request, "usuario": usuario, "nome_usuario": usuario.nome_usuario}
        )

    # contratante / usuário comum
    return templates.TemplateResponse(
        "/usuario/home_usuario.html",
        {"request": request, "usuario": usuario, "nome_usuario": usuario.nome_usuario}
    )


def include_dynamic_routes(app):
    """
    Incluir no main.py:
        include_dynamic_routes(app)

    Observação importante:
    - Os sub-roteadores importados aqui NÃO devem ter prefixo próprio.
    - Aqui nós os montamos com prefix "/{nome_usuario}" para que todas as rotas fiquem sob /nome_usuario/...
    """

    app.include_router(router)
    app.include_router(musico_categorias_router, prefix="/{nome_usuario}", tags=["musico"])
    app.include_router(musico_agenda_router, prefix="/{nome_usuario}", tags=["musico"])
    app.include_router(musico_galeria_router, prefix="/{nome_usuario}", tags=["musico"])
    app.include_router(musico_contratacoes_router, prefix="/{nome_usuario}", tags=["musico"])
    app.include_router(contratante_contratacoes_router, prefix="/{nome_usuario}", tags=["contratante"])
    app.include_router(contratante_pagamento_router, prefix="/{nome_usuario}", tags=["contratante"])
    
