from data.oferta_servico.os_repo import *
from data.servico.servico_repo import *
from data.musico.musico_repo import *
from data.usuario.usuario_repo import *
from data.cidade.cidade_repo import *
from data.uf.uf_repo import *

class TestOfertaServicoRepo:
    def test_create_table_oferta_servico(self, test_db):
        repo = OfertaServicoRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_insert_oferta_servico(self, test_db):
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
                cidade,
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

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico = Servico(0, "Servico Teste")
        id_servico = repo_servico.insert(servico)
        servico.id = id_servico

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        os = OfertaServico(id_servico=servico, id_musico=musico)

        # Act
        id_os = repo.insert(os)
        os_db = repo.get_by_id(id_servico)

        # Assert
        assert id_os is not None, "ID da oferta_servico inserida não deveria ser None"
        assert id_os == id_servico, "O id do serviço em OfertaServico deve ser igual ao id do serviço criado"
        assert os_db.id_musico.id.id == id_usuario, "O id do músico em OfertaServico deve ser igual ao id do usuário criado"
        assert os_db.id_musico.id.data_nascimento == "2000-01-01", "Data de nascimento do músico deveria ser '2000-01-01'"

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
                cidade,
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

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico = Servico(0, "Servico Teste")
        id_servico = repo_servico.insert(servico)
        servico.id = id_servico

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        os = OfertaServico(id_servico=servico, id_musico=musico)
        id_os = repo.insert(os)

        # Act
        os_db = repo.get_by_id(id_servico)
        # Assert
        assert os_db is not None, "OfertaServico não deveria ser None ao buscar por ID"
        assert id_os == id_servico, "O id do serviço em OfertaServico deve ser igual ao id do serviço criado"
        assert os_db.id_musico.id.id == id_usuario, "O id do músico em OfertaServico deve ser igual ao id do usuário criado"
        assert os_db.id_musico.id.data_nascimento == "2000-01-01", "Data de nascimento do músico deveria ser '2000-01-01'"

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
                cidade,
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

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico1 = Servico(0, "Servico 1")
        servico2 = Servico(0, "Servico 2")
        id_servico1 = repo_servico.insert(servico1)
        servico1.id = id_servico1
        id_servico2 = repo_servico.insert(servico2)
        servico2.id = id_servico2

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        os1 = OfertaServico(id_servico=servico1, id_musico=musico)
        os2 = OfertaServico(id_servico=servico2, id_musico=musico)
        repo.insert(os1)
        repo.insert(os2)
        
        # Act
        oss = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(oss) == 2, "Deveria retornar duas ofertas_servico"
        assert oss[0].id_servico.nome == "Servico 1"
        assert oss[0].id_servico.id == id_servico1, "O id do serviço na primeira oferta_servico deve ser igual ao id do serviço criado"
        assert oss[0].id_musico.id.id == id_usuario, "ID do músico na primeira oferta_servico deve ser igual ao ID do usuário criado"
        assert oss[1].id_servico.nome == "Servico 2"
        assert oss[1].id_servico.id == id_servico2, "O id do serviço na segunda oferta_servico deve ser igual ao id do serviço criado"
        assert oss[1].id_musico.id.id == id_usuario, "ID do músico na segunda oferta_servico deve ser igual ao ID do usuário criado"

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
                cidade,
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

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico1 = Servico(0, "Servico 1")
        servico2 = Servico(0, "Outro Servico")
        id_servico1 = repo_servico.insert(servico1)
        servico1.id = id_servico1
        id_servico2 = repo_servico.insert(servico2)
        servico2.id = id_servico2

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        os1 = OfertaServico(id_servico=servico1, id_musico=musico)
        os2 = OfertaServico(id_servico=servico2, id_musico=musico)
        repo.insert(os1)
        repo.insert(os2)
        
        # Act
        oss = repo.search_paged(termo="Servico", page_number=1, page_size=10)
        # Assert
        assert len(oss) == 2, "Deveria retornar duas ofertas_servico com 'Servico' no nome"

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
                cidade,
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

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico1 = Servico(0, "Servico 1")
        servico2 = Servico(0, "Servico 2")
        id_servico1 = repo_servico.insert(servico1)
        servico1.id = id_servico1
        id_servico2 = repo_servico.insert(servico2)
        servico2.id = id_servico2

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        os1 = OfertaServico(id_servico=servico1, id_musico=musico)
        os2 = OfertaServico(id_servico=servico2, id_musico=musico)
        repo.insert(os1)
        repo.insert(os2)
        
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de ofertas_servico deveria ser igual a 2"

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
                cidade,
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

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico1 = Servico(0, "Servico 1")
        servico2 = Servico(0, "Servico 2")
        id_servico1 = repo_servico.insert(servico1)
        servico1.id = id_servico1
        id_servico2 = repo_servico.insert(servico2)
        servico2.id = id_servico2

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        os1 = OfertaServico(id_servico=servico1, id_musico=musico)
        os2 = OfertaServico(id_servico=servico2, id_musico=musico)
        repo.insert(os1)
        repo.insert(os2)
        
        # Act
        oss = repo.get_all()
        # Assert
        assert len(oss) == 2, "Deveria retornar duas ofertas_servico"
        assert oss[0].id_servico.nome == "Servico 1"
        assert oss[1].id_servico.nome == "Servico 2"

    def test_update_oferta_servico(self, test_db):
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
        id_usuario1 = repo_usuario.insert(usuario1)
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
        id_musico1 = repo_musico.insert(musico1)
        id_musico2 = repo_musico.insert(musico2)

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico1 = Servico(0, "Servico 1")
        id_servico1 = repo_servico.insert(servico1)
        servico1.id = id_servico1
        servico2 = Servico(0, "Servico 2")
        id_servico2 = repo_servico.insert(servico2)
        servico2.id = id_servico2

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        # Cria o registro original
        os = OfertaServico(id_servico=servico1, id_musico=musico1)
        repo.insert(os)

        # Salve o id antigo antes de atualizar
        id_servico_antigo = os.id_servico.id
        os.id_servico = servico2
        os.id_musico = musico2
        resultado = repo.update(os, id_servico_antigo)

        # Assert
        assert resultado == True, "Atualização da oferta_servico deveria retornar True"
        os_db = repo.get_by_id(id_servico2)
        assert os_db is not None, "OfertaServico atualizada deveria existir"
        assert os_db.id_servico.id == id_servico2, "ID do serviço em OfertaServico deveria ser atualizado"
        assert os_db.id_musico.id.id == id_usuario2, "ID do músico em OfertaServico deveria ser atualizado"
        assert os_db.id_musico.id.data_nascimento == "1992-02-02", "Data de nascimento do músico atualizado deveria ser '1992-02-02'"

    def test_delete_oferta_servico(self, test_db):
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
                cidade,
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

        repo_servico = ServicoRepo(test_db)
        repo_servico.create_table()
        servico = Servico(0, "Servico Teste")
        id_servico = repo_servico.insert(servico)
        servico.id = id_servico

        repo = OfertaServicoRepo(test_db)
        repo.create_table()
        os = OfertaServico(id_servico=servico, id_musico=musico)
        repo.insert(os)
        resultado = repo.delete(id_servico)

        assert resultado == True, "Deleção da oferta_servico deveria retornar True"
        os_db = repo.get_by_id(id_servico)
        assert os_db is None, "OfertaServico não deveria existir após deleção"