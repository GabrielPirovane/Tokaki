from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data.categoria import categoria_repo
from data.categoria_musico import cm_repo
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


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

uf_repo_instance = uf_repo.UfRepo("dados.db")
uf_repo_instance.create_table()

cidade_repo_instance = cidade_repo.CidadeRepo("dados.db")
cidade_repo_instance.create_table()

usuario_repo_instance = usuario_repo.UsuarioRepo("dados.db")
usuario_repo_instance.create_table()

adm_repo_instance = adm_repo.admRepo("dados.db")
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

@app.get("/")
async def get_root():
    response = templates.TemplateResponse("index.html", {"request": {}})
    return response


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)