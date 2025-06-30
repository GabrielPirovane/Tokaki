from dataclasses import dataclass
from data.musico.musico_model import Musico

@dataclass
class Agenda:
    id: Musico
    data_hora: str
    disponivel: bool
