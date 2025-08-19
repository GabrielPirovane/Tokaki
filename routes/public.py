from typing import Optional
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from data.cidade import cidade_repo
from data.contratante import contratante_repo
from data.contratante.contratante_model import Contratante
from data.musico import musico_repo
from data.musico.musico_model import Musico
from data.uf import uf_repo
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from fastapi import Form
from validate_docbr import CPF
from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, field_validator
from pydantic import ValidationError
from datetime import date
import re
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
    request: Request,
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
    generos = {
        '1': "Masculino",
        '2': "Feminino",
        '3': "Outro",
        '4': "Prefiro não informar"
    }

    usuario = usuario_repo.UsuarioRepo("dados.db")
    cidades = cidade_repo.CidadeRepo("dados.db").get_all()
    contratante = contratante_repo.ContratanteRepo("dados.db")
    musico = musico_repo.MusicoRepo("dados.db")
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
        if u.nome_usuario == nome_usuario: errors["nome_usuario"] = "Nome de usuário já cadastrado."
        if u.email == email: errors["email"] = "Esse email já está cadastrado. Tente logar-se com ele."
        if u.cpf == cpf: errors["cpf"] = "Cpf já cadastrado."
    if validacao_nome_usuario:
        errors["nome_usuario"] = validacao_nome_usuario
    elif cpf != '':
        if not validador_cpf.validate(cpf) or len(cpf) < 11:
            errors["cpf"] = "Cpf inválido."
        cpf = re.sub(r'[^0-9]', '', cpf) 
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
        
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

    if telefone != '' and cep != '':
        telefone = re.sub(r'[^0-9]', '', telefone)
        cep = re.sub(r'[^0-9]', '', cep)  
    try:
        novo_usuario = Usuario(
            id=0,
            nome=nome,
            sobrenome=sobrenome,
            id_cidade=id_cidade if cidade != '' else None,
            nome_usuario=nome_usuario,
            email=email,
            senha=senha_hash.decode(), 
            genero=None if genero is None or genero == '' else generos[genero],
            telefone=None if telefone == '' else telefone,
            cpf=None if cpf == '' else cpf,
            logradouro=None if logradouro == '' else logradouro,  
            numero=None if numero == '' else numero,
            bairro=None if bairro == '' else bairro,
            complemento=None if complemento == '' else complemento,
            cep=None if cep == '' else cep,
            data_nascimento=None if data_nascimento == '' else data_nascimento,
            verificado=False
        )
        novo_usuario = usuario.insert(novo_usuario)
        if novo_usuario:
            print('tudo certo')
            if tipo_usuario == 'contratante':
                id_contratante = novo_usuario
                novo_contratante = contratante.insert(
                    Contratante(
                        id=id_contratante,
                        nota=None,
                        numero_contratacoes=0
                ))
                if novo_contratante:
                    pass
                else:
                    pass
            elif tipo_usuario == 'musico':
                id_musico = novo_usuario
                novo_musico = musico.insert(
                    Musico(
                        id=id_musico,
                        experiencia=None
                    )
                )
                if novo_musico:
                    pass
                else:
                    pass
        else:
            pass
    except Exception as e:
        pass
        
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

@router.post("/login")
async def post_login(
    request: Request, 
    email: str = Form(...),
    senha: str = Form(...),
):
    senha_hash = usuario_repo.UsuarioRepo("dados.db").get_senha_by_email(email)
    if not senha_hash:
        pass
    if not bcrypt.checkpw(senha.encode(), senha_hash.encode()):
        pass
    usuario = usuario_repo.UsuarioRepo("dados.db").get_by_email(email)
    username = usuario.nome_usuario
    request.session["usuario"] = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "nome_usuario": username
    }
    response = RedirectResponse(f"/{username}", 303)
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