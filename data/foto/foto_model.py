from dataclasses import dataclass
from data.galeria.galeria_model import Galeria

@dataclass
class Foto:
    id: int
    id_galeria: Galeria
    url: str
    descricao: str
