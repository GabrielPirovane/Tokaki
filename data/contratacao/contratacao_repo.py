import sqlite3
from typing import List, Optional
from data.agenda.agenda_model import Agenda
from data.agendamento.agendamento_model import Agendamento
from data.contratacao.contratacao_sql import *
from data.contratante.contratante_model import Contratante
from data.musico.musico_model import Musico
from data.usuario.usuario_model import Usuario
from data.contratacao.contratacao_model import Contratacao
from data.util import get_connection

class ContratacaoRepo:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self.create_table()
    
    def create_table(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_CONTRATACAO)
                return True
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def insert(self, contratacao: Contratacao) -> Optional[int]:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_CONTRATACAO, (
                    contratacao.id_agendamento.id,
                    contratacao.data_hora,
                    contratacao.valor,
                    contratacao.status_pagamento,
                    contratacao.nota,
                    contratacao.comentario,
                    contratacao.autor
                ))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir contratacao: {e}")
            return None

    def get_by_id(self, id: int) -> Optional[Contratacao]:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row  # Para acessar por nome de coluna
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CONTRATACAO_BY_ID, (id,))
            row = cursor.fetchone()
            if row:
                agendamento = Agendamento(
                    id=row['agendamento_id'],
                    id_musico=Musico(
                        id=Usuario(
                            id=row['id_musico'],
                            nome=None, nome_usuario=None, senha=None, email=None, cpf=None, telefone=None, genero=None,
                            logradouro=None, numero=None, bairro=None, complemento=None, cep=None, id_cidade=None
                        ),
                        experiencia=None
                    ),
                    id_contratante=Contratante(
                        id=Usuario(
                            id=row['id_contratante'],
                            nome=None, nome_usuario=None, senha=None, email=None, cpf=None, telefone=None, genero=None,
                            logradouro=None, numero=None, bairro=None, complemento=None, cep=None, id_cidade=None
                        ),
                        nota=None,
                        numero_contratacoes=None
                    ),
                    id_agenda=Agenda(
                        id=row['id_agenda'],
                        data_hora=None,
                        disponivel=None
                    ),
                    tipo_servico=row['tipo_servico'],
                    descricao=row['descricao'],
                    valor=row['agendamento_valor'],
                    data_hora=row['agendamento_data_hora'],
                    taxa_aprovacao=row['taxa_aprovacao'],
                    aprovado=row['aprovado']
                )
                return Contratacao(
                    id=row['id'],
                    id_agendamento=agendamento,
                    data_hora=row['data_hora'],
                    valor=row['valor'],
                    status_pagamento=row['status_pagamento'],
                    nota=row['nota'],
                    comentario=row['comentario'],
                    autor=row['autor']
                )
            return None

    def get_all_paged(self, page_number: int=1, page_size: int=10) -> List[Contratacao]:
        limit = page_size
        offset = (page_number - 1) * page_size
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_CONTRATACAO, (limit, offset))
            rows = cursor.fetchall()
            return [self._monta_contratacao(row) for row in rows]

    def search_paged(self, termo: str, page_number: int=1, page_size: int=10) -> List[Contratacao]:
        limit = page_size
        offset = (page_number - 1) * page_size
        termo = f"%{termo}%"
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_RANGE_BUSCA_CONTRATACAO, (termo, limit, offset))
            rows = cursor.fetchall()
            return [self._monta_contratacao(row) for row in rows]

    def count(self) -> int:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_COUNT_CONTRATACAO)
            return cursor.fetchone()[0]

    def get_all(self) -> List[Contratacao]:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(SQL_SELECT_CONTRATACAO)
            rows = cursor.fetchall()
            return [self._monta_contratacao(row) for row in rows]

    def update(self, contratacao: Contratacao) -> bool:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_CONTRATACAO, (
                    contratacao.id_agendamento.id,
                    contratacao.data_hora,
                    contratacao.valor,
                    contratacao.status_pagamento,
                    contratacao.nota,
                    contratacao.comentario,
                    contratacao.autor,
                    contratacao.id
                ))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao atualizar contratacao: {e}")
            return False

    def delete(self, id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(SQL_DELETE_CONTRATACAO, (id,))
            return cursor.rowcount > 0

    def _monta_contratacao(self, row) -> Contratacao:
        agendamento = Agendamento(
            id=row['agendamento_id'],
            id_musico=Musico(
                id=Usuario(
                    id=row['id_musico'],
                    nome=None, nome_usuario=None, senha=None, email=None, cpf=None, telefone=None, genero=None,
                    logradouro=None, numero=None, bairro=None, complemento=None, cep=None, id_cidade=None
                ),
                experiencia=None
            ),
            id_contratante=Contratante(
                id=Usuario(
                    id=row['id_contratante'],
                    nome=None, nome_usuario=None, senha=None, email=None, cpf=None, telefone=None, genero=None,
                    logradouro=None, numero=None, bairro=None, complemento=None, cep=None, id_cidade=None
                ),
                nota=None,
                numero_contratacoes=None
            ),
            id_agenda=Agenda(
                id=row['id_agenda'],
                data_hora=None,
                disponivel=None
            ),
            tipo_servico=row['tipo_servico'],
            descricao=row['descricao'],
            valor=row['agendamento_valor'],
            data_hora=row['agendamento_data_hora'],
            taxa_aprovacao=row['taxa_aprovacao'],
            aprovado=row['aprovado']
        )
        return Contratacao(
            id=row['id'],
            id_agendamento=agendamento,
            data_hora=row['data_hora'],
            valor=row['valor'],
            status_pagamento=row['status_pagamento'],
            nota=row['nota'],
            comentario=row['comentario'],
            autor=row['autor']
        )

