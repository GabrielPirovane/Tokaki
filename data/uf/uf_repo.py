import sqlite3
from typing import List, Optional
from data.uf.uf_sql import *
from data.uf.uf_model import Uf
from data.util import get_connection

class UfRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_UF)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, uf: Uf) -> Optional[int]:
        try: 
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_UF, (uf.nome,))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir UF: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[Uf]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_UF_BY_ID, (id,))
            row = cursor.fetchone()
            if row:
                return Uf(id=row['id'], nome=row['nome'])
            return None
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_UF)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Uf]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_UF)
            rows = cursor.fetchall()
            return [Uf(id=row['id'], nome=row['nome']) for row in rows]
    
    def update(self, uf: Uf) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_UF, (uf.nome, uf.id))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao atualizar UF: {e}")
            return None
        
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_UF, (id,))
            return cursor.rowcount > 0
            
    