import sqlite3
from typing import List, Optional
from data.oferta_servico.os_sql import *
from data.musico.musico_model import Musico
from data.usuario.usuario_model import Usuario
from data.cidade.cidade_model import Cidade
from data.uf.uf_model import Uf
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
                cursor.execute(SQL_INSERT_OFERTA_SERVICO, (os.id_servico.id, os.id_musico.id.id))
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
                return self._monta_oferta_servico(row)
            return None
        
    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[OfertaServico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_OFERTA_SERVICO, (limit, offset))
            rows = cursor.fetchall()
            return [self._monta_oferta_servico(row) for row in rows]
        
    def search_paged(self, termo: str, page_number: int=1, page_size: int=10) -> List[OfertaServico]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_OFERTA_SERVICO, (termo, limit, offset))
            rows = cursor.fetchall()
            return [self._monta_oferta_servico(row) for row in rows]
        
    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_OFERTA_SERVICO)
            return cursor.fetchone()[0]
        
    def get_all(self) -> List[OfertaServico]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_OFERTA_SERVICO)
            rows = cursor.fetchall()
            return [self._monta_oferta_servico(row) for row in rows]
    
    def update(self, os: OfertaServico, id_servico_antigo: int) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_OFERTA_SERVICO, (os.id_servico.id, os.id_musico.id.id, id_servico_antigo))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao atualizar os: {e}")
            return None
    
    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_OFERTA_SERVICO, (id,))
            return cursor.rowcount > 0

    def _monta_oferta_servico(self, row) -> OfertaServico:
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
            cep=row['cep'],
            data_nascimento=row['data_nascimento']  # Adicionado campo data_nascimento
        )
        musico = Musico(id=usuario, experiencia=row['experiencia'])
        servico = Servico(
            id=row['id_servico'],
            nome=row['nome_servico']
        )
        return OfertaServico(id_servico=servico, id_musico=musico)

