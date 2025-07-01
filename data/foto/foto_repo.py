import sqlite3
from typing import List, Optional
from data.foto.foto_model import Foto
from data.galeria.galeria_model import Galeria
from data.foto.foto_sql import *
from data.util import get_connection

class FotoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_FOTO)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, foto: Foto) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_FOTO, (foto.id_galeria.id, foto.url, foto.descricao))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir foto: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[Foto]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_FOTO_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return Foto(
                    id=row['id'],
                    id_galeria=Galeria(id=row['id_galeria'], nome=row['nome_galeria']),
                    url=row['url'],
                    descricao=row['descricao']
                )
            return None
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_FOTO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Foto]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_FOTO)
            rows = cursor.fetchall()
            return [
                Foto(
                    id=row['id'],
                    id_galeria=Galeria(id=row['id_galeria'], nome=row['nome_galeria']),
                    url=row['url'],
                    descricao=row['descricao']
                )
                for row in rows
            ]
    
    def update(self, foto: Foto) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_FOTO, (foto.id_galeria.id, foto.url, foto.descricao, foto.id))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_FOTO, (id,))
            return cursor.rowcount > 0

