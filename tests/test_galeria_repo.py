import sys
import os
from data.galeria.galeria_repo import *
from data.musico.musico_repo import *
from data.usuario.usuario_repo import *
from data.cidade.cidade_repo import *
from data.uf.uf_repo import *

class TestGaleriaRepo:
    def test_create_table_galeria(self, test_db):
        repo = GaleriaRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_insert_galeria(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria = Galeria(id=None, id_musico=musico, nome="Galeria Teste", descricao="Descrição teste")
        id_galeria = repo.insert(galeria)
        assert id_galeria is not None, "ID da galeria inserida não deveria ser None"
        assert galeria.id_musico.id == musico.id, "ID do músico na galeria inserida deveria ser igual ao ID do músico"

    def test_get_by_id(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria = Galeria(id=None, id_musico=musico, nome="Galeria Teste", descricao="Descrição teste")
        id_galeria = repo.insert(galeria)
        # Act
        galeria_db = repo.get_by_id(id_galeria)
        # Assert
        assert galeria_db is not None, "Galeria não deveria ser None ao buscar por ID"
        assert galeria.id_musico.id == musico.id, "ID do músico na galeria inserida deveria ser igual ao ID do músico"
        assert galeria_db.nome == "Galeria Teste"
        assert galeria_db.descricao == "Descrição teste"
        assert galeria_db.id_musico.id.nome == "Nome Musico"

    def test_get_all_paged(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria1 = Galeria(id=None, id_musico=musico, nome="Galeria 1", descricao="Descrição 1")
        galeria2 = Galeria(id=None, id_musico=musico, nome="Galeria 2", descricao="Descrição 2")
        repo.insert(galeria1)
        repo.insert(galeria2)
        # Act
        galerias = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(galerias) == 2, "Deveria retornar duas galerias"
        assert galerias[0].nome == "Galeria 1"
        assert galerias[1].nome == "Galeria 2"

    def test_search_paged(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria1 = Galeria(id=None, id_musico=musico, nome="Galeria 1", descricao="Descrição 1")
        galeria2 = Galeria(id=None, id_musico=musico, nome="Outra Galeria", descricao="Descrição 2")
        repo.insert(galeria1)
        repo.insert(galeria2)
        # Act
        galerias = repo.search_paged(termo="Galeria", page_number=1, page_size=10)
        # Assert
        assert len(galerias) == 2, "Deveria retornar duas galerias com 'Galeria' no nome"

    def test_count(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria1 = Galeria(id=None, id_musico=musico, nome="Galeria 1", descricao="Descrição 1")
        galeria2 = Galeria(id=None, id_musico=musico, nome="Galeria 2", descricao="Descrição 2")
        repo.insert(galeria1)
        repo.insert(galeria2)
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de galerias deveria ser igual a 2"

    def test_get_all(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria1 = Galeria(id=None, id_musico=musico, nome="Galeria 1", descricao="Descrição 1")
        galeria2 = Galeria(id=None, id_musico=musico, nome="Galeria 2", descricao="Descrição 2")
        repo.insert(galeria1)
        repo.insert(galeria2)
        # Act
        galerias = repo.get_all()
        # Assert
        assert len(galerias) == 2, "Deveria retornar duas galerias"
        assert galerias[0].nome == "Galeria 1"
        assert galerias[1].nome == "Galeria 2"

    def test_update_galeria(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria = Galeria(id=None, id_musico=musico, nome="Galeria Teste", descricao="Descrição teste")
        id_galeria = repo.insert(galeria)
        galeria.nome = "Galeria Atualizada"
        galeria.descricao = "Descrição atualizada"
        galeria.id = id_galeria
        resultado = repo.update(galeria)
        assert resultado == True, "Atualização da galeria deveria retornar True"
        galeria_db = repo.get_by_id(id_galeria)
        assert galeria_db.nome == "Galeria Atualizada"
        assert galeria_db.descricao == "Descrição atualizada"

    def test_delete_galeria(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425")
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        repo_musico.insert(musico)

        repo = GaleriaRepo(test_db)
        repo.create_table()
        galeria = Galeria(id=None, id_musico=musico, nome="Galeria Teste", descricao="Descrição teste")
        id_galeria = repo.insert(galeria)
        resultado = repo.delete(id_galeria)
        assert resultado == True, "Deleção da galeria deveria retornar True"
        galeria_db = repo.get_by_id(id_galeria)
        assert galeria_db is None, "Galeria não deveria existir após deleção"