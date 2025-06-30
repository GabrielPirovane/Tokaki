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
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_ADMINISTRADOR)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, adm: Administrador) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_ADMINISTRADOR, (adm.id,))
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir adm: {e}")
            return None
        
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
    
    def update(self, adm: Administrador) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_ADMINISTRADOR, (adm.id.id, adm.nome))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir agenda: {e}")
            return None

    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_ADMINISTRADOR, (id,))
            return cursor.rowcount > 0

