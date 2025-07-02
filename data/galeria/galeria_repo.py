import sqlite3
from typing import List, Optional
from data.galeria.galeria_model import Galeria
from data.galeria.galeria_sql import *
from data.musico.musico_model import Musico
from data.usuario.usuario_model import Usuario
from data.cidade.cidade_model import Cidade
from data.uf.uf_model import Uf
from data.util import get_connection

class GaleriaRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_GALERIA)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, galeria: Galeria) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_GALERIA, (galeria.id_musico.id.id, galeria.nome, galeria.descricao))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir galeria: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[Galeria]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_GALERIA_BY_ID, (id,))
            row = cursor.fetchone() 
            if row:
                musico = self._monta_musico(row)
                return Galeria(id=row['id'], id_musico=musico, nome=row['nome'], descricao=row['descricao'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Galeria]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_GALERIA, (limit, offset))
            rows = cursor.fetchall()
            return [Galeria(id=row['id'], id_musico=self._monta_musico(row), nome=row['nome'], descricao=row['descricao']) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10) -> List[Galeria]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_GALERIA, (termo, limit, offset))
            rows = cursor.fetchall()
            return [Galeria(id=row['id'], id_musico=self._monta_musico(row), nome=row['nome'], descricao=row['descricao']) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_GALERIA)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Galeria]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_GALERIA)
            rows = cursor.fetchall()
            return [Galeria(id=row['id'], id_musico=self._monta_musico(row), nome=row['nome'], descricao=row['descricao']) for row in rows]
    
    def update(self, galeria: Galeria) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_UPDATE_GALERIA, (galeria.id_musico.id.id, galeria.nome, galeria.descricao, galeria.id))
            return cursor.rowcount > 0
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_GALERIA, (id,))
            return cursor.rowcount > 0

    def _monta_musico(self, row) -> Musico:
        cidade = Cidade(
            id=row['cidade_id'],
            nome=row['nome_cidade'],
            id_uf=Uf(id=row['uf_id'], nome=row['nome_uf'])
        )
        usuario = Usuario(
            id=row['usuario_id'],
            id_cidade=cidade,
            nome=row['usuario_nome'],
            nome_usuario=row['nome_usuario'],
            senha=row['senha'],
            email=row['email'],
            cpf=row['cpf'],
            telefone=row['telefone'],
            genero=row['genero'],
            logradouro=row['logradouro'],
            numero=row['numero'],
            bairro=row['bairro'],
            complemento=row['complemento'],
            cep=row['cep']
        )
        return Musico(id=usuario, experiencia=row['experiencia'])

