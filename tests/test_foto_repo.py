import sys
import os
from data.foto.foto_repo import *
from data.galeria.galeria_repo import *
from data.galeria.galeria_model import Galeria
from data.foto.foto_model import Foto
from data.musico.musico_repo import *
from data.usuario.usuario_repo import *
from data.cidade.cidade_repo import *
from data.uf.uf_repo import UfRepo

class TestFotoRepo:
    def test_create_table_foto(self, test_db):
        repo = FotoRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_insert_foto(self, test_db):
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
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        id_musico = repo_musico.insert(musico)

        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        galeria = Galeria(0, musico, "Galeria Teste", "Descrição da galeria")
        id_galeria = repo_galeria.insert(galeria)
        galeria.id = id_galeria

        repo = FotoRepo(test_db)
        repo.create_table()
        foto = Foto(id=0, id_galeria=galeria, url="http://url.com/foto.jpg", descricao="Foto de teste")
        # Act
        id_foto = repo.insert(foto)
        # Assert
        assert id_foto is not None, "ID da foto inserida não deveria ser None"
        foto_db = repo.get_by_id(id_foto)
        assert foto_db is not None, "Foto não deveria ser None ao buscar por ID"
        assert foto_db.url == "http://url.com/foto.jpg"
        assert foto_db.descricao == "Foto de teste"
        assert foto_db.id_galeria.id == id_galeria
        assert foto_db.id_galeria.nome == "Galeria Teste"

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
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        id_musico = repo_musico.insert(musico)

        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        galeria = Galeria(0, musico, "Galeria Teste", "Descrição da galeria")
        id_galeria = repo_galeria.insert(galeria)
        galeria.id = id_galeria

        repo = FotoRepo(test_db)
        repo.create_table()
        foto = Foto(id=0, id_galeria=galeria, url="http://url.com/foto.jpg", descricao="Foto de teste")
        id_foto = repo.insert(foto)
        # Act
        foto_db = repo.get_by_id(id_foto)
        # Assert
        assert foto_db is not None, "Foto não deveria ser None ao buscar por ID"
        assert foto_db.url == "http://url.com/foto.jpg"
        assert foto_db.descricao == "Foto de teste"
        assert foto_db.id_galeria.id == id_galeria
        assert foto_db.id_galeria.nome == "Galeria Teste"

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
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        id_musico = repo_musico.insert(musico)

        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        galeria = Galeria(0, musico, "Galeria Teste", "Descrição da galeria")
        id_galeria = repo_galeria.insert(galeria)
        galeria.id = id_galeria

        repo = FotoRepo(test_db)
        repo.create_table()
        foto1 = Foto(id=0, id_galeria=galeria, url="http://url.com/foto1.jpg", descricao="Foto 1")
        foto2 = Foto(id=0, id_galeria=galeria, url="http://url.com/foto2.jpg", descricao="Foto 2")
        foto1_id = repo.insert(foto1)
        foto2_id = repo.insert(foto2)
        # Act
        fotos = repo.get_all()
        # Assert
        assert len(fotos) == 2, "Deveria retornar duas fotos"
        assert fotos[0].id == foto1_id, "ID da primeira foto deveria ser igual ao ID inserido"
        assert fotos[0].url == "http://url.com/foto1.jpg", "URL da primeira foto deveria ser igual ao URL inserido"
        assert fotos[1].url == "http://url.com/foto2.jpg", "URL da segunda foto deveria ser igual ao URL inserido"
        assert fotos[1].id == foto2_id, "ID da segunda foto deveria ser igual ao ID inserido"

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
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        id_musico = repo_musico.insert(musico)

        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        galeria = Galeria(0, musico, "Galeria Teste", "Descrição da galeria")
        id_galeria = repo_galeria.insert(galeria)
        galeria.id = id_galeria

        repo = FotoRepo(test_db)
        repo.create_table()
        foto1 = Foto(id=0, id_galeria=galeria, url="http://url.com/foto1.jpg", descricao="Foto 1")
        foto2 = Foto(id=0, id_galeria=galeria, url="http://url.com/foto2.jpg", descricao="Foto 2")
        repo.insert(foto1)
        repo.insert(foto2)
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de fotos deveria ser igual a 2"

    def test_update_foto(self, test_db):
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
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        id_musico = repo_musico.insert(musico)

        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        galeria = Galeria(0, musico, "Galeria Teste", "Descrição da galeria")
        id_galeria = repo_galeria.insert(galeria)
        galeria.id = id_galeria

        repo = FotoRepo(test_db)
        repo.create_table()
        foto = Foto(id=0, id_galeria=galeria, url="http://url.com/foto.jpg", descricao="Foto de teste")
        id_foto = repo.insert(foto)
        foto.url = "http://url.com/foto-atualizada.jpg"
        foto.descricao = "Foto atualizada"
        foto.id = id_foto
        # Act
        resultado = repo.update(foto)
        # Assert
        assert resultado == True, "Atualização da foto deveria retornar True"
        foto_db = repo.get_by_id(id_foto)
        assert foto_db.url == "http://url.com/foto-atualizada.jpg"
        assert foto_db.descricao == "Foto atualizada"

    def test_delete_foto(self, test_db):
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
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425"), "experiencia teste")
        id_musico = repo_musico.insert(musico)

        repo_galeria = GaleriaRepo(test_db)
        repo_galeria.create_table()
        galeria = Galeria(0, musico, "Galeria Teste", "Descrição da galeria")
        id_galeria = repo_galeria.insert(galeria)
        galeria.id = id_galeria

        repo = FotoRepo(test_db)
        repo.create_table()
        foto = Foto(id=0, id_galeria=galeria, url="http://url.com/foto.jpg", descricao="Foto de teste")
        id_foto = repo.insert(foto)
        # Act
        resultado = repo.delete(id_foto)
        # Assert
        assert resultado == True, "Deleção da foto deveria retornar True"
        foto_db = repo.get_by_id(id_foto)
        assert foto_db is None, "Foto não deveria existir após deleção"