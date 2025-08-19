from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from routes.public import router as public_router
from routes.admin.adm_administradores_routes import router as adm_administradores_router
from routes.admin.adm_categorias_routes import router as adm_categorias_router
from routes.admin.adm_fotos import router as adm_fotos_router
from routes.usuario.usuario_perfil import router as usuario_perfil_router
from routes.usuario.usuario_conversas import router as usuario_conversas_router


from data.agenda import agenda_repo
from data.agendamento import agendamento_repo
from data.categoria import categoria_repo
from data.categoria_musico import cm_repo
from data.contratacao import contratacao_repo
from data.contratante import contratante_repo
from data.foto import foto_repo
from data.galeria import galeria_repo
from data.oferta_servico import os_repo
from data.servico import servico_repo
from data.uf import uf_repo
from data.cidade import cidade_repo
from data.usuario import usuario_repo
from data.adm import adm_repo
from data.musico import musico_repo

uf_repo_instance = uf_repo.UfRepo("dados.db")
uf_repo_instance.create_table()

cidade_repo_instance = cidade_repo.CidadeRepo("dados.db")
cidade_repo_instance.create_table()

usuario_repo_instance = usuario_repo.UsuarioRepo("dados.db")
usuario_repo_instance.create_table()

adm_repo_instance = adm_repo.AdmRepo("dados.db")
adm_repo_instance.create_table()

categoria_repo_instance = categoria_repo.CategoriaRepo("dados.db")
categoria_repo_instance.create_table()

categoria_musico_repo_instance = cm_repo.CategoriaMusicoRepo("dados.db")
categoria_musico_repo_instance.create_table()

musico_repo_instance = musico_repo.MusicoRepo("dados.db")
musico_repo_instance.create_table()

galeria_repo_instance = galeria_repo.GaleriaRepo("dados.db")
galeria_repo_instance.create_table()

foto_repo_instance = foto_repo.FotoRepo("dados.db")
foto_repo_instance.create_table()

servico_repo_instance = servico_repo.ServicoRepo("dados.db")
servico_repo_instance.create_table()

oferta_servico_repo_instance = os_repo.OfertaServicoRepo("dados.db")
oferta_servico_repo_instance.create_table()

contratante_repo_instance = contratante_repo.ContratanteRepo("dados.db")
contratante_repo_instance.create_table()

agenda_repo_instance = agenda_repo.AgendaRepo("dados.db")
agenda_repo_instance.create_table()

agendamento_repo_instance = agendamento_repo.AgendamentoRepo("dados.db")
agendamento_repo_instance.create_table()

contratacao_repo_instance = contratacao_repo.ContratacaoRepo("dados.db")
contratacao_repo_instance.create_table()


#Teste em localhost
import secrets
secret_key = secrets.token_hex(32)
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(public_router)
app.include_router(adm_administradores_router)
app.include_router(adm_categorias_router)
app.include_router(adm_fotos_router)
app.include_router(usuario_perfil_router)
app.include_router(usuario_conversas_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="192.168.3.252", port=8000, reload=True)