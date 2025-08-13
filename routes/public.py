from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from data.uf import uf_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get_root():
    response = templates.TemplateResponse("/public/home.html", {"request": {}})
    return response

@router.get("/cadastro")
async def get_cadastro():
    uf = uf_repo.UfRepo("dados.db").get_all()
    response = templates.TemplateResponse("/public/cadastro.html", {"request": {}, "uf":uf})
    return response

@router.get("/login")
async def get_login():
    response = templates.TemplateResponse("/public/login.html", {"request": {}})
    return response

@router.get("/verificacao")
async def get_verificacao():
    response = templates.TemplateResponse("/public/verificacao.html", {"request": {}})
    return response

@router.get("/sobre")
async def get_sobre():
    response = templates.TemplateResponse("/public/sobre.html", {"request": {}})
    return response

@router.get("/contatos")
async def get_contatos():
    response = templates.TemplateResponse("/public/contatos.html", {"request": {}})
    return response

@router.get("/catalogo")
async def get_catalogo():
    response = templates.TemplateResponse("/public/catalogo.html", {"request": {}})
    return response

@router.get("/detalhes")
async def get_detalhes():
    response = templates.TemplateResponse("/public/detalhes_musico.html", {"request": {}})
    return response

@router.get("/galeria")
async def get_galeria():
    response = templates.TemplateResponse("/public/galeria.html", {"request": {}})
    return response

@router.get("/foto")
async def get_foto():
    response = templates.TemplateResponse("/public/ampliar_foto.html", {"request": {}})
    return response