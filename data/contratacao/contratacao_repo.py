import sqlite3
from typing import List, Optional
from data.agenda.agenda_model import Agenda
from data.agendamento.agendamento_model import Agendamento
from data.contratacao.contratacao_sql import *
from data.contratante.contratante_model import Contratante
from data.musico.musico_model import Musico
from data.contratacao.contratacao_model import Contratacao

from data.util import get_connection

class ContratacaoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_CREATE_TABLE_CONTRATACAO)
    
    def insert(self, contratacao: Contratacao) -> Optional[int]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_INSERT_CONTRATACAO, (contratacao.id_agendamento.id,
                                                       contratacao.data_hora,
                                                       contratacao.valor,
                                                       contratacao.status_pagamento,
                                                       contratacao.nota,
                                                       contratacao.comentario,
                                                       contratacao.autor))
            return cursor.lastrowid
        
    def get_by_id(self, id: int) -> Optional[Contratacao]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CONTRATACAO_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Contratacao(id=row['id'],
                                   id_agendamento=Agendamento(id=row['id_agendamento']),
                                   data_hora=row['data_hora'],
                                   valor=row['valor'],
                                   status_pagamento=row['status_pagamento'],
                                   nota=row['nota'],
                                   comentario=row['comentario'],
                                   autor=row['autor'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Contratacao]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_CONTRATACAO, (limit, offset))
            rows = cursor.fetchall()
            return [Contratacao(id=row['id'],
                                   id_agendamento=Agendamento(id=row['id_agendamento']),
                                   data_hora=row['data_hora'],
                                   valor=row['valor'],
                                   status_pagamento=row['status_pagamento'],
                                   nota=row['nota'],
                                   comentario=row['comentario'],
                                   autor=row['autor']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Contratacao]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_CONTRATACAO, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Contratacao(id=row['id'],
                                   id_agendamento=Agendamento(id=row['id_agendamento']),
                                   data_hora=row['data_hora'],
                                   valor=row['valor'],
                                   status_pagamento=row['status_pagamento'],
                                   nota=row['nota'],
                                   comentario=row['comentario'],
                                   autor=row['autor']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_CONTRATACAO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CONTRATACAO)
            rows = cursor.fetchall()
            return [Contratacao(id=row['id'],
                                   id_agendamento=Agendamento(id=row['id_agendamento']),
                                   data_hora=row['data_hora'],
                                   valor=row['valor'],
                                   status_pagamento=row['status_pagamento'],
                                   nota=row['nota'],
                                   comentario=row['comentario'],
                                   autor=row['autor']) for row in rows]
    
    def update(self, contratacao: Contratacao) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_CONTRATACAO, (contratacao.id_agendamento.id,
                                                       contratacao.data_hora,
                                                       contratacao.valor,
                                                       contratacao.status_pagamento,
                                                       contratacao.nota,
                                                       contratacao.comentario,
                                                       contratacao.autor))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_CONTRATACAO, (id,))
            return cursor.rowcount > 0

