from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Musico:
    id: Usuario
    experiencia: str
