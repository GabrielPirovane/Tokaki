from data.uf.uf_repo import *
from data.cidade.cidade_repo import *
from data.cidade.cidade_model import Cidade
from data.uf.uf_model import Uf

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
        id_cidade = repo.insert(cidade_teste)
        # Assert
        cidade_db = repo.get_by_id(id_cidade)
        assert cidade_db is not None, "Cidade não deveria ser None ao inserir"
        assert cidade_db.id == id_cidade, "ID da cidade buscada deveria ser igual ao ID inserido"
        assert cidade_db.nome == "Test Cidade", "Nome da cidade buscada deveria ser 'Test Cidade'"
        assert cidade_db.id_uf.id == id_uf_inserida, "ID da UF da cidade deveria ser igual ao inserido"
  
    
    def test_get_by_id(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade = repo.insert(cidade_teste)
        
        # Act
        cidade_db = repo.get_by_id(id_cidade)
        # Assert
        assert cidade_db is not None, "Cidade não deveria ser None ao buscar por ID"
        assert cidade_db.id == id_cidade, "ID da cidade buscada deveria ser igual ao ID inserido"
        assert cidade_db.nome == "Test Cidade", "Nome da cidade buscada deveria ser 'Test Cidade'"
        assert cidade_db.id_uf.id == id_uf_inserida, "ID da UF da cidade deveria ser igual ao inserido"

    def test_count_cidade(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade1 = Cidade(0, "Cidade 1", Uf(id_uf, "Test UF"))
        cidade2 = Cidade(0, "Cidade 2", Uf(id_uf, "Test UF"))
        repo.insert(cidade1)
        repo.insert(cidade2)
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de cidades deveria ser igual a 2"
    
    def test_get_all_cidade(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserido = repo_uf.insert(uf_teste)

        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade1 = Cidade(0, "Cidade 1", Uf(id_uf_inserido, "Test UF"))
        cidade2 = Cidade(0, "Cidade 2", Uf(id_uf_inserido, "Test UF"))
        id_cidade1 = repo.insert(cidade1)
        id_cidade2 = repo.insert(cidade2)
        # Act
        cidades = repo.get_all()
        # Assert
        assert len(cidades) == 2, "Deveria retornar duas cidades"
        assert cidades[0].nome == cidade1.nome, "Primeira cidade deveria ser 'Cidade 1'"
        assert cidades[0].id == id_cidade1, "ID da primeira cidade deveria ser igual ao ID inserido"
        assert cidades[0].id_uf.id == cidade1.id_uf.id, "ID da UF da primeira cidade deveria ser igual ao inserido"
        assert cidades[1].nome ==  cidade2.nome, "Segunda cidade deveria ser 'Cidade 2'"
        assert cidades[1].id == id_cidade2, "ID da segunda cidade deveria ser igual ao ID inserido"
        assert cidades[1].id_uf.id == cidade2.id_uf.id, "ID da UF da segunda cidade deveria ser igual ao inserido"
        
    
    def test_update_cidade(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade = Cidade(0, "Cidade Antiga", Uf(id_uf, "Test UF"))
        id_cidade = repo.insert(cidade)
        cidade_db = repo.get_by_id(id_cidade)
        # Act
        cidade_db.nome = "Cidade Atualizada"
        resultado = repo.update(cidade_db)
        cidade_atualizada = repo.get_by_id(id_cidade)
        # Assert
        assert resultado == True, "Atualização da cidade deveria retornar True"
        assert cidade_atualizada.nome == "Cidade Atualizada", "Nome da cidade atualizada deveria ser 'Cidade Atualizada'"
    
    def test_delete_cidade(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo = CidadeRepo(test_db)
        repo.create_table()
        cidade = Cidade(0, "Cidade Para Deletar", Uf(id_uf, "Test UF"))
        id_cidade = repo.insert(cidade)
        # Act
        resultado = repo.delete(id_cidade)
        # Assert
        assert resultado == True, "Deleção da cidade deveria retornar True"
        cidade_db = repo.get_by_id(id_cidade)
        assert cidade_db is None, "Cidade deveria ser None após deleção"