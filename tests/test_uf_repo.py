import sys
import os
from data.uf.uf_repo import *

#Arrange
#act
#Assert

class TestUfRepo:
    def test_create_table_uf(self, test_db):
        repo = UfRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"
    
    def test_insert_uf(self, test_db):
        # Arrange
        repo = UfRepo(test_db)
        repo.create_table()
        uf_teste = Uf(0, "Test UF")
        # Act
        id_uf_inserida = repo.insert(uf_teste)
        # Assert
        uf_db = repo.get_by_id(id_uf_inserida)
        assert uf_db is not None, "UF não deveria ser None após inserção"
        assert uf_db.id == 1, "ID da UF inserida deveria ser igual a 1"
        assert uf_db.nome == "Test UF", "Nome da UF inserida deveria ser 'Test UF'"
