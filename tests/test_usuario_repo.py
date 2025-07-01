import sys
import os
from data.usuario.usuario_repo import *

class TestUsuarioRepo:
    def test_create_table_usuario(self, test_db):
        repo = UsuarioRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"
