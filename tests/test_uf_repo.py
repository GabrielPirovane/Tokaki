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
        assert resultado == True, "A criação da tabela deveria retornar None"
    
    def test_get_by_id(self, test_db):
        # Arrange
        repo = UfRepo(test_db)
        repo.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo.insert(uf_teste)
        # Act
        uf_db = repo.get_by_id(id_uf_inserida)
        # Assert
        assert uf_db is not None, "UF não deveria ser None ao buscar por ID"
        assert uf_db.id == id_uf_inserida, "ID da UF buscada deveria ser igual ao ID inserido"
        assert uf_db.nome == "Test UF", "Nome da UF buscada deveria ser 'Test UF'"

    def test_count_uf(self, test_db):
        # Arrange
        repo = UfRepo(test_db)
        repo.create_table()
        uf_teste1 = Uf(0, "Test UF")
        repo.insert(uf_teste1)
        # Act
        count = repo.count()
        # Assert
        assert count == 1, "Contagem de UFs deveria ser igual a 1"
    
    def test_get_all_uf(self, test_db):
        # Arrange
        repo = UfRepo(test_db)
        repo.create_table()
        uf_teste1 = Uf(0, "Test UF 1")
        uf_teste2 = Uf(0, "Test UF 2")
        repo.insert(uf_teste1)
        repo.insert(uf_teste2)
        # Act
        ufs = repo.get_all()
        # Assert
        assert len(ufs) == 2, "Deveria retornar duas UFs"
        assert ufs[0].nome == "Test UF 1", "Primeira UF deveria ser 'Test UF 1'"
        assert ufs[1].nome == "Test UF 2", "Segunda UF deveria ser 'Test UF 2'"
        
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

    def test_update_uf(self, test_db):
        # Arrange
        repo = UfRepo(test_db)
        repo.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo.insert(uf_teste)
        uf_inserida = repo.get_by_id(id_uf_inserida)
        # Act
        uf_inserida.nome = "Updated UF"
        resultado = repo.update(uf_inserida)
        # Assert
        assert resultado == True, "Atualização da UF deveria retornar True"
        uf_db = repo.get_by_id(id_uf_inserida)
        assert uf_db.nome == "Updated UF", "Nome da UF atualizada deveria ser 'Updated UF'"
    
    def test_delete_uf(self, test_db):
        # Arrange
        repo = UfRepo(test_db)
        repo.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo.insert(uf_teste)
        # Act
        resultado = repo.delete(id_uf_inserida)
        # Assert
        assert resultado == True, "Deleção da UF deveria retornar True"
        uf_db = repo.get_by_id(id_uf_inserida)
        assert uf_db is None, "UF deveria ser None após deleção"