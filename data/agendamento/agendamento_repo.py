import sqlite3
from typing import List, Optional
from data.agenda.agenda_model import Agenda
from data.agendamento.agendamento_sql import *
from data.contratante.contratante_model import Contratante
from data.musico.musico_model import Musico
from data.agendamento.agendamento_model import Agendamento

from data.util import get_connection

class AgendamentoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_CREATE_TABLE_AGENDAMENTO)
    
    def insert(self, agendamento: Agendamento) -> Optional[int]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_INSERT_AGENDAMENTO, (agendamento.id_musico.id, agendamento.id_contratante.id, agendamento.id_agenda.id, agendamento.tipo_servico, agendamento.descricao, agendamento.valor, agendamento.data_hora, agendamento.taxa_aprovacao, agendamento.aprovado))
            return cursor.lastrowid
        
    def get_by_id(self, id: int) -> Optional[Agendamento]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_AGENDAMENTO_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Agendamento(id=row['id'],
                                   id_musico=Musico(id=row['id_musico']),
                                   id_contratante=Contratante(id=row['id_contratante']),
                                   id_agenda=Agenda(id=row['id_agenda']),
                                   tipo_servico=row['tipo_servico'],
                                   descricao=row['descricao'],
                                   valor=row['valor'],
                                   data_hora=row['data_hora'],
                                   taxa_aprovacao=row['taxa_aprovacao'],
                                   aprovado=row['aprovado'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Agendamento]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_AGENDAMENTO, (limit, offset))
            rows = cursor.fetchall()
            return [Agendamento(id=row['id'],
                                   id_musico=Musico(id=row['id_musico']),
                                   id_contratante=Contratante(id=row['id_contratante']),
                                   id_agenda=Agenda(id=row['id_agenda']),
                                   tipo_servico=row['tipo_servico'],
                                   descricao=row['descricao'],
                                   valor=row['valor'],
                                   data_hora=row['data_hora'],
                                   taxa_aprovacao=row['taxa_aprovacao'],
                                   aprovado=row['aprovado']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Agendamento]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_AGENDAMENTO, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Agendamento(id=row['id'],
                                   id_musico=Musico(id=row['id_musico']),
                                   id_contratante=Contratante(id=row['id_contratante']),
                                   id_agenda=Agenda(id=row['id_agenda']),
                                   tipo_servico=row['tipo_servico'],
                                   descricao=row['descricao'],
                                   valor=row['valor'],
                                   data_hora=row['data_hora'],
                                   taxa_aprovacao=row['taxa_aprovacao'],
                                   aprovado=row['aprovado']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_AGENDAMENTO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_AGENDAMENTO)
            rows = cursor.fetchall()
            return [Agendamento(id=row['id'],
                                   id_musico=Musico(id=row['id_musico']),
                                   id_contratante=Contratante(id=row['id_contratante']),
                                   id_agenda=Agenda(id=row['id_agenda']),
                                   tipo_servico=row['tipo_servico'],
                                   descricao=row['descricao'],
                                   valor=row['valor'],
                                   data_hora=row['data_hora'],
                                   taxa_aprovacao=row['taxa_aprovacao'],
                                   aprovado=row['aprovado']) for row in rows]
    
    def update(self, agendamento: Agendamento) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_AGENDAMENTO, (agendamento.id_musico.id, agendamento.id_contratante.id, agendamento.id_agenda.id, agendamento.tipo_servico, agendamento.descricao, agendamento.valor, agendamento.data_hora, agendamento.taxa_aprovacao, agendamento.aprovado))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_AGENDAMENTO, (id,))
            return cursor.rowcount > 0

