from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Contratante:
    id: Usuario
    nota: float | None
    numero_contratacoes: int | None
