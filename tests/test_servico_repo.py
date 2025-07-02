from data.servico.servico_repo import *
class TestServicoRepo:
    def test_create_table_servico(self, test_db):
        repo = ServicoRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar None"

    def test_insert_servico(self, test_db):
        # Arrange
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste = Servico(0, "Test Servico")
        # Act
        id_servico_inserida = repo.insert(servico_teste)
        # Assert
        servico_db = repo.get_by_id(id_servico_inserida)
        assert servico_db is not None, "servico não deveria ser None após inserção"
        assert servico_db.id == 1, "ID da servico inserida deveria ser igual a 1" #Autoincrement
        assert servico_db.nome == "Test Servico", "Nome da servico inserida deveria ser 'Test Servico'"
    
    
    def test_get_by_id(self, test_db):
        # Arrange
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste = Servico(0, "Test Servico")
        id_servico_inserida = repo.insert(servico_teste)
        # Act
        servico_db = repo.get_by_id(id_servico_inserida)
        # Assert
        assert servico_db is not None, "servico não deveria ser None ao buscar por ID"
        assert servico_db.id == id_servico_inserida, "ID da servico buscada deveria ser igual ao ID inserido"
        assert servico_db.nome == "Test Servico", "Nome da servico buscada deveria ser 'Test Servico'"
      
        
    def test_get_all_paged(self, test_db):
        # Arrange
        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste1 = Servico(0, "Test Servico 1")
        servico_teste2 = Servico(0, "Test Servico 2")
        repo.insert(servico_teste1)
        repo.insert(servico_teste2)
        # Act
        servico = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(servico) == 2, "Deveria retornar duas Servicos"
        assert servico[0].nome == "Test Servico 1", "Primeira Servico deveria ser 'Test Servico 1'"
        assert servico[0].id == 1, "ID da primeira Servico deveria ser 1"
        assert servico[1].nome == "Test Servico 2", "Segunda Servico deveria ser 'Test Servico 2'"
        assert servico[1].id == 2, "ID da segunda Servico deveria ser 2"
    

    def test_search_paged(self, test_db):
        # Arrange
        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste1 = Servico(0, "Test Servico 1")
        servico_teste2 = Servico(0, "Test Servico 2")
        repo.insert(servico_teste1)
        repo.insert(servico_teste2)
        # Act
        servico = repo.search_paged(termo="Test", page_number=1, page_size=10)
        # Assert
        assert len(servico) == 2, "Deveria retornar duas Servicos"
        assert servico[1].nome == "Test Servico 2", "Segunda Servico deveria ser 'Test Servico 2'"
   

    def test_count_servico(self, test_db):
        # Arrange
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste1 =  Servico(0, "Test Servico")
        repo.insert(servico_teste1)
        # Act
        count = repo.count()
        # Assert
        assert count == 1, "Contagem de servico deveria ser igual a 1"
    
    def test_get_all_servico(self, test_db):
        # Arrange
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste1 = Servico(0, "Test Servico 1")
        servico_teste2 = Servico(0, "Test Servico 2")
        repo.insert(servico_teste1)
        repo.insert(servico_teste2)
        # Act
        servico = repo.get_all()
        # Assert
        assert len(servico) == 2, "Deveria retornar duas servico"
        assert servico[0].nome == "Test Servico 1", "Primeira servico deveria ser 'Test Servico 1'"
        assert servico[1].nome == "Test Servico 2", "Segunda servico deveria ser 'Test Servico 2'"
        

    def test_update_servico(self, test_db):
        # Arrange
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste = Servico(0, "Test Servico")
        id_servico_inserida = repo.insert(servico_teste)
        servico_inserida = repo.get_by_id(id_servico_inserida)
        # Act
        servico_inserida.nome = "Updated Servico"
        resultado = repo.update(servico_inserida)
        # Assert
        assert resultado == True, "Atualização da UF deveria retornar True"
        servico_db = repo.get_by_id(id_servico_inserida)
        assert servico_db.nome == "Updated Servico", "Nome da servico atualizada deveria ser 'Updated Servico"
    
    def test_delete_servico(self, test_db):
        # Arrange
        repo = ServicoRepo(test_db)
        repo.create_table()
        servico_teste = Servico(0, "Test Servico")
        id_servico_inserida = repo.insert(servico_teste)
        # Act
        resultado = repo.delete(id_servico_inserida)
        # Assert
        assert resultado == True, "Deleção da servico deveria retornar True"
        servico_db = repo.get_by_id(id_servico_inserida)
        assert servico_db is None, "servico deveria ser None após deleção"