from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data import uf_repo


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

uf_repo_instance = uf_repo.UfRepo("dados.db")
uf_repo_instance.create_table()

@app.get("/")
async def get_root():
    response = templates.TemplateResponse("index.html", {"request": {}})
    return response


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)