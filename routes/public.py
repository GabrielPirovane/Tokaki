from typing import Optional
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from data.cidade import cidade_repo
from data.uf import uf_repo
from data.usuario import usuario_repo
from fastapi import Form
from validate_docbr import CPF
from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, field_validator
from pydantic import ValidationError
from datetime import date
import re
import requests
from io import BytesIO
import bcrypt

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class UserModel(BaseModel):
    data_nascimento: str

    @field_validator('data_nascimento')
    def valida_data(cls, v):
        try:
            dia, mes, ano = map(int, v.split('/'))
            date(ano, mes, dia)
        except Exception:
            raise ValueError("Data inválida")
        return v
    
def validar_email(email: str):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
        return False

def validar_nome_usuario(nome):
    NOMES_USUARIOS_PROIBIDOS = {"admin", "root", "suporte", "usuario", "test"}
    regex = r"^(?![_.])(?!.*[_.]{2})[a-z0-9._]{3,30}(?<![_.])$"

    if not re.match(regex, nome):
        return "O nome de usuário deve ter entre 3 e 20 caracteres, sem espaços ou acentos, e deve conter apenas letras minúsculas, números, ponto e underline."
    
    if nome.lower() in NOMES_USUARIOS_PROIBIDOS:
        return "Este nome de usuário não é permitido."

    return None 

def validar_logradouro_bairro(logradouro: str, bairro: str, cidade: str) -> bool:

    query = f"{logradouro}, {bairro}, {cidade}, Brasil"
    url = "https://nominatim.openstreetmap.org/search"
    headers = {"User-Agent": "MeuApp/1.0"}
    params = {
        "q": query,
        "format": "json",
        "addressdetails": 1, 
        "limit": 5           
    }
    
    try:
        res = requests.get(url, params=params, headers=headers, timeout=5)
        res.raise_for_status()
        data = res.json()
        validados = {
            "logradouro":False,
            "bairro":False
        }

        for item in data:
            addr = item.get("address", {})
            if addr.get("road", "").lower() == logradouro.lower():
                validados["logradouro"] = True
            if addr.get("suburb", "").lower() == bairro.lower():
                validados["bairro"] = True
        return validados
    except Exception as e:
        print("Erro na validação do endereço:", e)
        return None

@router.get("/", response_class=HTMLResponse)
async def get_root():
    response = templates.TemplateResponse("/public/home.html", {"request": {}})
    return response

@router.get("/cadastro")
async def get_cadastro():
    form_data = {
        "nome": "",
        "sobrenome": "",
        "nome_usuario": "",
        "email": "",
        "cpf": "",
        "data_nascimento": "",
        "telefone": "",
        "genero": "",
        "logradouro": "",
        "id_cidade": "",
        "numero": "",
        "bairro": "",
        "complemento": "",
        "cep": ""
    }
    uf = uf_repo.UfRepo("dados.db").get_all()
    response = templates.TemplateResponse("/public/cadastro.html", {"request": {}, "uf":uf, "errors":{}, "form_data": form_data})
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
    cidade: Optional[str] = Form(None),
    numero: Optional[str] = Form(None),
    bairro: Optional[str] = Form(None),
    complemento: Optional[str] = Form(None),
    cep: Optional[str] = Form(None),
    data_nascimento: Optional[str] = Form(None),  
):
    form_data_dict = {
    "nome": nome or "",
    "sobrenome": sobrenome or "",
    "nome_usuario": nome_usuario or "",
    "email": email or "",
    "cpf": cpf or "",
    "data_nascimento": data_nascimento or "",
    "telefone": telefone or "",
    "genero": genero or "",
    "logradouro": logradouro or "",
    "cidade": cidade or "",
    "numero": numero or "",
    "bairro": bairro or "",
    "complemento": complemento or "",
    "cep": cep or ""
}

    usuario = usuario_repo.UsuarioRepo("dados.db")
    cidades = cidade_repo.CidadeRepo("dados.db").get_all()
    usuarios = usuario.get_all()
    errors = dict()
    validador_cpf = CPF()
    validacao_email = validar_email(email=email)
    validacao_nome_usuario = validar_nome_usuario(nome_usuario)
    if data_nascimento != "":
        try:
            user = UserModel(data_nascimento=data_nascimento)
        except ValidationError as e:
            print("DEBUG str(e):", str(e))
            print("DEBUG e.errors():", e.errors())
            errors["data_nascimento"] = (e.errors()[0]['msg']).replace("Value error, ", "")
            return templates.TemplateResponse(
                "/public/cadastro.html",
                {"request": {}, "errors": errors, "form_data":form_data_dict}
            )
    if len(nome) < 2:
        errors["nome"] = "Nome muito curto (Min: 2 caracteres)."
    elif len(sobrenome) < 2:
        errors["sobrenome"] = "Sobrenome muito curto (Min: 2 caracteres)."
    elif len(nome_usuario) < 3:
        errors["nome_usuario"] = "Nome de usuário muito curto (Min: 3 caracteres)."
    for u in usuarios:
        if u['nome_usuario'] == nome_usuario: errors["nome_usuario"] = "Nome de usuário já cadastrado."
        if u['email'] == email: errors["email"] = "Esse email já está cadastrado. Tente logar-se com ele."
        if u['cpf'] == cpf: errors["cpf"] = "Cpf já cadastrado."

    if validacao_nome_usuario:
        errors["nome_usuario"] = validacao_nome_usuario
    elif cpf != "":
        if not validador_cpf.validate(cpf) or len(cpf) < 11:
            errors["cpf"] = "Cpf inválido."
    elif not validacao_email:
        errors["email"] = "Email inválido."
    elif len(data_nascimento) < 10 and data_nascimento != "":
        errors["data_nascimento"] = "Data inválida."

    id_cidade = None
    for c in cidades:
        if c.nome == cidade:
            id_cidade = c.id
            break
    if not id_cidade:
        errors["cidade"] = "Cidade não encontrada."
    validados_dict = validar_logradouro_bairro(logradouro=logradouro, bairro=bairro, cidade=cidade)
    if validados_dict != None:
        errors["logradouro"] = "Rua não encontrada" if not validados_dict["logradouro"] else None
        errors["bairro"] = "Bairro não encontrado" if not validados_dict["bairro"] else None
        
    if errors:
        uf = uf_repo.UfRepo('dados.db').get_all()
        return templates.TemplateResponse(
            "/public/cadastro.html",
            {
                "request": {},
                "errors": errors,
                "uf": uf,
                "form_data": form_data_dict
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