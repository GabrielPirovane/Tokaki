import sqlite3
from typing import List, Optional
from data.cidade.cidade_sql import *
from data.cidade.cidade_model import Cidade
from data.uf.uf_model import Uf
from data.util import get_connection

class CidadeRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_CIDADE)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, cidade: Cidade) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_CIDADE, (cidade.nome, cidade.id_uf.id))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir cidade: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[Cidade]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CIDADE_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Cidade(id=row['id'], nome=row['nome'], id_uf=Uf(id=row['id_uf'], nome=row['nome_uf'])) 
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Cidade]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_CIDADE, (limit, offset))
            rows = cursor.fetchall()
            return [Cidade(id=row['id'], nome=row['nome'], id_uf=Uf(id=row['id_uf'], nome=row['nome_uf'])) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[Cidade]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_CIDADE, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [Cidade(id=row['id'], nome=row['nome'], id_uf=Uf(id=row['id_uf'], nome=row['nome_uf'])) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_CIDADE)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Cidade]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CIDADE)
            rows = cursor.fetchall()
            return [Cidade(id=row['id'], nome=row['nome'], id_uf=Uf(id=row['id_uf'], nome=row['nome_uf'])) for row in rows]
    
    def update(self, cidade: Cidade) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_CIDADE, (cidade.nome, cidade.id_uf.id, cidade.id))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir cidade: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_CIDADE, (id,))
            return cursor.rowcount > 0

