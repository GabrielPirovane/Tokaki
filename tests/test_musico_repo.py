from data.musico.musico_repo import *
from data.usuario.usuario_repo import *
from data.cidade.cidade_repo import *
from data.uf.uf_repo import *

class TestMusicoRepo:
    def test_create_table_musico(self, test_db):
        repo = MusicoRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"
    
    def test_insert_musico(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Nome teste",
            "nome usuario teste",
            "senha teste",
            "email teste",
            "cpf teste",
            "289999999999",
            "m",
            "logradouro teste",
            "43",
            "bairro teste",
            "complemento teste",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste = Musico(
            Usuario(
                id_usuario_inserido,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Nome teste",
                "nome usuario teste",
                "senha teste",
                "email teste",
                "cpf teste",
                "289999999999",
                "m",
                "logradouro teste",
                43,
                "bairro teste",
                "complemento teste",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        
        # Act
        id_musico_inserido = repo.insert(musico_teste)
        # Assert
        assert id_musico_inserido is not None, "ID do Musico inserido não deveria ser None"
        assert musico_teste.id.id == id_usuario_inserido, "ID da Musico inserida deveria ser igual ao ID do usuário inserido"
        assert musico_teste.id.id_cidade.id == id_cidade_inserida, "ID da Cidade do Musico inserido deveria ser igual ao ID da cidade inserida"
        assert musico_teste.id.nome == "Nome teste", "Nome do Musico inserido deveria ser 'Nome teste'"
        assert musico_teste.id.nome_usuario == "nome usuario teste", "Nome de usuário do Musico inserido deveria ser 'nome usuario teste'"
        assert musico_teste.id.senha == "senha teste", "Senha do Musico inserido deveria ser 'senha teste'"
        assert musico_teste.id.email == "email teste", "Email do Musico inserido deveria ser 'email teste'"
        assert musico_teste.id.cpf == "cpf teste", "CPF do Musico inserido deveria ser 'cpf teste'"
        assert musico_teste.id.telefone == "289999999999", "Telefone do Musico inserido deveria ser '289999999999'"
        assert musico_teste.id.genero == "m", "Gênero do Musico inserido deveria ser 'm'"
        assert musico_teste.id.logradouro == "logradouro teste", "Logradouro do Musico inserido deveria ser 'logradouro teste'"
        assert musico_teste.id.numero == 43, "Número do Musico inserido deveria ser '43'"
        assert musico_teste.id.bairro == "bairro teste", "Bairro do Musico inserido deveria ser 'bairro teste'"
        assert musico_teste.id.complemento == "complemento teste", "Complemento do Musico inserido deveria ser 'complemento teste'"
        assert musico_teste.id.cep == "29454425", "CEP do Musico inserido deveria ser '29454425'"
        assert musico_teste.experiencia == "experiencia teste", "Experiência do Musico inserido deveria ser 'experiencia teste'"
        assert musico_teste.id.data_nascimento == "2000-01-01", "Data de nascimento do Musico inserido deveria ser '2000-01-01'"

    def test_get_by_id(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Nome teste",
            "nome usuario teste",
            "senha teste",
            "email teste",
            "cpf teste",
            "289999999999",
            "m",
            "logradouro teste",
            "43",
            "bairro teste",
            "complemento teste",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste = Musico(
            Usuario(
                id_usuario_inserido,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Nome teste",
                "nome usuario teste",
                "senha teste",
                "email teste",
                "cpf teste",
                "289999999999",
                "m",
                "logradouro teste",
                43,
                "bairro teste",
                "complemento teste",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        id
        id_musico_inserido = repo.insert(musico_teste)
        
        
        # Act
        musico_db = repo.get_by_id(id_musico_inserido)
        # Assert
        assert id_musico_inserido is not None, "ID do Musico inserido não deveria ser None"
        assert musico_teste.id.id == id_usuario_inserido, "ID da Musico inserida deveria ser igual ao ID do usuário inserido"
        assert musico_teste.id.id_cidade.id == id_cidade_inserida, "ID da Cidade do Musico inserido deveria ser igual ao ID da cidade inserida"
        assert musico_teste.id.nome == "Nome teste", "Nome do Musico inserido deveria ser 'Nome teste'"
        assert musico_teste.id.nome_usuario == "nome usuario teste", "Nome de usuário do Musico inserido deveria ser 'nome usuario teste'"
        assert musico_teste.id.senha == "senha teste", "Senha do Musico inserido deveria ser 'senha teste'"
        assert musico_teste.id.email == "email teste", "Email do Musico inserido deveria ser 'email teste'"
        assert musico_teste.id.cpf == "cpf teste", "CPF do Musico inserido deveria ser 'cpf teste'"
        assert musico_teste.id.telefone == "289999999999", "Telefone do Musico inserido deveria ser '289999999999'"
        assert musico_teste.id.genero == "m", "Gênero do Musico inserido deveria ser 'm'"
        assert musico_teste.id.logradouro == "logradouro teste", "Logradouro do Musico inserido deveria ser 'logradouro teste'"
        assert musico_teste.id.numero == 43, "Número do Musico inserido deveria ser '43'"
        assert musico_teste.id.bairro == "bairro teste", "Bairro do Musico inserido deveria ser 'bairro teste'"
        assert musico_teste.id.complemento == "complemento teste", "Complemento do Musico inserido deveria ser 'complemento teste'"
        assert musico_teste.id.cep == "29454425", "CEP do Musico inserido deveria ser '29454425'"
        assert musico_teste.experiencia == "experiencia teste", "Experiência do Musico inserido deveria ser 'experiencia teste'"
        assert musico_teste.id.data_nascimento == "2000-01-01", "Data de nascimento do Musico inserido deveria ser '2000-01-01'"
    
    def test_get_all_paged(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste1 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 1",
            "nome usuario 1",
            "senha 1",
            "email 1",
            "cpf 1",
            "289999999991",
            "m",
            "logradouro 1",
            "41",
            "bairro 1",
            "complemento 1",
            "29454421",
            data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido1 = repo_usuario.insert(usuario_teste1)
        usuario_teste2 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 2",
            "nome usuario 2",
            "senha 2",
            "email 2",
            "cpf 2",
            "289999999992",
            "f",
            "logradouro 2",
            "42",
            "bairro 2",
            "complemento 2",
            "29454422",
            data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido2 = repo_usuario.insert(usuario_teste2)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste1 = Musico(
            Usuario(
                id_usuario_inserido1,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 1",
                "nome usuario 1",
                "senha 1",
                "email 1",
                "cpf 1",
                "289999999991",
                "m",
                "logradouro 1",
                41,
                "bairro 1",
                "complemento 1",
                "29454421",
                data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia 1"
        )
        musico_teste2 = Musico(
            Usuario(
                id_usuario_inserido2,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 2",
                "nome usuario 2",
                "senha 2",
                "email 2",
                "cpf 2",
                "289999999992",
                "f",
                "logradouro 2",
                42,
                "bairro 2",
                "complemento 2",
                "29454422",
                data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
            ),
            "experiencia 2"
        )
        repo.insert(musico_teste1)
        repo.insert(musico_teste2)
        # Act
        musicos = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(musicos) == 2, "Deveria retornar duas Musicos"
        assert musicos[0].experiencia == "experiencia 1", "Experiência da primeira Musico deveria ser 'experiencia 1'"
        assert musicos[0].id.id == id_usuario_inserido1, "ID do usuário da primeira Musico deveria ser igual ao ID do usuário inserido"
        assert musicos[1].experiencia == "experiencia 2", "Experiência da segunda Musico deveria ser 'experiencia 2'"
        assert musicos[1].id.id == id_usuario_inserido2, "ID do usuário da segunda Musico deveria ser igual ao ID do usuário inserido"
        assert musicos[0].id.data_nascimento == "1990-01-01", "Data de nascimento do primeiro Musico deveria ser '1990-01-01'"
        assert musicos[1].id.data_nascimento == "1992-02-02", "Data de nascimento do segundo Musico deveria ser '1992-02-02'"

    def test_search_paged(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste1 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 1",
            "nome usuario 1",
            "senha 1",
            "email 1",
            "cpf 1",
            "289999999991",
            "m",
            "logradouro 1",
            "41",
            "bairro 1",
            "complemento 1",
            "29454421",
            data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido1 = repo_usuario.insert(usuario_teste1)
        usuario_teste2 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 2",
            "nome usuario 2",
            "senha 2",
            "email 2",
            "cpf 2",
            "289999999992",
            "f",
            "logradouro 2",
            "42",
            "bairro 2",
            "complemento 2",
            "29454422",
            data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido2 = repo_usuario.insert(usuario_teste2)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste1 = Musico(
            Usuario(
                id_usuario_inserido1,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 1",
                "nome usuario 1",
                "senha 1",
                "email 1",
                "cpf 1",
                "289999999991",
                "m",
                "logradouro 1",
                41,
                "bairro 1",
                "complemento 1",
                "29454421",
                data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia 1"
        )
        musico_teste2 = Musico(
            Usuario(
                id_usuario_inserido2,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 2",
                "nome usuario 2",
                "senha 2",
                "email 2",
                "cpf 2",
                "289999999992",
                "f",
                "logradouro 2",
                42,
                "bairro 2",
                "complemento 2",
                "29454422",
                data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
            ),
            "experiencia 2"
        )
        repo.insert(musico_teste1)
        repo.insert(musico_teste2)
        # Act
        musicos = repo.search_paged(termo="Test", page_number=1, page_size=10)
        # Assert
        assert len(musicos) == 2, "Deveria retornar duas Musicos"
        assert musicos[0].experiencia == "experiencia 1", "Experiência da primeira Musico deveria ser 'experiencia 1'"
        assert musicos[0].id.id == id_usuario_inserido1, "ID do usuário da primeira Musico deveria ser igual ao ID do usuário inserido"
        assert musicos[1].experiencia == "experiencia 2", "Experiência da segunda Musico deveria ser 'experiencia 2'"
        assert musicos[1].id.id == id_usuario_inserido2, "ID do usuário da segunda Musico deveria ser igual ao ID do usuário inserido"
        assert musicos[0].id.data_nascimento == "1990-01-01", "Data de nascimento do primeiro Musico deveria ser '1990-01-01'"
        assert musicos[1].id.data_nascimento == "1992-02-02", "Data de nascimento do segundo Musico deveria ser '1992-02-02'"

    def test_count(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste1 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 1",
            "nome usuario 1",
            "senha 1",
            "email 1",
            "cpf 1",
            "289999999991",
            "m",
            "logradouro 1",
            "41",
            "bairro 1",
            "complemento 1",
            "29454421",
            data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido1 = repo_usuario.insert(usuario_teste1)
        usuario_teste2 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 2",
            "nome usuario 2",
            "senha 2",
            "email 2",
            "cpf 2",
            "289999999992",
            "f",
            "logradouro 2",
            "42",
            "bairro 2",
            "complemento 2",
            "29454422",
            data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido2 = repo_usuario.insert(usuario_teste2)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste1 = Musico(
            Usuario(
                id_usuario_inserido1,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 1",
                "nome usuario 1",
                "senha 1",
                "email 1",
                "cpf 1",
                "289999999991",
                "m",
                "logradouro 1",
                41,
                "bairro 1",
                "complemento 1",
                "29454421",
                data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia 1"
        )
        musico_teste2 = Musico(
            Usuario(
                id_usuario_inserido2,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 2",
                "nome usuario 2",
                "senha 2",
                "email 2",
                "cpf 2",
                "289999999992",
                "f",
                "logradouro 2",
                42,
                "bairro 2",
                "complemento 2",
                "29454422",
                data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
            ),
            "experiencia 2"
        )
        repo.insert(musico_teste1)
        repo.insert(musico_teste2)
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de Musicos deveria ser igual a 2"

    def test_get_all(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste1 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 1",
            "nome usuario 1",
            "senha 1",
            "email 1",
            "cpf 1",
            "289999999991",
            "m",
            "logradouro 1",
            "41",
            "bairro 1",
            "complemento 1",
            "29454421",
            data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido1 = repo_usuario.insert(usuario_teste1)
        usuario_teste2 = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Test Musico 2",
            "nome usuario 2",
            "senha 2",
            "email 2",
            "cpf 2",
            "289999999992",
            "f",
            "logradouro 2",
            "42",
            "bairro 2",
            "complemento 2",
            "29454422",
            data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido2 = repo_usuario.insert(usuario_teste2)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste1 = Musico(
            Usuario(
                id_usuario_inserido1,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 1",
                "nome usuario 1",
                "senha 1",
                "email 1",
                "cpf 1",
                "289999999991",
                "m",
                "logradouro 1",
                41,
                "bairro 1",
                "complemento 1",
                "29454421",
                data_nascimento="1990-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia 1"
        )
        musico_teste2 = Musico(
            Usuario(
                id_usuario_inserido2,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Test Musico 2",
                "nome usuario 2",
                "senha 2",
                "email 2",
                "cpf 2",
                "289999999992",
                "f",
                "logradouro 2",
                42,
                "bairro 2",
                "complemento 2",
                "29454422",
                data_nascimento="1992-02-02"  # Adicionado campo data_nascimento
            ),
            "experiencia 2"
        )
        repo.insert(musico_teste1)
        repo.insert(musico_teste2)
        # Act
        musicos = repo.get_all()
        # Assert
        assert len(musicos) == 2, "Deveria retornar duas Musicos"
        assert musicos[0].id.nome == "Test Musico 1", "Primeira Musico deveria ser 'Test Musico 1'"
        assert musicos[1].id.nome == "Test Musico 2", "Segunda Musico deveria ser 'Test Musico 2'"

    def test_update_musico(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Nome teste",
            "nome usuario teste",
            "senha teste",
            "email teste",
            "cpf teste",
            "289999999999",
            "m",
            "logradouro teste",
            "43",
            "bairro teste",
            "complemento teste",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste = Musico(
            Usuario(
                id_usuario_inserido,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Nome teste",
                "nome usuario teste",
                "senha teste",
                "email teste",
                "cpf teste",
                "289999999999",
                "m",
                "logradouro teste",
                "43",
                "bairro teste",
                "complemento teste",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        id_musico_inserido = repo.insert(musico_teste)
        musico_teste.experiencia = "Updated experiencia"
        # Act
        resultado = repo.update(musico_teste)
        musico_db = repo.get_by_id(id_musico_inserido)
        # Assert
        assert resultado == True, "Atualização da Musico deveria retornar True"
        assert musico_db.id.id == id_usuario_inserido, "ID do usuário da Musico atualizada deveria ser igual ao ID do usuário inserido"
        assert musico_db.experiencia == "Updated experiencia", "Experiência da Musico atualizada deveria ser 'Updated experiencia'"
        assert musico_db.id.data_nascimento == "2000-01-01", "Data de nascimento do Musico buscado deveria ser '2000-01-01'"
    
    def test_delete_musico(self, test_db):
        # Arrange
        repo_uf = UfRepo(test_db)
        repo_uf.create_table()
        uf_teste = Uf(0, "Test UF")
        id_uf_inserida = repo_uf.insert(uf_teste)
        
        repo_cidade = CidadeRepo(test_db)
        repo_cidade.create_table()
        cidade_teste = Cidade(0, "Test Cidade", Uf(id_uf_inserida, "Test UF"))
        id_cidade_inserida = repo_cidade.insert(cidade_teste)
        
        repo_usuario = UsuarioRepo(test_db)
        repo_usuario.create_table()
        usuario_teste = Usuario(
            0,
            Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
            "Nome teste",
            "nome usuario teste",
            "senha teste",
            "email teste",
            "cpf teste",
            "289999999999",
            "m",
            "logradouro teste",
            "43",
            "bairro teste",
            "complemento teste",
            "29454425",
            data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
        )
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = MusicoRepo(test_db)
        repo.create_table()
        musico_teste = Musico(
            Usuario(
                id_usuario_inserido,
                Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")),
                "Nome teste",
                "nome usuario teste",
                "senha teste",
                "email teste",
                "cpf teste",
                "289999999999",
                "m",
                "logradouro teste",
                "43",
                "bairro teste",
                "complemento teste",
                "29454425",
                data_nascimento="2000-01-01"  # Adicionado campo data_nascimento
            ),
            "experiencia teste"
        )
        id_musico_inserido = repo.insert(musico_teste)
        # Act
        resultado = repo.delete(id_musico_inserido)
        # Assert
        assert resultado == True, "Deleção da Musico deveria retornar True"
        musico_db = repo.get_by_id(id_musico_inserido)
        assert musico_db is None, "Musico não deveria existir após deleção"