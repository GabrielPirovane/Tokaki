import sqlite3
from typing import List, Optional
from data.uf.uf_model import Uf
from data.usuario.usuario_sql import *
from data.usuario.usuario_model import Usuario
from data.cidade.cidade_model import Cidade
from data.util import get_connection


class UsuarioRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()

    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_USUARIO)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False

    def insert(self, usuario: Usuario) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    SQL_INSERT_USUARIO,
                    (
                        usuario.id_cidade,
                        usuario.nome,
                        usuario.sobrenome,
                        usuario.nome_usuario,
                        usuario.senha,
                        usuario.email,
                        usuario.cpf,
                        usuario.telefone,
                        usuario.genero,
                        usuario.logradouro,
                        usuario.numero,
                        usuario.bairro,
                        usuario.complemento,
                        usuario.cep,
                        usuario.data_nascimento,
                        usuario.verificado,
                    ),
                )
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir usuario: {e}")
            return None

    def get_by_id(self, id: int) -> Optional[Usuario]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_USUARIO_BY_ID, (id,))
            row = cursor.fetchone()
            if row:
                return Usuario(
                    id=row["id"],
                    id_cidade=Cidade(
                        id=row["id_cidade"],
                        nome=row["nome_cidade"],
                        id_uf=Uf(id=row["id_uf"], nome=row["nome_uf"]),
                    ),
                    nome=row["nome"],
                    sobrenome=row["sobrenome"],
                    nome_usuario=row["nome_usuario"],
                    senha=row["senha"],
                    email=row["email"],
                    cpf=row["cpf"],
                    telefone=row["telefone"],
                    genero=row["genero"],
                    logradouro=row["logradouro"],
                    numero=row["numero"],
                    bairro=row["bairro"],
                    complemento=row["complemento"],
                    cep=row["cep"],
                    data_nascimento=row["data_nascimento"],
                )
            return None

    def get_by_email(self, email: str):
        with get_connection() as db:
            cursor = db.cursor()
            cursor.execute(SQL_GET_DADOS_POR_EMAIL, (email,))
            row = cursor.fetchone()
            if row is None:
                return None
            
            uf = Uf(id=row['id_uf'], nome=row['nome_uf']) if row['id_uf'] else None
            cidade = Cidade(id=row['id_cidade'], nome=row['nome_cidade'], id_uf=uf) if row['id_cidade'] else None
            return Usuario(
                id=row["id"],
                id_cidade=cidade,
                nome=row["nome"],
                sobrenome=row["sobrenome"],
                nome_usuario=row["nome_usuario"],
                senha=row["senha"],
                email=row["email"],
                cpf=row["cpf"],
                telefone=row["telefone"],
                genero=row["genero"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                bairro=row["bairro"],
                complemento=row["complemento"],
                cep=row["cep"],
                data_nascimento=row["data_nascimento"],
                verificado=row["verificado"],
            )

    def get_all_paged(self, page_number: int = 1, page_size: int = 10) -> List[Usuario]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_USUARIO, (limit, offset))
            rows = cursor.fetchall()
            return [
                Usuario(
                    id=row["id"],
                    id_cidade=Cidade(
                        id=row["id_cidade"],
                        nome=row["nome_cidade"],
                        id_uf=Uf(id=row["id_uf"], nome=row["nome_uf"]),
                    ),
                    nome=row["nome"],
                    sobrenome=row["sobrenome"],
                    nome_usuario=row["nome_usuario"],
                    senha=row["senha"],
                    email=row["email"],
                    cpf=row["cpf"],
                    telefone=row["telefone"],
                    genero=row["genero"],
                    logradouro=row["logradouro"],
                    numero=row["numero"],
                    bairro=row["bairro"],
                    complemento=row["complemento"],
                    cep=row["cep"],
                    data_nascimento=row["data_nascimento"],
                )
                for row in rows
            ]

    def search_paged_nome(
        self, termo: str, page_number: int = 1, page_size: int = 10
    ) -> List[Usuario]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                SQL_SELECT_RANGE_BUSCA_USUARIO_NOME, (f"%{termo}%", limit, offset)
            )
            rows = cursor.fetchall()
            return [
                Usuario(
                    id=row["id"],
                    id_cidade=Cidade(
                        id=row["id_cidade"],
                        nome=row["nome_cidade"],
                        id_uf=Uf(id=row["id_uf"], nome=row["nome_uf"]),
                    ),
                    nome=row["nome"],
                    sobrenome=row["sobrenome"],
                    nome_usuario=row["nome_usuario"],
                    senha=row["senha"],
                    email=row["email"],
                    cpf=row["cpf"],
                    telefone=row["telefone"],
                    genero=row["genero"],
                    logradouro=row["logradouro"],
                    numero=row["numero"],
                    bairro=row["bairro"],
                    complemento=row["complemento"],
                    cep=row["cep"],
                    data_nascimento=row["data_nascimento"],
                )
                for row in rows
            ]

    def get_by_nome_usuario(self, nome_usuario: str) -> Optional[Usuario]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_USUARIO_BY_NOMEUSUARIO, (nome_usuario,))
            row = cursor.fetchone()
            if row:
                return Usuario(
                    id=row["id"],
                    id_cidade=Cidade(
                        id=row["id_cidade"],
                        nome=row["nome_cidade"],
                        id_uf=Uf(id=row["id_uf"], nome=row["nome_uf"]),
                    ),
                    nome=row["nome"],
                    sobrenome=row["sobrenome"],
                    nome_usuario=row["nome_usuario"],
                    senha=row["senha"],
                    email=row["email"],
                    cpf=row["cpf"],
                    telefone=row["telefone"],
                    genero=row["genero"],
                    logradouro=row["logradouro"],
                    numero=row["numero"],
                    bairro=row["bairro"],
                    complemento=row["complemento"],
                    cep=row["cep"],
                    data_nascimento=row["data_nascimento"],
                    verificado=row["verificado"],
                )
            return None

    def get_senha_by_email(self, email: str) -> Optional[str]:
        with get_connection() as db:
            cursor = db.cursor()
            cursor.execute(SQL_GET_SENHA_POR_EMAIL, (email,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return dados["senha"]

    def search_paged_nomecompleto(
        self, termo: str, page_number: int = 1, page_size: int = 10
    ) -> List[Usuario]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termos = termo.strip().split(maxsplit=1)
        nome_term = f"%{termos[0]}%"
        sobrenome_term = f"%{termos[1]}%" if len(termos) > 1 else "%"

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                SQL_SELECT_RANGE_BUSCA_USUARIO_NOMECOMPLETO,
                (nome_term, sobrenome_term, limit, offset),
            )
            rows = cursor.fetchall()
            return [
                Usuario(
                    id=row["id"],
                    id_cidade=Cidade(
                        id=row["id_cidade"],
                        nome=row["nome_cidade"],
                        id_uf=Uf(id=row["id_uf"], nome=row["nome_uf"]),
                    ),
                    nome=row["nome"],
                    sobrenome=row["sobrenome"],
                    nome_usuario=row["nome_usuario"],
                    senha=row["senha"],
                    email=row["email"],
                    cpf=row["cpf"],
                    telefone=row["telefone"],
                    genero=row["genero"],
                    logradouro=row["logradouro"],
                    numero=row["numero"],
                    bairro=row["bairro"],
                    complemento=row["complemento"],
                    cep=row["cep"],
                    data_nascimento=row["data_nascimento"],
                )
                for row in rows
            ]

    def search_paged_email(
        self, termo: str, page_number: int = 1, page_size: int = 10
    ) -> List[Usuario]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                SQL_SELECT_RANGE_BUSCA_USUARIO_EMAIL, (f"%{termo}%", limit, offset)
            )
            rows = cursor.fetchall()
            return [
                Usuario(
                    id=row["id"],
                    id_cidade=Cidade(
                        id=row["id_cidade"],
                        nome=row["nome_cidade"],
                        id_uf=Uf(id=row["id_uf"], nome=row["nome_uf"]),
                    ),
                    nome=row["nome"],
                    sobrenome=row["sobrenome"],
                    nome_usuario=row["nome_usuario"],
                    senha=row["senha"],
                    email=row["email"],
                    cpf=row["cpf"],
                    telefone=row["telefone"],
                    genero=row["genero"],
                    logradouro=row["logradouro"],
                    numero=row["numero"],
                    bairro=row["bairro"],
                    complemento=row["complemento"],
                    cep=row["cep"],
                    data_nascimento=row["data_nascimento"],
                )
                for row in rows
            ]

    def count(self) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_USUARIO)
            return cursor.fetchone()[0]

    def get_all(self) -> List[Usuario]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_USUARIO)
            rows = cursor.fetchall()
            return [
                Usuario(
                    id=row["id"],
                    id_cidade=Cidade(
                        id=row["id_cidade"],
                        nome=row["nome_cidade"],
                        id_uf=Uf(id=row["id_uf"], nome=row["nome_uf"]),
                    ),
                    nome=row["nome"],
                    sobrenome=row["sobrenome"],
                    nome_usuario=row["nome_usuario"],
                    senha=row["senha"],
                    email=row["email"],
                    cpf=row["cpf"],
                    telefone=row["telefone"],
                    genero=row["genero"],
                    logradouro=row["logradouro"],
                    numero=row["numero"],
                    bairro=row["bairro"],
                    complemento=row["complemento"],
                    cep=row["cep"],
                    data_nascimento=row["data_nascimento"],
                    verificado=row["verificado"],
                )
                for row in rows
            ]

    def update(self, usuario: Usuario) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    SQL_UPDATE_USUARIO,
                    (
                        usuario.id_cidade.id,
                        usuario.nome,
                        usuario.sobrenome,
                        usuario.nome_usuario,
                        usuario.senha,
                        usuario.email,
                        usuario.cpf,
                        usuario.telefone,
                        usuario.genero,
                        usuario.logradouro,
                        usuario.numero,
                        usuario.bairro,
                        usuario.complemento,
                        usuario.cep,
                        usuario.data_nascimento,
                        usuario.id,
                    ),
                )
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao atualizar usuario: {e}")
            return None

    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_USUARIO, (id,))
            return cursor.rowcount > 0
