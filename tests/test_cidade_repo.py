import sys
import os
from data.cidade.cidade_repo import *
from data.uf.uf_repo import *

class TestCidadeRepo:
    def test_create_table_cidade(self, test_db):
        repo = CidadeRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"
    
    def test_insert_cidade(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        # Act
        id_cidade_inserida = repo.insert(cidade_teste)
        # Assert
        assert id_cidade_inserida is not None, "ID da Cidade inserida não deveria ser None"

    def test_get_by_id(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo.insert(cidade_teste)
        # Act
        cidade_db = repo.get_by_id(id_cidade_inserida)
        # Assert
        assert cidade_db is not None, "Cidade não deveria ser None ao buscar por ID"
        assert cidade_db.id == id_cidade_inserida, "ID da Cidade buscada deveria ser igual ao ID inserido"
        assert cidade_db.nome == "Test Cidade", "Nome da Cidade buscada deveria ser 'Test Cidade'"
    
    def test_get_all_paged(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste1 = Cidade(0, "Test Cidade 1", Uf(id_uf_inserida, "Test UF"))
        cidade_teste2 = Cidade(0, "Test Cidade 2", Uf(id_uf_inserida, "Test UF"))
        repo.insert(cidade_teste1)
        repo.insert(cidade_teste2)
        # Act
        cidades = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(cidades) == 2, "Deveria retornar duas Cidades"
        assert cidades[0].nome == "Test Cidade 1", "Primeira Cidade deveria ser 'Test Cidade 1'"
        assert cidades[1].nome == "Test Cidade 2", "Segunda Cidade deveria ser 'Test Cidade 2'"

    def test_search_paged(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste1 = Cidade(0, "Test Cidade 1", Uf(id_uf_inserida, "Test UF"))
        cidade_teste2 = Cidade(0, "Test Cidade 2", Uf(id_uf_inserida, "Test UF"))
        repo.insert(cidade_teste1)
        repo.insert(cidade_teste2)
        # Act
        cidades = repo.search_paged(termo="Test", page_number=1, page_size=10)
        # Assert
        assert len(cidades) == 2, "Deveria retornar duas Cidades ao buscar por 'Test'"
        assert cidades[0].nome == "Test Cidade 1", "Primeira Cidade deveria ser 'Test Cidade 1'"
        assert cidades[1].nome == "Test Cidade 2", "Segunda Cidade deveria ser 'Test Cidade 2'"

    def test_count(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste1 = Cidade(0, "Test Cidade 1", Uf(id_uf_inserida, "Test UF"))
        cidade_teste2 = Cidade(0, "Test Cidade 2", Uf(id_uf_inserida, "Test UF"))
        repo.insert(cidade_teste1)
        repo.insert(cidade_teste2)
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de Cidades deveria ser igual a 2"

    def test_get_all(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste1 = Cidade(0, "Test Cidade 1", Uf(id_uf_inserida, "Test UF"))
        cidade_teste2 = Cidade(0, "Test Cidade 2", Uf(id_uf_inserida, "Test UF"))
        repo.insert(cidade_teste1)
        repo.insert(cidade_teste2)
        # Act
        cidades = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(cidades) == 2, "Deveria retornar duas Cidades"
        assert cidades[0].nome == "Test Cidade 1", "Primeira Cidade deveria ser 'Test Cidade 1'"
        assert cidades[1].nome == "Test Cidade 2", "Segunda Cidade deveria ser 'Test Cidade 2'"

    def test_update_cidade(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo.insert(cidade_teste)
        cidade_inserida = repo.get_by_id(id_cidade_inserida)
        # Act
        cidade_inserida.nome = "Updated Cidade"
        repo.insert(cidade_inserida)
        # Assert
        cidade_atualizada = repo.get_by_id(id_cidade_inserida)
        assert cidade_atualizada.nome == "Updated Cidade", "Nome da Cidade atualizada deveria ser 'Updated Cidade'"