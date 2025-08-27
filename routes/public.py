from typing import Optional
from fastapi import APIRouter, Request, Depends
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
from routes.email_util import send_reset_email
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
import os

import re
from io import BytesIO
import bcrypt


SECRET_KEY = os.getenv("SECRET_KEY")
serializer = URLSafeTimedSerializer(SECRET_KEY)
router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_sessao(request: Request) -> Optional[dict]:
    return request.session.get("usuario")


class UserModel(BaseModel):
    data_nascimento: str

    @field_validator("data_nascimento")
    def valida_data(cls, v):
        try:
            dia, mes, ano = map(int, v.split("/"))
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
async def get_root(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
    return templates.TemplateResponse(
        "/public/home.html", {"request": request, "sessao": sessao}
    )


@router.get("/cadastro")
async def get_cadastro(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
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
        "cep": "",
    }
    uf = uf_repo.UfRepo("dados.db").get_all()
    return templates.TemplateResponse(
        "/public/cadastro.html",
        {
            "request": request,
            "uf": uf,
            "errors": {},
            "form_data": form_data,
            "sessao": sessao,
        },
    )


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
        "cep": cep or "",
    }
    generos = {
        "1": "Masculino",
        "2": "Feminino",
        "3": "Outro",
        "4": "Prefiro não informar",
    }

    usuario = usuario_repo.UsuarioRepo("dados.db")
    cidades = cidade_repo.CidadeRepo("dados.db").get_all()
    contratante = contratante_repo.ContratanteRepo("dados.db")
    usuarios = usuario.get_all()
    musico = musico_repo.MusicoRepo("dados.db")
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
            errors["data_nascimento"] = (e.errors()[0]["msg"]).replace(
                "Value error, ", ""
            )
            return templates.TemplateResponse(
                "/public/cadastro.html",
                {"request": {}, "errors": errors, "form_data": form_data_dict},
            )
    if len(nome) < 2:
        errors["nome"] = "Nome muito curto (Min: 2 caracteres)."
    elif len(sobrenome) < 2:
        errors["sobrenome"] = "Sobrenome muito curto (Min: 2 caracteres)."
    elif len(nome_usuario) < 3:
        errors["nome_usuario"] = "Nome de usuário muito curto (Min: 3 caracteres)."
    for u in usuarios:
        if u.nome_usuario == nome_usuario:
            errors["nome_usuario"] = "Nome de usuário já cadastrado."
        if u.email == email:
            errors["email"] = "Esse email já está cadastrado. Tente logar-se com ele."
        if u.cpf == cpf:
            errors["cpf"] = "Cpf já cadastrado."
    if validacao_nome_usuario:
        errors["nome_usuario"] = validacao_nome_usuario
    elif cpf != "":
        cpf = re.sub(r"[^0-9]", "", cpf)
        if not validador_cpf.validate(cpf) or len(cpf) < 11:
            errors["cpf"] = "Cpf inválido."
    elif not validacao_email:
        errors["email"] = "Email inválido."
    elif len(data_nascimento) < 10 and data_nascimento != "":
        errors["data_nascimento"] = "Data inválida."
    elif cidade != "":
        id_cidade = None
        for c in cidades:
            if c.nome == cidade:
                id_cidade = c.id
                break
        if not id_cidade:
            errors["cidade"] = "Cidade não encontrada."

    if errors:
        uf = uf_repo.UfRepo("dados.db").get_all()
        return templates.TemplateResponse(
            "/public/cadastro.html",
            {"request": {}, "errors": errors, "uf": uf, "form_data": form_data_dict},
        )

    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

    if telefone != "" and cep != "":
        telefone = re.sub(r"[^0-9]", "", telefone)
        cep = re.sub(r"[^0-9]", "", cep)
    try:
        novo_usuario = Usuario(
            id=0,
            nome=nome,
            sobrenome=sobrenome,
            id_cidade=id_cidade if cidade != "" else None,
            nome_usuario=nome_usuario,
            email=email,
            senha=senha_hash.decode(),
            genero=None if genero is None or genero == "" else generos[genero],
            telefone=None if telefone == "" else telefone,
            cpf=None if cpf == "" else cpf,
            logradouro=None if logradouro == "" else logradouro,
            numero=None if numero == "" else numero,
            bairro=None if bairro == "" else bairro,
            complemento=None if complemento == "" else complemento,
            cep=None if cep == "" else cep,
            data_nascimento=None if data_nascimento == "" else data_nascimento,
            verificado=False,
            tipo_usuario=tipo_usuario.strip().lower(),
        )
        novo_usuario = usuario.insert(novo_usuario)
        if novo_usuario:
            print("tudo certo")
            if tipo_usuario == "contratante":
                print("durex")
                id_contratante = novo_usuario
                novo_contratante = contratante.insert(
                    Contratante(id=id_contratante, nota=None, numero_contratacoes=0)
                )
                if novo_contratante:
                    pass
                else:
                    pass
            elif tipo_usuario == "musico":
                id_musico = novo_usuario
                try:
                    novo_musico = musico.insert(Musico(id=id_musico, experiencia=None))
                except Exception as e:
                    raise Exception(f"Erro ao inserir músico: {str(e)}")
                if novo_musico:
                    pass
                else:
                    pass
        else:
            pass
    except Exception as e:
        print(e)


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
    repo = usuario_repo.UsuarioRepo("dados.db")

    senha_hash = repo.get_senha_by_email(email)
    if not senha_hash:
        return RedirectResponse("/login?error=invalid", status_code=303)


    if not bcrypt.checkpw(senha.encode(), senha_hash.encode()):
        return RedirectResponse("/login?error=invalid", status_code=303)

    usuario = repo.get_by_email(email)
    if not usuario:
        return RedirectResponse("/login?error=invalid", status_code=303)

    if usuario.tipo_usuario != "administrador": 
        username = usuario.nome_usuario

        # salva sessão (incluindo tipo para acesso rápido)
        request.session["usuario"] = {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "nome_usuario": username,
            "tipo": usuario.tipo_usuario,
        }

        # Sempre redireciona para a home central /{nome_usuario}
        return RedirectResponse(f"/{username}", status_code=303)
    else:
        return RedirectResponse(f"/admin", status_code=303)

