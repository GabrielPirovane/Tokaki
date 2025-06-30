import sqlite3
from typing import List, Optional
from data.contratante.contratante_model import Contratante
from data.contratante.contratante_sql import *
from data.usuario.usuario_model import Usuario
from data.util import get_connection

class ContratanteRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_CREATE_TABLE_CONTRATANTE)
    
    def insert(self, contratante: Contratante) -> Optional[int]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_INSERT_CONTRATANTE, (contratante.id.id, contratante.nota, contratante.numero_contratacoes))
            return cursor.lastrowid
        
    def get_by_id(self, id: int) -> Optional[Contratante]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CONTRATANTE_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Contratante(id=Usuario(id=row['id'], ), nota=row['nota'], numero_contratacoes=row['numero_contratacoes'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Contratante]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_CONTRATANTE, (limit, offset))
            rows = cursor.fetchall()
            return [Contratante(id=Usuario(id=row['id'], ), nota=row['nota'], numero_contratacoes=row['numero_contratacoes']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Contratante]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_CONTRATANTE, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Contratante(id=Usuario(id=row['id'], ), nota=row['nota'], numero_contratacoes=row['numero_contratacoes']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_CONTRATANTE)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Contratante]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CONTRATANTE)
            rows = cursor.fetchall()
            return [Contratante(id=Usuario(id=row['id'], ), nota=row['nota'], numero_contratacoes=row['numero_contratacoes']) for row in rows]
    
    def update(self, contratante: Contratante) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_CONTRATANTE, (contratante.id.id, contratante.nota, contratante.numero_contratacoes))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_CONTRATANTE, (id,))
            return cursor.rowcount > 0

