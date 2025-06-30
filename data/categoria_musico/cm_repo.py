import sqlite3
from typing import List, Optional
from data.categoria.categoria_model import Categoria
from data.categoria_musico.cm_sql import *
from data.musico.musico_model import Musico
from data.categoria_musico.cm_model import CategoriaMusico
from data.util import get_connection

class CategoriaMusicoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_CATEGORIA_MUSICO)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, cm: CategoriaMusico) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_CATEGORIA_MUSICO, (cm.id_categoria.id, cm.id_musico.id))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir cm: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[CategoriaMusico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CATEGORIA_MUSICO_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return CategoriaMusico(id_musico=Musico(id=row['id_musico'], id_categoria=Categoria(id=row['id_categoria'])))
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[CategoriaMusico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_CATEGORIA_MUSICO, (limit, offset))
            rows = cursor.fetchall()
            return [CategoriaMusico(id_musico=Musico(id=row['id_musico'], id_categoria=Categoria(id=row['id_categoria']))) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[CategoriaMusico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_CATEGORIA_MUSICO, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [CategoriaMusico(id_musico=Musico(id=row['id_musico'], id_categoria=Categoria(id=row['id_categoria']))) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_CATEGORIA_MUSICO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CATEGORIA_MUSICO)
            rows = cursor.fetchall()
            return [CategoriaMusico(id_musico=Musico(id=row['id_musico'], id_categoria=Categoria(id=row['id_categoria']))) for row in rows]
    
    def update(self, cm: CategoriaMusico) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_CATEGORIA_MUSICO, (cm.id_categoria.id, cm.id_musico.id))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir cm: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_CATEGORIA_MUSICO, (id,))
            return cursor.rowcount > 0

