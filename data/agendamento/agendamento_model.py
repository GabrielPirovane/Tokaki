from dataclasses import dataclass
from data.agenda.agenda_model import Agenda
from data.contratante.contratante_model import Contratante
from data.musico.musico_model import Musico

@dataclass
class Agendamento:
    id: int
    id_musico: Musico
    id_contratante: Contratante
    id_agenda: Agenda
    tipo_servico: str
    descricao: str
    valor: float
    data_hora: str
    taxa_aprovacao: float
    aprovado: bool