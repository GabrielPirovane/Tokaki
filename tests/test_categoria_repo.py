import sys
import os
from data.categoria.categoria_repo import *

#Arrange
#act
#Assert

class TestCategoriaRepo:
    def test_create_table_categoria(self, test_db):
        repo = CategoriaRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar None"

    def test_insert_categoria(self, test_db):
        # Arrange
        repo = CategoriaRepo(test_db)
        repo.create_table()
        categoria_teste = Categoria(0, "Test Categoria", "descricao teste")
        # Act
        id_categoria_inserida = repo.insert(categoria_teste)
        # Assert
        categoria_db = repo.get_by_id(id_categoria_inserida)
        assert categoria_db is not None, "categoria não deveria ser None após inserção"
        assert categoria_db.id == 1, "ID da categoria inserida deveria ser igual a 1"
        assert categoria_db.nome == "Test Categoria", "Nome da categoria inserida deveria ser 'Test Categoria'"
    
    def test_get_by_id(self, test_db):
        # Arrange
        repo = CategoriaRepo(test_db)
        repo.create_table()
        categoria_teste = Categoria(0, "Test Categoria", "descricao teste")
        id_categoria_inserida = repo.insert(categoria_teste)
        # Act
        categoria_db = repo.get_by_id(id_categoria_inserida)
        # Assert
        assert categoria_db is not None, "categoria não deveria ser None ao buscar por ID"
        assert categoria_db.id == id_categoria_inserida, "ID da categoria buscada deveria ser igual ao ID inserido"
        assert categoria_db.nome == "Test Categoria", "Nome da categoria buscada deveria ser 'Test Categoria'"

    def test_count_categoria(self, test_db):
        # Arrange
        repo = CategoriaRepo(test_db)
        repo.create_table()
        categoria_teste1 =  Categoria(0, "Test Categoria", "descricao teste")
        repo.insert(categoria_teste1)
        # Act
        count = repo.count()
        # Assert
        assert count == 1, "Contagem de categorias deveria ser igual a 1"
    
    def test_get_all_categoria(self, test_db):
        # Arrange
        repo = CategoriaRepo(test_db)
        repo.create_table()
        categoria_teste1 = Categoria(0, "Test Categoria 1", "descricao teste")
        categoria_teste2 = Categoria(0, "Test Categoria 2", "descricao teste")
        repo.insert(categoria_teste1)
        repo.insert(categoria_teste2)
        # Act
        categorias = repo.get_all()
        # Assert
        assert len(categorias) == 2, "Deveria retornar duas categorias"
        assert categorias[0].nome == "Test Categoria 1", "Primeira categoria deveria ser 'Test Categoria 1'"
        assert categorias[1].nome == "Test Categoria 2", "Segunda categoria deveria ser 'Test Categoria 2'"
        

    def test_update_categoria(self, test_db):
        # Arrange
        repo = CategoriaRepo(test_db)
        repo.create_table()
        categoria_teste = Categoria(0, "Test Categoria", "descricao teste")
        id_categoria_inserida = repo.insert(categoria_teste)
        categoria_inserida = repo.get_by_id(id_categoria_inserida)
        # Act
        categoria_inserida.nome = "Updated categoria"
        resultado = repo.update(categoria_inserida)
        # Assert
        assert resultado == True, "Atualização da categoria deveria retornar True"
        categoria_db = repo.get_by_id(id_categoria_inserida)
        assert categoria_db.nome == "Updated categoria", "Nome da categoria atualizada deveria ser 'Updated categoria'"
    
    def test_delete_categoria(self, test_db):
        # Arrange
        repo = CategoriaRepo(test_db)
        repo.create_table()
        categoria_teste = Categoria(0, "Test Categoria", "descricao teste")
        id_categoria_inserida = repo.insert(categoria_teste)
        # Act
        resultado = repo.delete(id_categoria_inserida)
        # Assert
        assert resultado == True, "Deleção da categoria deveria retornar True"
        categoria_db = repo.get_by_id(id_categoria_inserida)
        assert categoria_db is None, "categoria deveria ser None após deleção"