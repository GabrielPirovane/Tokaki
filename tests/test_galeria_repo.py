import sys
import os
from data.galeria.galeria_repo import *

#Arrange
#act
#Assert

#TODO
class TestGaleriaRepo:
    def test_create_table_galeria(self, test_db):
        repo = GaleriaRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar None"

    def test_insert_galeria(self, test_db):
        # Arrange
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste = Galeria(0, "Test Galeria", "descricao teste")
        # Act
        id_galeria_inserida = repo.insert(galeria_teste)
        # Assert
        galeria_db = repo.get_by_id(id_galeria_inserida)
        assert galeria_db is not None, "galeria não deveria ser None após inserção"
        assert galeria_db.id == 1, "ID da galeria inserida deveria ser igual a 1"
        assert galeria_db.nome == "Test Galeria", "Nome da galeria inserida deveria ser 'Test Galeria'"
        assert galeria_db.descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"
    
    def test_get_by_id(self, test_db):
        # Arrange
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste = Galeria(0, "Test Galeria", "descricao teste")
        id_galeria_inserida = repo.insert(galeria_teste)
        # Act
        galeria_db = repo.get_by_id(id_galeria_inserida)
        # Assert
        assert galeria_db is not None, "galeria não deveria ser None ao buscar por ID"
        assert galeria_db.id == id_galeria_inserida, "ID da galeria buscada deveria ser igual ao ID inserido"
        assert galeria_db.nome == "Test Galeria", "Nome da galeria buscada deveria ser 'Test Galeria'"
        assert galeria_db.descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"
        
    def test_get_all_paged(self, test_db):
        # Arrange
        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste1 = Galeria(0, "Test Galeria 1", "descricao teste")
        galeria_teste2 = Galeria(0, "Test Galeria 2", "descricao teste")
        repo.insert(galeria_teste1)
        repo.insert(galeria_teste2)
        # Act
        galeria = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(galeria) == 2, "Deveria retornar duas Galerias"
        assert galeria[0].nome == "Test Galeria 1", "Primeira Galeria deveria ser 'Test Galeria 1'"
        assert galeria[0].descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"
        assert galeria[1].nome == "Test Galeria 2", "Segunda Galeria deveria ser 'Test Galeria 2'"
        assert galeria[1].descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"

    def test_search_paged(self, test_db):
        # Arrange
        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste1 = Galeria(0, "Test Galeria 1", "descricao teste")
        galeria_teste2 = Galeria(0, "Test Galeria 2", "descricao teste")
        repo.insert(galeria_teste1)
        repo.insert(galeria_teste2)
        # Act
        galeria = repo.search_paged(termo="Test", page_number=1, page_size=10)
        # Assert
        assert len(galeria) == 2, "Deveria retornar duas Galerias"
        assert galeria[0].nome == "Test Galeria 1", "Primeira Galeria deveria ser 'Test Galeria 1'"
        assert galeria[0].descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"
        assert galeria[1].nome == "Test Galeria 2", "Segunda Galeria deveria ser 'Test Galeria 2'"
        assert galeria[1].descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"

    def test_count_galeria(self, test_db):
        # Arrange
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste1 =  Galeria(0, "Test Galeria", "descricao teste")
        repo.insert(galeria_teste1)
        # Act
        count = repo.count()
        # Assert
        assert count == 1, "Contagem de galeria deveria ser igual a 1"
    
    def test_get_all_galeria(self, test_db):
        # Arrange
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste1 = Galeria(0, "Test Galeria 1", "descricao teste")
        galeria_teste2 = Galeria(0, "Test Galeria 2", "descricao teste")
        repo.insert(galeria_teste1)
        repo.insert(galeria_teste2)
        # Act
        galeria = repo.get_all()
        # Assert
        assert len(galeria) == 2, "Deveria retornar duas galeria"
        assert galeria[0].nome == "Test Galeria 1", "Primeira galeria deveria ser 'Test Galeria 1'"
        assert galeria[0].descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"
        assert galeria[1].nome == "Test Galeria 2", "Segunda galeria deveria ser 'Test Galeria 2'"
        assert galeria[1].descricao == "descricao teste", "Descrição da galeria buscada deveria ser 'descricao teste'"
        

    def test_update_galeria(self, test_db):
        # Arrange
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste = Galeria(0, "Test Galeria", "descricao teste")
        id_galeria_inserida = repo.insert(galeria_teste)
        galeria_inserida = repo.get_by_id(id_galeria_inserida)
        # Act
        galeria_inserida.nome = "Updated Galeria"
        resultado = repo.update(galeria_inserida)
        # Assert
        assert resultado == True, "Atualização da UF deveria retornar True"
        galeria_db = repo.get_by_id(id_galeria_inserida)
        assert galeria_db.nome == "Updated Galeria", "Nome da galeria atualizada deveria ser 'Updated Galeria"
    
    def test_delete_galeria(self, test_db):
        # Arrange
        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria_teste = Galeria(0, "Test Galeria", "descricao teste")
        id_galeria_inserida = repo.insert(galeria_teste)
        # Act
        resultado = repo.delete(id_galeria_inserida)
        # Assert
        assert resultado == True, "Deleção da galeria deveria retornar True"
        galeria_db = repo.get_by_id(id_galeria_inserida)
        assert galeria_db is None, "galeria deveria ser None após deleção"