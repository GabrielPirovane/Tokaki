from typing import Optional
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from data.uf import uf_repo
from data.usuario import usuario_repo
from fastapi import Form
from validate_docbr import CPF
from email_validator import validate_email, EmailNotValidError


router = APIRouter()
templates = Jinja2Templates(directory="templates")


def validar_email(email: str):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
        return False


@router.get("/", response_class=HTMLResponse)
async def get_root():
    response = templates.TemplateResponse("/public/home.html", {"request": {}})
    return response

@router.get("/cadastro")
async def get_cadastro():
    uf = uf_repo.UfRepo("dados.db").get_all()
    response = templates.TemplateResponse("/public/cadastro.html", {"request": {}, "uf":uf, "errors":{}})
    return response

@router.post("/cadastro")
async def post_cadastro(
    tipo_usuario: str = Form(...),
    nome: str = Form(...),
    sobrenome: str = Form(...),
    nome_usuario: str = Form(...),
    senha: str = Form(...),
    email: str = Form(...),
    cpf: Optional[str] = Form(None),
    telefone: Optional[str] = Form(None),
    genero: Optional[str] = Form(None),
    logradouro: Optional[str] = Form(None),
    id_cidade: Optional[int] = Form(None),
    numero: Optional[str] = Form(None),
    bairro: Optional[str] = Form(None),
    complemento: Optional[str] = Form(None),
    cep: Optional[str] = Form(None),
    data_nascimento: Optional[str] = Form(None),  
):
    usuario = usuario_repo.UsuarioRepo("dados.db")
    usuarios = usuario.get_all()
    errors = dict()
    validador_cpf = CPF()
    validacao_email = validar_email(email=email)
    

    
    if len(nome) > 100:
        errors["nome"] = "Nome muito grande (Máx: 100 caracteres)."
    elif len(sobrenome) > 100:
        errors["sobrenome"] = "Sobrenome muito grande (Máx: 100 caracteres)."
    elif len(nome_usuario) > 30:
        errors["nome_usuario"] = "Nome de usuário muito grande (Máx: 30 caracteres)."
    elif cpf != "":
        if not validador_cpf.validate(cpf) or len(cpf) < 11:
            errors["cpf"] = "Cpf inválido."
    elif len(email) > 254:
        errors["email"] = "Email muito grande (Máx: 254 caracteres)"
    elif not validacao_email:
        errors["email"] = "Email inválido."
    
    
    for u in usuarios:
        if u['nome_usuario'] == nome_usuario: errors["nome_usuario"] = "Nome de usuário já cadastrado."
        if u['email'] == email: errors["email"] = "Esse email já está cadastrado. Tente logar-se com ele."
        if u['cpf'] == cpf: errors["cpf"] = "Cpf já cadastrado."
        
    
    
        
    if errors:
        uf = uf_repo.UfRepo('dados.db').get_all()
        return templates.TemplateResponse(
            "/public/cadastro.html",
            {
                "request": {},
                "errors": errors,
                "uf": uf,
                "form_data": {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "nome_usuario": nome_usuario,
                    "email": email,
                    "cpf": cpf
                },
            },
        )
    
    

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

@router.get("/esqueci-senha")
async def get_esqueci_senha():
    response = templates.TemplateResponse("/public/esqueci_senha.html", {"request": {}})
    return response