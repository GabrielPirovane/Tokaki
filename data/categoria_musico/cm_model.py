from dataclasses import dataclass
from data.musico.musico_model import Musico
from data.categoria.categoria_model import Categoria

@dataclass
class CategoriaMusico:
    id_categoria: Categoria
    id_musico: Musico
