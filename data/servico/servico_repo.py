import sqlite3
from typing import List, Optional
from data.servico.servico_model import Servico
from data.servico.servico_sql import *
from data.util import get_connection

class ServicoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_CREATE_TABLE_SERVICO)
    
    def insert(self, servico: Servico) -> Optional[int]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_INSERT_SERVICO, (servico.nome,))
            return cursor.lastrowid
        
    def get_by_id(self, id: int) -> Optional[Servico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_SERVICO_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Servico(id=row['id'], nome=row['nome'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Servico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_SERVICO, (limit, offset))
            rows = cursor.fetchall()
            return [Servico(id=row['id'], nome=row['nome']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Servico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_SERVICO, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Servico(id=row['id'], nome=row['nome']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_SERVICO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Servico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_SERVICO)
            rows = cursor.fetchall()
            return [Servico(id=row['id'], nome=row['nome']) for row in rows]
    
    def update(self, servico: Servico) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_SERVICO, (servico.nome,))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_SERVICO, (id,))
            return cursor.rowcount > 0

