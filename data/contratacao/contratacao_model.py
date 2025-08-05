from dataclasses import dataclass
from data.agendamento.agendamento_model import Agendamento

@dataclass
class Contratacao:
    id: int
    id_agendamento: Agendamento
    data_hora: str
    valor: float
    status_pagamento: str
    nota: float
    comentario: str
    autor: str