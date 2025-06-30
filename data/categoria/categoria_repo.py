import sqlite3
from typing import List, Optional
from data.categoria.categoria_sql import *
from data.categoria.categoria_model import Categoria
from data.util import get_connection

class CategoriaRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_CATEGORIA)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, categoria: Categoria) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_CATEGORIA, (categoria.nome, categoria.descricao))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir categoria: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[Categoria]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CATEGORIA_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Categoria(id=row['id'], nome=row['nome'], descricao=row['descricao']) 
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Categoria]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_CATEGORIA, (limit, offset))
            rows = cursor.fetchall()
            return [Categoria(id=row['id'], nome=row['nome'], descricao=row['descricao']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Categoria]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_CATEGORIA, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Categoria(id=row['id'], nome=row['nome'], descricao=row['descricao']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_CATEGORIA)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Categoria]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CATEGORIA)
            rows = cursor.fetchall()
            return [Categoria(id=row['id'], nome=row['nome'], descricao=row['descricao']) for row in rows]
    
    def update(self, categoria: Categoria) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_CATEGORIA, (categoria.id, categoria.nome, categoria.descricao))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir categoria: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_CATEGORIA, (id,))
            return cursor.rowcount > 0
            
    