from dataclasses import dataclass
from data.musico.musico_model import Musico
from data.categoria.categoria_model import Categoria

@dataclass
class CategoriaMusico:
    id_Categoria: Categoria
    id_Musico: Musico
