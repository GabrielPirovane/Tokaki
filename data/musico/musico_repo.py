import sqlite3
from typing import List, Optional
from data.musico.musico_sql import *
from data.musico.musico_model import Musico
from data.usuario.usuario_model import Usuario
from data.util import get_connection

class MusicoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_MUSICO)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, musico: Musico) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_MUSICO, (musico.id.id, musico.experiencia))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir musico: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_MUSICO_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Musico(id=Usuario(id=row['id'], ), experiencia=row['experiencia'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Musico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_MUSICO, (limit, offset))
            rows = cursor.fetchall()
            return [Musico(id=Usuario(id=row['id'], ), experiencia=row['experiencia']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Musico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_MUSICO, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Musico(id=Usuario(id=row['id'], ), experiencia=row['experiencia']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_MUSICO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_MUSICO)
            rows = cursor.fetchall()
            return [Musico(id=Usuario(id=row['id'], ), experiencia=row['experiencia']) for row in rows]
    
    def update(self, musico: Musico) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_MUSICO, (musico.id.id, musico.experiencia))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir musico: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_MUSICO, (id,))
            return cursor.rowcount > 0

