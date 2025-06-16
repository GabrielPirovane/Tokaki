import sqlite3
from typing import List, Optional
from data.uf_sql import *
from data.uf_model import Uf

class UfRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()

    def _connect(self):
        connection = sqlite3.connect(self._db_path)
        connection.row_factory = sqlite3.Row
        return connection
    
    def create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_CREATE_TABLE_UF)
    
    def insert(self, uf: Uf) -> Optional[int]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_INSERT_UF, (uf.nome,))
            return cursor.lastrowid
        
    def get_by_id(self, id: int) -> Optional[Uf]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_UF_BY_ID, (id,))
            row = cursor.fetchone()
            if row:
                return Uf(id=row['id'], nome=row['nome'])
            return None
        
    def count(self) -> int:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_UF)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Uf]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_UF)
            rows = cursor.fetchall()
            return [Uf(id=row['id'], nome=row['nome']) for row in rows]
    
    def update(self, uf: Uf) -> bool:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_UF, (uf.nome, uf.id))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_UF, (id,))
            return cursor.rowcount > 0
            
    