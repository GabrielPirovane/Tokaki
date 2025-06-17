import sqlite3
from typing import List, Optional
from data.galeria.galeria_model import Galeria
from data.galeria.galeria_sql import *
from data.musico.musico_model import Musico
from data.util import get_connection

class GaleriaRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_CREATE_TABLE_GALERIA)
    
    def insert(self, galeria: Galeria) -> Optional[int]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_INSERT_GALERIA, (galeria.id_musico.id, galeria.nome, galeria.descricao))
            return cursor.lastrowid
        
    def get_by_id(self, id: int) -> Optional[Galeria]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_GALERIA_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Galeria(id=row['id'], id_musico=Musico(id=row['id_musico'], nome=row['nome_musico']), nome=row['nome'], descricao=row['descricao'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Musico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_GALERIA, (limit, offset))
            rows = cursor.fetchall()
            return [Galeria(id=row['id'], id_musico=Musico(id=row['id_musico'], nome=row['nome_musico']), nome=row['nome'], descricao=row['descricao']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Galeria]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_GALERIA, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Galeria(id=row['id'], id_musico=Musico(id=row['id_musico'], nome=row['nome_musico']), nome=row['nome'], descricao=row['descricao']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_GALERIA)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Galeria]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_GALERIA)
            rows = cursor.fetchall()
            return [Galeria(id=row['id'], id_musico=Musico(id=row['id_musico'], nome=row['nome_musico']), nome=row['nome'], descricao=row['descricao']) for row in rows]
    
    def update(self, galeria: Galeria) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_GALERIA, (galeria.id_musico.id, galeria.nome, galeria.descricao))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_GALERIA, (id,))
            return cursor.rowcount > 0

