import sqlite3
from typing import List, Optional
from data.cidade.cidade_model import Cidade
from data.musico.musico_sql import *
from data.musico.musico_model import Musico
from data.uf.uf_model import Uf
from data.usuario.usuario_model import Usuario
from data.util import get_connection

class MusicoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_MUSICO)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, musico: Musico) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_MUSICO, (musico.id.id, musico.experiencia))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir musico: {e}")
            return None
        
    def get_by_id(self, id: int) -> Optional[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_MUSICO_BY_ID, (id,))
            row = cursor.fetchone()
            if row:
                cidade = Cidade(
                    id=row['cidade_id'],
                    nome=row['nome_cidade'],
                    id_uf=Uf(id=row['uf_id'], nome=row['nome_uf'])
                )
                usuario = Usuario(
                    id=row['usuario_id'],
                    id_cidade=cidade,
                    nome=row['nome'],
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
                    cep=row['cep'],
                    data_nascimento=row['data_nascimento']  # Adicionado aqui
                )
                return Musico(id=usuario, experiencia=row['experiencia'])
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Musico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_MUSICO, (limit, offset))
            rows = cursor.fetchall()
            musicos = []
            for row in rows:
                cidade = Cidade(
                    id=row['cidade_id'],
                    nome=row['nome_cidade'],
                    id_uf=Uf(id=row['uf_id'], nome=row['nome_uf'])
                )
                usuario = Usuario(
                    id=row['usuario_id'],
                    id_cidade=cidade,
                    nome=row['nome'],
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
                    cep=row['cep'],
                    data_nascimento=row['data_nascimento']  # Adicionado aqui
                )
                musicos.append(Musico(id=usuario, experiencia=row['experiencia']))
            return musicos
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10) -> List[Musico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_MUSICO, (termo, limit, offset))
            rows = cursor.fetchall()
            musicos = []
            for row in rows:
                cidade = Cidade(
                    id=row['cidade_id'],
                    nome=row['nome_cidade'],
                    id_uf=Uf(id=row['uf_id'], nome=row['nome_uf'])
                )
                usuario = Usuario(
                    id=row['usuario_id'],
                    id_cidade=cidade,
                    nome=row['nome'],
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
                    cep=row['cep'],
                    data_nascimento=row['data_nascimento']  # Adicionado aqui
                )
                musicos.append(Musico(id=usuario, experiencia=row['experiencia']))
            return musicos
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_MUSICO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[Musico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_MUSICO)
            rows = cursor.fetchall()
            musicos = []
            for row in rows:
                cidade = Cidade(
                    id=row['cidade_id'],
                    nome=row['nome_cidade'],
                    id_uf=Uf(id=row['uf_id'], nome=row['nome_uf'])
                )
                usuario = Usuario(
                    id=row['usuario_id'],
                    id_cidade=cidade,
                    nome=row['nome'],
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
                    cep=row['cep'],
                    data_nascimento=row['data_nascimento']  # Adicionado aqui
                )
                musicos.append(Musico(id=usuario, experiencia=row['experiencia']))
            return musicos
    
    def update(self, musico: Musico) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_MUSICO, (musico.experiencia, musico.id.id))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao atualizar musico: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_MUSICO, (id,))
            return cursor.rowcount > 0