@router.get("/verificacao")
async def get_verificacao(
    request: Request, sessao: Optional[dict] = Depends(get_sessao)
):
    return templates.TemplateResponse(
        "/public/verificacao.html", {"request": request, "sessao": sessao}
    )


@router.get("/sobre")
async def get_sobre(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
    return templates.TemplateResponse(
        "/public/sobre.html", {"request": request, "sessao": sessao}
    )


@router.get("/contatos")
async def get_contatos(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
    return templates.TemplateResponse(
        "/public/contatos.html", {"request": request, "sessao": sessao}
    )


@router.get("/catalogo")
async def get_catalogo(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
    return templates.TemplateResponse(
        "/public/catalogo.html", {"request": request, "sessao": sessao}
    )


@router.get("/detalhes")
async def get_detalhes(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
    return templates.TemplateResponse(
        "/public/detalhes_musico.html", {"request": request, "sessao": sessao}
    )


@router.get("/galeria")
async def get_galeria(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
    return templates.TemplateResponse(
        "/public/galeria.html", {"request": request, "sessao": sessao}
    )


@router.get("/foto")
async def get_foto(request: Request, sessao: Optional[dict] = Depends(get_sessao)):
    return templates.TemplateResponse(
        "/public/ampliar_foto.html", {"request": request, "sessao": sessao}
    )

@router.get("/esqueci-senha")
async def get_esqueci_senha(request: Request):
    return templates.TemplateResponse(
        "/public/esqueci_senha.html", {"request": request}
    )

@router.post("/esqueci-senha")
async def post_esqueci_senha(request: Request, email: str = Form(...)):
    repo = usuario_repo.UsuarioRepo("dados.db")
    usuario = repo.get_by_email(email)

    if not usuario:
        return templates.TemplateResponse(
            "/public/esqueci_senha.html",
            {"request": request, "message": "Se este email estiver cadastrado, enviamos instruções para redefinir a senha."},
        )

    token = serializer.dumps(email, salt="reset-senha")
    reset_link = f"http://127.0.0.1:8000/mudar-senha/{token}"

    repo.update_token(email=email, token=token, expiracao=60)

    send_reset_email(to_email=email, reset_link=reset_link)
    return templates.TemplateResponse(
        "/public/esqueci_senha.html",
        {"request": request, "message": "Se este email estiver cadastrado, enviamos instruções para redefinir a senha."},
    )
    
@router.get("/mudar-senha/{token}", response_class=HTMLResponse)
async def get_mudar_senha(request: Request, token: str):
    try:
        email = serializer.loads(token, salt="reset-senha", max_age=3600)
    except SignatureExpired:
        return templates.TemplateResponse(
            "/public/mudar_senha.html",
            {"request": request, "error": "O link expirou, peça um novo email."},
        )
    except BadSignature:
        return templates.TemplateResponse(
            "/public/mudar_senha.html",
            {"request": request, "error": "Link inválido."},
        )


    repo = usuario_repo.UsuarioRepo("dados.db")
    usuario = repo.get_by_email(email)
    if not usuario:
        return templates.TemplateResponse(
            "/public/mudar_senha.html",
            {"request": request, "error": "Usuário não encontrado."},
        )


    return templates.TemplateResponse(
        "/public/mudar_senha.html",
        {"request": request, "email": email, "token": token},
    )

    
@router.post("/mudar-senha/{token}", response_class=HTMLResponse)
async def post_mudar_senha(request: Request, token: str, senha: str = Form(...)):
    try:
        email = serializer.loads(token, salt="reset-senha", max_age=3600)
    except SignatureExpired:
        return templates.TemplateResponse("/public/esqueci_senha.html", {"request": request, "error": "O link expirou."})
    except BadSignature:
        return templates.TemplateResponse("/public/esqueci_senha.html", {"request": request, "error": "Link inválido."})

    repo = usuario_repo.UsuarioRepo("dados.db")
    usuario = repo.get_by_email(email)
    if not usuario:
        return templates.TemplateResponse("/public/mudar_senha.html", {"request": request, "error": "Usuário não encontrado."})

    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    try:
        repo.update_senha(id=usuario.id, nova_senha=senha_hash.decode())
        repo.clear_token(id=usuario.id)
    except Exception:
        return templates.TemplateResponse("/public/mudar_senha.html", {"request": request, "error": "Erro ao atualizar senha."})

    return templates.TemplateResponse("/public/login.html", {"request": request, "success": "Senha atualizada com sucesso!"})
