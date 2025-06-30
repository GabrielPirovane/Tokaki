from dataclasses import dataclass
from data.musico.musico_model import Musico
from data.servico.servico_model import Servico

@dataclass
class OfertaServico:
    id_servico: Servico
    id_musico: Musico
