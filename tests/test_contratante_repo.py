from data.uf.uf_repo import *
from data.cidade.cidade_repo import *
from data.cidade.cidade_model import Cidade
from data.uf.uf_model import Uf
from data.usuario.usuario_repo import UsuarioRepo
from data.usuario.usuario_model import Usuario
from data.contratante.contratante_repo import ContratanteRepo
from data.contratante.contratante_model import Contratante

class TestContratanteRepo:
    def test_create_table_contratante(self, test_db):
        repo = ContratanteRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_insert_contratante(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade_teste)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Usuário Contratante",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario_teste)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante_teste = Contratante(
            id=Usuario(id_usuario, usuario_teste.id_cidade, usuario_teste.nome, usuario_teste.nome_usuario, usuario_teste.senha, usuario_teste.email, usuario_teste.cpf, usuario_teste.telefone, usuario_teste.genero, usuario_teste.logradouro, usuario_teste.numero, usuario_teste.bairro, usuario_teste.complemento, usuario_teste.cep, usuario_teste.data_nascimento),  # Adicionado campo data_nascimento
            nota=4.5,
            numero_contratacoes=2
        )
        # Act
        id_contratante = repo_contratante.insert(contratante_teste)
        # Assert
        contratante_db = repo_contratante.get_by_id(id_usuario)
        assert contratante_db is not None, "Contratante não deveria ser None ao inserir"
        assert contratante_db.id.id == id_usuario, "ID do contratante deveria ser igual ao do usuário inserido"
        assert contratante_db.nota == 4.5, "Nota do contratante deveria ser 4.5"
        assert contratante_db.numero_contratacoes == 2, "Número de contratações deveria ser 2"

    def test_get_by_id(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf = repo_uf.insert(uf_teste)

        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf, "Test UF"))
        id_cidade = repo_cidade.insert(cidade_teste)

        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Usuário Contratante",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario_teste)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante_teste = Contratante(
            id=Usuario(id_usuario, usuario_teste.id_cidade, usuario_teste.nome, usuario_teste.nome_usuario, usuario_teste.senha, usuario_teste.email, usuario_teste.cpf, usuario_teste.telefone, usuario_teste.genero, usuario_teste.logradouro, usuario_teste.numero, usuario_teste.bairro, usuario_teste.complemento, usuario_teste.cep, usuario_teste.data_nascimento),  # Adicionado campo data_nascimento
            nota=4.5,
            numero_contratacoes=2
        )
        repo_contratante.insert(contratante_teste)
        # Act
        contratante_db = repo_contratante.get_by_id(id_usuario)
        # Assert
        assert contratante_db is not None, "Contratante não deveria ser None ao buscar por ID"
        assert contratante_db.id.id == id_usuario, "ID do contratante deveria ser igual ao do usuário inserido"
        assert contratante_db.nota == 4.5, "Nota do contratante deveria ser 4.5"
        assert contratante_db.numero_contratacoes == 2, "Número de contratações deveria ser 2"

    def test_count_contratante(self, test_db):
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
            cep="29000001",
            data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
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
            cep="29000002",
            data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
        )
        id_usuario1 = repo_usuario.insert(usuario1)
        id_usuario2 = repo_usuario.insert(usuario2)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante1 = Contratante(
            id=Usuario(id_usuario1, usuario1.id_cidade, usuario1.nome, usuario1.nome_usuario, usuario1.senha, usuario1.email, usuario1.cpf, usuario1.telefone, usuario1.genero, usuario1.logradouro, usuario1.numero, usuario1.bairro, usuario1.complemento, usuario1.cep, usuario1.data_nascimento),  # Adicionado campo data_nascimento
            nota=4.0,
            numero_contratacoes=1
        )
        contratante2 = Contratante(
            id=Usuario(id_usuario2, usuario2.id_cidade, usuario2.nome, usuario2.nome_usuario, usuario2.senha, usuario2.email, usuario2.cpf, usuario2.telefone, usuario2.genero, usuario2.logradouro, usuario2.numero, usuario2.bairro, usuario2.complemento, usuario2.cep, usuario2.data_nascimento),  # Adicionado campo data_nascimento
            nota=5.0,
            numero_contratacoes=3
        )
        repo_contratante.insert(contratante1)
        repo_contratante.insert(contratante2)
        # Act
        count = repo_contratante.count()
        # Assert
        assert count == 2, "Contagem de contratantes deveria ser igual a 2"

    def test_get_all_contratante(self, test_db):
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
            cep="29000001",
            data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
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
            cep="29000002",
            data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
        )
        id_usuario1 = repo_usuario.insert(usuario1)
        id_usuario2 = repo_usuario.insert(usuario2)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante1 = Contratante(
            id=Usuario(id_usuario1, usuario1.id_cidade, usuario1.nome, usuario1.nome_usuario, usuario1.senha, usuario1.email, usuario1.cpf, usuario1.telefone, usuario1.genero, usuario1.logradouro, usuario1.numero, usuario1.bairro, usuario1.complemento, usuario1.cep, usuario1.data_nascimento),  # Adicionado campo data_nascimento
            nota=4.0,
            numero_contratacoes=1
        )
        contratante2 = Contratante(
            id=Usuario(id_usuario2, usuario2.id_cidade, usuario2.nome, usuario2.nome_usuario, usuario2.senha, usuario2.email, usuario2.cpf, usuario2.telefone, usuario2.genero, usuario2.logradouro, usuario2.numero, usuario2.bairro, usuario2.complemento, usuario2.cep, usuario2.data_nascimento),  # Adicionado campo data_nascimento
            nota=5.0,
            numero_contratacoes=3
        )
        repo_contratante.insert(contratante1)
        repo_contratante.insert(contratante2)
        # Act
        contratantes = repo_contratante.get_all()
        # Assert
        assert len(contratantes) == 2, "Deveria retornar dois contratantes"
        assert contratantes[0].nota == 4.0, "Nota do primeiro contratante deveria ser 4.0"
        assert contratantes[0].id.id == id_usuario1, "ID do primeiro contratante deveria ser igual ao do usuário 1"
        assert contratantes[1].nota == 5.0, "Nota do segundo contratante deveria ser 5.0"
        assert contratantes[1].id.id == id_usuario2, "ID do segundo contratante deveria ser igual ao do usuário 2"

    def test_update_contratante(self, test_db):
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
            cep="29000003",
            data_nascimento="1980-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario, usuario.id_cidade, usuario.nome, usuario.nome_usuario, usuario.senha, usuario.email, usuario.cpf, usuario.telefone, usuario.genero, usuario.logradouro, usuario.numero, usuario.bairro, usuario.complemento, usuario.cep, usuario.data_nascimento),  # Adicionado campo data_nascimento
            nota=3.0,
            numero_contratacoes=1
        )
        repo_contratante.insert(contratante)
        contratante_db = repo_contratante.get_by_id(id_usuario)
        # Act
        contratante_db.nota = 4.8
        contratante_db.numero_contratacoes = 5
        resultado = repo_contratante.update(contratante_db)
        contratante_atualizado = repo_contratante.get_by_id(id_usuario)
        # Assert
        assert resultado == True, "Atualização do contratante deveria retornar True"
        assert contratante_atualizado.nota == 4.8, "Nota do contratante atualizada deveria ser 4.8"
        assert contratante_atualizado.numero_contratacoes == 5, "Número de contratações atualizado deveria ser 5"

    def test_delete_contratante(self, test_db):
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
            cep="29000004",
            data_nascimento="1970-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario = repo_usuario.insert(usuario)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario, usuario.id_cidade, usuario.nome, usuario.nome_usuario, usuario.senha, usuario.email, usuario.cpf, usuario.telefone, usuario.genero, usuario.logradouro, usuario.numero, usuario.bairro, usuario.complemento, usuario.cep, usuario.data_nascimento),  # Adicionado campo data_nascimento
            nota=2.5,
            numero_contratacoes=1
        )
        repo_contratante.insert(contratante)
        # Act
        resultado = repo_contratante.delete(id_usuario)
        # Assert
        assert resultado == True, "Deleção do contratante deveria retornar True"
        contratante_db = repo_contratante.get_by_id(id_usuario)
        assert contratante_db is None, "Contratante deveria ser None após deleção"