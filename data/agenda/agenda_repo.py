import sqlite3
from typing import List, Optional
from data.agenda.agenda_model import Agenda
from data.agenda.agenda_sql import *
from data.musico.musico_model import Musico
from data.usuario.usuario_model import Usuario
from data.util import get_connection

class AgendaRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_AGENDA)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, agenda: Agenda) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_AGENDA, (agenda.id.id, agenda.data_hora, agenda.disponivel))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir agenda: {e}")
            return None
            
    def get_by_id(self, id: int) -> Optional[Agenda]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_AGENDA_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Agenda(id=Musico(id=row['id']), data_hora=row['data_hora'], disponivel=row['disponivel'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Agenda]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_AGENDA, (limit, offset))
            rows = cursor.fetchall()
            return [Agenda(id=Musico(id=row['id']), data_hora=row['data_hora'], disponivel=row['disponivel']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Agenda]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_AGENDA, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Agenda(id=Musico(id=row['id']), data_hora=row['data_hora'], disponivel=row['disponivel']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_AGENDA)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Agenda]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_AGENDA)
            rows = cursor.fetchall()
            return [Agenda(id=Musico(id=row['id']), data_hora=row['data_hora'], disponivel=row['disponivel']) for row in rows]
    
    def update(self, agenda: Agenda) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_AGENDA, (agenda.id.id, agenda.data_hora, agenda.disponivel))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir agenda: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_AGENDA, (id,))
            return cursor.rowcount > 0

