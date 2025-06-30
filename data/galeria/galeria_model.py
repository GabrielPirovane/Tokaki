from dataclasses import dataclass
from data.musico.musico_model import Musico

@dataclass
class Galeria:
    id: int
    id_musico: Musico
    nome: str
    descricao: str
