import sqlite3
from typing import List, Optional
from data.adm.adm_sql import *
from data.adm.adm_model import Administrador
from data.usuario.usuario_model import Usuario
from data.util import get_connection

class admRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_CREATE_TABLE_ADMINISTRADOR)
    
    def insert(self, adm: Administrador) -> Optional[int]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_INSERT_ADMINISTRADOR, (adm.id,))
        
    def get_by_id(self, id: int) -> Optional[Administrador]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_ADMINISTRADOR_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Administrador(id=row['id'])
            return None

    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_ADMINISTRADOR)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Administrador]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_ADMINISTRADOR)
            rows = cursor.fetchall()
            return [Administrador(id=row['id']) for row in rows]
    
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_ADMINISTRADOR, (id,))
            return cursor.rowcount > 0

