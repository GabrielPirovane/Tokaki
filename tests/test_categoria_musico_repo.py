import sys
import os
from data.categoria_musico.cm_repo import *
from data.categoria.categoria_repo import *
from data.musico.musico_repo import *
from data.usuario.usuario_repo import *
from data.cidade.cidade_repo import *
from data.uf.uf_repo import *

class TestCategoriaMusicoRepo:
    def test_create_table_categoria_musico(self, test_db):
        repo = CategoriaMusicoRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_insert_categoria_musico(self, test_db):
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
        usuario = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Nome Musico",
            "nome usuario",
            "senha",
            "email",
            "cpf",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            Usuario(
                id_usuario,
                Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
                "Nome Musico",
                "nome usuario",
                "senha",
                "email",
                "cpf",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        id_musico = repo_musico.insert(musico)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria = Categoria(1, "Categoria Teste", "Descrição categoria")
        id_categoria = repo_categoria.insert(categoria)
        categoria.id = id_categoria  # <-- Atualize aqui!

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        cm = CategoriaMusico(categoria, musico)

        # Act
        id_cm = repo.insert(cm)
        cm_db = repo.get_by_id(id_categoria)
        
        # Assert
        assert id_cm is not None, "ID da categoria_musico inserida não deveria ser None"
        assert id_cm == id_categoria, "O id da categoria em CategoriaMusico deve ser igual ao id da categoria criada"
        assert cm_db.id_musico.id.id == id_musico, "O id do músico em CategoriaMusico deve ser igual ao id do músico criado"

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
        usuario = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Nome Musico",
            "nome usuario",
            "senha",
            "email",
            "cpf",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            Usuario(
                id_usuario,
                Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
                "Nome Musico",
                "nome usuario",
                "senha",
                "email",
                "cpf",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        id_musico = repo_musico.insert(musico)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria = Categoria(1, "Categoria Teste", "Descrição categoria")
        id_categoria = repo_categoria.insert(categoria)
        categoria.id = id_categoria  

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        cm = CategoriaMusico(categoria, musico)
        id_cm = repo.insert(cm)

        # Act
        cm_db = repo.get_by_id(id_categoria)
        # Assert
        assert cm_db is not None, "CategoriaMusico não deveria ser None ao buscar por ID"
        assert id_cm == id_categoria, "O id da categoria em CategoriaMusico deve ser igual ao id da categoria criada"
        assert cm_db.id_musico.id.id == id_musico, "O id do músico em CategoriaMusico deve ser igual ao id do músico criado"

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
        usuario = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Nome Musico",
            "nome usuario",
            "senha",
            "email",
            "cpf",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            Usuario(
                id_usuario,
                Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
                "Nome Musico",
                "nome usuario",
                "senha",
                "email",
                "cpf",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        repo_musico.insert(musico)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria1 = Categoria(0, "Categoria 1", "Descrição 1")
        categoria2 = Categoria(0, "Categoria 2", "Descrição 2")
        id_categoria1 = repo_categoria.insert(categoria1)
        categoria1.id = id_categoria1  
        id_categoria2 = repo_categoria.insert(categoria2)
        categoria2.id = id_categoria2

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        cm1 = CategoriaMusico(id_categoria=categoria1, id_musico=musico)
        cm2 = CategoriaMusico(id_categoria=categoria2, id_musico=musico)
        repo.insert(cm1)
        repo.insert(cm2)
        
        # Act
        cms = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(cms) == 2, "Deveria retornar duas categorias_musico"
        assert cms[0].id_categoria.nome == categoria1.nome, "Nome deveria ser 'Categoria 1'"
        assert cms[0].id_categoria.id == id_categoria1, "Id de categoria1 deveria ser 1"
        assert cms[1].id_categoria.nome == categoria2.nome, "Nome deveria ser 'Categoria 2'"
        assert cms[1].id_categoria.id == id_categoria2, "Id de categoria2 deveria ser 2"

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
        usuario = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Nome Musico",
            "nome usuario",
            "senha",
            "email",
            "cpf",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            Usuario(
                id_usuario,
                Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
                "Nome Musico",
                "nome usuario",
                "senha",
                "email",
                "cpf",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        repo_musico.insert(musico)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria1 = Categoria(0, "Categoria 1", "Descrição 1")
        categoria2 = Categoria(0, "Categoria 2", "Descrição 2")
        id_categoria1 = repo_categoria.insert(categoria1)
        categoria1.id = id_categoria1  
        id_categoria2 = repo_categoria.insert(categoria2)
        categoria2.id = id_categoria2

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        cm1 = CategoriaMusico(id_categoria=categoria1, id_musico=musico)
        cm2 = CategoriaMusico(id_categoria=categoria2, id_musico=musico)
        repo.insert(cm1)
        repo.insert(cm2)
        
        # Act
        cms = repo.search_paged(termo="Categoria", page_number=1, page_size=10)
        # Assert
        assert len(cms) == 2, "Deveria retornar duas categorias_musico com 'Categoria' no nome"

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
        usuario = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Nome Musico",
            "nome usuario",
            "senha",
            "email",
            "cpf",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            Usuario(
                id_usuario,
                Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
                "Nome Musico",
                "nome usuario",
                "senha",
                "email",
                "cpf",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        repo_musico.insert(musico)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria1 = Categoria(0, "Categoria 1", "Descrição 1")
        categoria2 = Categoria(0, "Categoria 2", "Descrição 2")
        id_categoria1 = repo_categoria.insert(categoria1)
        categoria1.id = id_categoria1  
        id_categoria2 = repo_categoria.insert(categoria2)
        categoria2.id = id_categoria2

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        cm1 = CategoriaMusico(id_categoria=categoria1, id_musico=musico)
        cm2 = CategoriaMusico(id_categoria=categoria2, id_musico=musico)
        repo.insert(cm1)
        repo.insert(cm2)
        
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de categorias_musico deveria ser igual a 2"

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
        usuario = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Nome Musico",
            "nome usuario",
            "senha",
            "email",
            "cpf",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            Usuario(
                id_usuario,
                Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
                "Nome Musico",
                "nome usuario",
                "senha",
                "email",
                "cpf",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        repo_musico.insert(musico)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria1 = Categoria(0, "Categoria 1", "Descrição 1")
        categoria2 = Categoria(0, "Categoria 2", "Descrição 2")
        id_categoria1 = repo_categoria.insert(categoria1)
        categoria1.id = id_categoria1  
        id_categoria2 = repo_categoria.insert(categoria2)
        categoria2.id = id_categoria2

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        cm1 = CategoriaMusico(id_categoria=categoria1, id_musico=musico)
        cm2 = CategoriaMusico(id_categoria=categoria2, id_musico=musico)
        repo.insert(cm1)
        repo.insert(cm2)
        
        # Act
        cms = repo.get_all()
        # Assert
        assert len(cms) == 2, "Deveria retornar duas categorias_musico"
        assert cms[0].id_categoria.nome == categoria1.nome, "Nome deveria ser 'Categoria 1'"
        assert cms[0].id_categoria.id == id_categoria1, "Id de categoria1 deveria ser 1"
        assert cms[1].id_categoria.nome == categoria2.nome, "Nome deveria ser 'Categoria 2'"
        assert cms[1].id_categoria.id == id_categoria2, "Id de categoria2 deveria ser 2"

    def test_update_categoria_musico(self, test_db):
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
        usuario1 = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Musico 1",
            "usuario1",
            "senha",
            "email1",
            "cpf1",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario1 = repo_usuario.insert(usuario1)
        usuario2 = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Musico 2",
            "usuario2",
            "senha",
            "email2",
            "cpf2",
            "289999999998",
            "f",
            "logradouro",
            "44",
            "bairro",
            "complemento",
            "29454426",
            data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
        )
        id_usuario2 = repo_usuario.insert(usuario2)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico1 = Musico(
            Usuario(
                id_usuario1,
                cidade,
                "Musico 1",
                "usuario1",
                "senha",
                "email1",
                "cpf1",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia 1"
        )
        id_musico1 = repo_musico.insert(musico1)
        musico2 = Musico(
            Usuario(
                id_usuario2,
                cidade,
                "Musico 2",
                "usuario2",
                "senha",
                "email2",
                "cpf2",
                "289999999998",
                "f",
                "logradouro",
                "44",
                "bairro",
                "complemento",
                "29454426",
                data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
            ),
            "experiencia 2"
        )
        id_musico2 = repo_musico.insert(musico2)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria1 = Categoria(0, "Categoria 1", "Descrição 1")
        id_categoria1 = repo_categoria.insert(categoria1)
        categoria1.id = id_categoria1
        categoria2 = Categoria(0, "Categoria 2", "Descrição 2")
        id_categoria2 = repo_categoria.insert(categoria2)
        categoria2.id = id_categoria2

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        # Cria o registro original
        cm = CategoriaMusico(id_categoria=categoria1, id_musico=musico1)
        repo.insert(cm)

        # Salve o id antigo antes de atualizar
        id_categoria_antigo = cm.id_categoria.id
        cm.id_categoria = categoria2
        cm.id_musico = musico2
        resultado = repo.update(cm, id_categoria_antigo)

        # Assert
        assert resultado == True, "Atualização da categoria_musico deveria retornar True"
        cm_db = repo.get_by_id(id_categoria2)
        assert cm_db is not None, "CategoriaMusico atualizado deveria existir"
        assert cm_db.id_categoria.id == id_categoria2, "ID da categoria em CategoriaMusico deveria ser atualizado"
        assert cm_db.id_musico.id.id == id_usuario2, "ID do músico em CategoriaMusico deveria ser atualizado"
        assert cm_db.id_musico.id.data_nascimento == "1992-02-02", "Data de nascimento do músico atualizado deveria ser '1992-02-02'"

    def test_delete_categoria_musico(self, test_db):
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
        usuario = Usuario(
            0,
            Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            "Nome Musico",
            "nome usuario",
            "senha",
            "email",
            "cpf",
            "289999999999",
            "m",
            "logradouro",
            "43",
            "bairro",
            "complemento",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            Usuario(
                id_usuario,
                Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
                "Nome Musico",
                "nome usuario",
                "senha",
                "email",
                "cpf",
                "289999999999",
                "m",
                "logradouro",
                "43",
                "bairro",
                "complemento",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        id_musico = repo_musico.insert(musico)

        repo_categoria = CategoriaRepo(test_db)
        repo_categoria.create_table()
        categoria = Categoria(1, "Categoria Teste", "Descrição categoria")
        id_categoria = repo_categoria.insert(categoria)
        categoria.id = id_categoria  # <-- Atualize aqui!

        repo = CategoriaMusicoRepo(test_db)
        repo.create_table()
        cm = CategoriaMusico(categoria, musico)
        
        repo.insert(cm)
        resultado = repo.delete(id_categoria)
        
        assert resultado == True, "Deleção da categoria_musico deveria retornar True"
        cm_db = repo.get_by_id(id_categoria)
        assert cm_db is None, "CategoriaMusico não deveria existir após deleção"