import sqlite3
from typing import List, Optional
from data.oferta_servico.os_sql import *
from data.musico.musico_model import Musico
from data.oferta_servico.os_model import OfertaServico
from data.servico.servico_model import Servico

from data.util import get_connection

class OfertaServicoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_OFERTA_SERVICO)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
        
    def insert(self, os: OfertaServico) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_OFERTA_SERVICO, (os.id_musico.id, os.id_musico.id))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir os: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[OfertaServico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_OFERTA_SERVICO_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                return OfertaServico(id_servico=Servico(id=row['id_servico']), id_musico=Musico(id=row['id_musico']))
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[OfertaServico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_OFERTA_SERVICO, (limit, offset))
            rows = cursor.fetchall()
            return [OfertaServico(id_servico=Servico(id=row['id_servico']), id_musico=Musico(id=row['id_musico'])) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10, ) -> List[OfertaServico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_OFERTA_SERVICO, (f'%{termo}%', limit, offset))
            rows = cursor.fetchall()
            return [OfertaServico(id_servico=Servico(id=row['id_servico']), id_musico=Musico(id=row['id_musico'])) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_OFERTA_SERVICO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_OFERTA_SERVICO)
            rows = cursor.fetchall()
            return [OfertaServico(id_servico=Servico(id=row['id_servico']), id_musico=Musico(id=row['id_musico'])) for row in rows]
    
    def update(self, os: OfertaServico) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_OFERTA_SERVICO, (os.id_musico.id, os.id_musico.id))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir os: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_OFERTA_SERVICO, (id,))
            return cursor.rowcount > 0

