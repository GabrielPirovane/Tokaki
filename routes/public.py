from fastapi import APIRouter
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_root():
    response = templates.TemplateResponse("home.html", {"request": {}})
    return response

@router.get("/cadastro")
async def get_cadastro():
    response = templates.TemplateResponse("cadastro.html", {"request": {}})
    return response