from data.uf.uf_repo import *
from data.cidade.cidade_repo import *
from data.cidade.cidade_model import Cidade
from data.uf.uf_model import Uf
from data.usuario.usuario_repo import UsuarioRepo
from data.usuario.usuario_model import Usuario

class TestUsuarioRepo:
    def test_create_table_usuario(self, test_db):
        repo = UsuarioRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"
        
    def test_insert_usuario(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            nome="Usuário Teste",
            nome_usuario="usuario_teste",
            senha="senha123",
            email="teste@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        # Act
        id_usuario = repo_usuario.insert(usuario_teste)
        # Assert
        usuario_db = repo_usuario.get_by_id(id_usuario)
        assert usuario_db is not None, "Usuário não deveria ser None ao inserir"
        assert usuario_db.id == id_usuario, "ID do usuário buscado deveria ser igual ao ID inserido"
        assert usuario_db.id_cidade.id == id_cidade, "ID da cidade do usuário deveria ser igual ao inserido"
        assert usuario_db.nome == "Usuário Teste", "Nome do usuário deveria ser 'Usuário Teste'"
        assert usuario_db.nome_usuario == "usuario_teste", "Nome de usuário deveria ser 'usuario_teste'"
        assert usuario_db.email == "teste@email.com", "Email do usuário deveria ser 'teste@gmail.com'"
        assert usuario_db.cpf == "12345678900", "CPF do usuário deveria ser '12345678900'"
        assert usuario_db.telefone == "27999999999", "Telefone do usuário deveria ser '27999999999'"
        assert usuario_db.genero == "M", "Gênero do usuário deveria ser 'M'"
        assert usuario_db.logradouro == "Rua Teste", "Logradouro do usuário deveria ser 'Rua Teste'"
        assert usuario_db.numero == 123, "Número do usuário deveria ser '123'"
        assert usuario_db.bairro == "Centro", "Bairro do usuário deveria ser 'Centro'"
        assert usuario_db.complemento == "Apto 1", "Complemento do usuário deveria ser 'Apto 1'"
        assert usuario_db.cep == "29000000", "CEP do usuário deveria ser '29000000'"
       
    def test_get_by_id(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            nome="Usuário Teste",
            nome_usuario="usuario_teste",
            senha="senha123",
            email="teste@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        id_usuario = repo_usuario.insert(usuario_teste)
        # Act
        usuario_db = repo_usuario.get_by_id(id_usuario)
        # Assert
        assert usuario_db is not None, "Usuário não deveria ser None ao inserir"
        assert usuario_db.id == id_usuario, "ID do usuário buscado deveria ser igual ao ID inserido"
        assert usuario_db.id_cidade.id == id_cidade, "ID da cidade do usuário deveria ser igual ao inserido"
        assert usuario_db.nome == "Usuário Teste", "Nome do usuário deveria ser 'Usuário Teste'"
        assert usuario_db.nome_usuario == "usuario_teste", "Nome de usuário deveria ser 'usuario_teste'"
        assert usuario_db.email == "teste@email.com", "Email do usuário deveria ser 'teste@gmail.com'"
        assert usuario_db.cpf == "12345678900", "CPF do usuário deveria ser '12345678900'"
        assert usuario_db.telefone == "27999999999", "Telefone do usuário deveria ser '27999999999'"
        assert usuario_db.genero == "M", "Gênero do usuário deveria ser 'M'"
        assert usuario_db.logradouro == "Rua Teste", "Logradouro do usuário deveria ser 'Rua Teste'"
        assert usuario_db.numero == 123, "Número do usuário deveria ser '123'"
        assert usuario_db.bairro == "Centro", "Bairro do usuário deveria ser 'Centro'"
        assert usuario_db.complemento == "Apto 1", "Complemento do usuário deveria ser 'Apto 1'"
        assert usuario_db.cep == "29000000", "CEP do usuário deveria ser '29000000'"

    def test_count_usuario(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Cidade 1", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario1 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 1",
            nome_usuario="usuario1",
            senha="senha1",
            email="usuario1@email.com",
            cpf="11111111111",
            telefone="27999999991",
            genero="M",
            logradouro="Rua 1",
            numero="1",
            bairro="Bairro 1",
            complemento="Comp 1",
            cep="29000001"
        )
        usuario2 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 2",
            nome_usuario="usuario2",
            senha="senha2",
            email="usuario2@email.com",
            cpf="22222222222",
            telefone="27999999992",
            genero="F",
            logradouro="Rua 2",
            numero="2",
            bairro="Bairro 2",
            complemento="Comp 2",
            cep="29000002"
        )
        repo_usuario.insert(usuario1)
        repo_usuario.insert(usuario2)
        # Act
        count = repo_usuario.count()
        # Assert
        assert count == 2, "Contagem de usuários deveria ser igual a 2"
    
    def test_get_all_usuario(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Cidade 1", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario1 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 1",
            nome_usuario="usuario1",
            senha="senha1",
            email="usuario1@email.com",
            cpf="11111111111",
            telefone="27999999991",
            genero="M",
            logradouro="Rua 1",
            numero="1",
            bairro="Bairro 1",
            complemento="Comp 1",
            cep="29000001"
        )
        usuario2 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 2",
            nome_usuario="usuario2",
            senha="senha2",
            email="usuario2@email.com",
            cpf="22222222222",
            telefone="27999999992",
            genero="F",
            logradouro="Rua 2",
            numero="2",
            bairro="Bairro 2",
            complemento="Comp 2",
            cep="29000002"
        )
        repo_usuario.insert(usuario1)
        repo_usuario.insert(usuario2)
        # Act
        usuarios = repo_usuario.get_all()
        # Assert
        assert len(usuarios) == 2, "Deveria retornar dois usuários"
        assert usuarios[0].nome == "Usuário 1", "Primeiro usuário deveria ser 'Usuário 1'"
        assert usuarios[0].id_cidade.id == id_cidade, "ID da cidade do primeiro usuário deveria ser igual ao inserido"
        assert usuarios[1].nome == "Usuário 2", "Segundo usuário deveria ser 'Usuário 2'"
        assert usuarios[1].id_cidade.id == id_cidade, "ID da cidade do segundo usuário deveria ser igual ao inserido"
    
    def test_update_usuario(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Cidade Antiga", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade Antiga", Uf(id_uf, "Test UF")),
            nome="Usuário Antigo",
            nome_usuario="usuario_antigo",
            senha="senha_antiga",
            email="antigo@email.com",
            cpf="33333333333",
            telefone="27999999993",
            genero="M",
            logradouro="Rua Antiga",
            numero="3",
            bairro="Bairro Antigo",
            complemento="Comp Antigo",
            cep="29000003"
        )
        id_usuario = repo_usuario.insert(usuario)
        usuario_db = repo_usuario.get_by_id(id_usuario)
        # Act
        usuario_db.nome = "Usuário Atualizado"
        usuario_db.email = "atualizado@email.com"
        resultado = repo_usuario.update(usuario_db)
        usuario_atualizado = repo_usuario.get_by_id(id_usuario)
        # Assert
        assert resultado == True, "Atualização do usuário deveria retornar True"
        assert usuario_atualizado.nome == "Usuário Atualizado", "Nome do usuário atualizado deveria ser 'Usuário Atualizado'"
        assert usuario_atualizado.email == "atualizado@email.com", "Email do usuário atualizado deveria ser 'atualizado@email.com'"
    
    def test_delete_usuario(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Cidade Para Deletar", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade Para Deletar", Uf(id_uf, "Test UF")),
            nome="Usuário Para Deletar",
            nome_usuario="usuario_deletar",
            senha="senha_deletar",
            email="deletar@email.com",
            cpf="44444444444",
            telefone="27999999994",
            genero="F",
            logradouro="Rua Deletar",
            numero="4",
            bairro="Bairro Deletar",
            complemento="Comp Deletar",
            cep="29000004"
        )
        id_usuario = repo_usuario.insert(usuario)
        # Act
        resultado = repo_usuario.delete(id_usuario)
        # Assert
        assert resultado == True, "Deleção do usuário deveria retornar True"
        usuario_db = repo_usuario.get_by_id(id_usuario)
        assert usuario_db is None, "Usuário deveria ser None após deleção"
        
    def test_get_all_paged_usuario(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Cidade 1", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario1 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 1",
            nome_usuario="usuario1",
            senha="senha1",
            email="usuario1@email.com",
            cpf="11111111111",
            telefone="27999999991",
            genero="M",
            logradouro="Rua 1",
            numero="1",
            bairro="Bairro 1",
            complemento="Comp 1",
            cep="29000001"
        )
        usuario2 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 2",
            nome_usuario="usuario2",
            senha="senha2",
            email="usuario2@email.com",
            cpf="22222222222",
            telefone="27999999992",
            genero="F",
            logradouro="Rua 2",
            numero="2",
            bairro="Bairro 2",
            complemento="Comp 2",
            cep="29000002"
        )
        repo_usuario.insert(usuario1)
        repo_usuario.insert(usuario2)
        # Act
        usuarios_paged = repo_usuario.get_all_paged(page_number=1, page_size=1)
        # Assert
        assert len(usuarios_paged) == 1, "Deveria retornar apenas um usuário na primeira página"
        assert usuarios_paged[0].nome == "Usuário 1", "Primeiro usuário paginado deveria ser 'Usuário 1'"

        usuarios_paged_2 = repo_usuario.get_all_paged(page_number=2, page_size=1)
        assert len(usuarios_paged_2) == 1, "Deveria retornar apenas um usuário na segunda página"
        assert usuarios_paged_2[0].nome == "Usuário 2", "Segundo usuário paginado deveria ser 'Usuário 2'"

    def test_search_paged_usuario(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade = Cidade(0, "Cidade 1", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario1 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 1",
            nome_usuario="usuario1",
            senha="senha1",
            email="usuario1@email.com",
            cpf="11111111111",
            telefone="27999999991",
            genero="M",
            logradouro="Rua 1",
            numero="1",
            bairro="Bairro 1",
            complemento="Comp 1",
            cep="29000001"
        )
        usuario2 = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Cidade 1", Uf(id_uf, "Test UF")),
            nome="Usuário 2",
            nome_usuario="usuario2",
            senha="senha2",
            email="usuario2@email.com",
            cpf="22222222222",
            telefone="27999999992",
            genero="F",
            logradouro="Rua 2",
            numero="2",
            bairro="Bairro 2",
            complemento="Comp 2",
            cep="29000002"
        )
        repo_usuario.insert(usuario1)
        repo_usuario.insert(usuario2)
        # Act
        usuarios_search = repo_usuario.search_paged("Usuário 1", page_number=1, page_size=10)
        # Assert
        assert len(usuarios_search) == 1, "Busca paginada deveria retornar um usuário"
        assert usuarios_search[0].nome == "Usuário 1", "Usuário buscado deveria ser 'Usuário 1'"

        usuarios_search_none = repo_usuario.search_paged("Inexistente", page_number=1, page_size=10)
        assert len(usuarios_search_none) == 0, "Busca paginada deveria retornar zero usuários para termo inexistente"