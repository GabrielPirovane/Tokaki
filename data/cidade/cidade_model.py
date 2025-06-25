from dataclasses import dataclass
from data.uf.uf_model import Uf

@dataclass
class Cidade:
    id: int
    nome: str
    id_uf: Uf