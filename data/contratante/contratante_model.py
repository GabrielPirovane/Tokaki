from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Contratante:
    id: Usuario
    nota: float
    numero_contratacoes: int
