from data.uf.uf_repo import *
from data.cidade.cidade_repo import *
from data.cidade.cidade_model import Cidade
from data.uf.uf_model import Uf
from data.usuario.usuario_repo import UsuarioRepo
from data.usuario.usuario_model import Usuario
from data.contratante.contratante_repo import ContratanteRepo
from data.contratante.contratante_model import Contratante
from data.musico.musico_repo import MusicoRepo
from data.musico.musico_model import Musico
from data.agenda.agenda_repo import AgendaRepo
from data.agenda.agenda_model import Agenda
from data.agendamento.agendamento_repo import AgendamentoRepo
from data.agendamento.agendamento_model import Agendamento

class TestAgendamentoRepo:
    def test_create_table_agendamento(self, test_db):
        repo = AgendamentoRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_insert_agendamento(self, test_db):
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
        usuario_musico = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Musico Teste",
            nome_usuario="musico_teste",
            senha="senha123",
            email="musico@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        id_usuario_musico = repo_usuario.insert(usuario_musico)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=Usuario(id_usuario_musico, usuario_musico.id_cidade, usuario_musico.nome, usuario_musico.nome_usuario, usuario_musico.senha, usuario_musico.email, usuario_musico.cpf, usuario_musico.telefone, usuario_musico.genero, usuario_musico.logradouro, usuario_musico.numero, usuario_musico.bairro, usuario_musico.complemento, usuario_musico.cep),
            experiencia="Experiência Teste"
        )
        repo_musico.insert(musico)

        usuario_contratante = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Contratante Teste",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="98765432100",
            telefone="27999999998",
            genero="F",
            logradouro="Rua Teste 2",
            numero="456",
            bairro="Centro",
            complemento="Apto 2",
            cep="29000001"
        )
        id_usuario_contratante = repo_usuario.insert(usuario_contratante)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario_contratante, usuario_contratante.id_cidade, usuario_contratante.nome, usuario_contratante.nome_usuario, usuario_contratante.senha, usuario_contratante.email, usuario_contratante.cpf, usuario_contratante.telefone, usuario_contratante.genero, usuario_contratante.logradouro, usuario_contratante.numero, usuario_contratante.bairro, usuario_contratante.complemento, usuario_contratante.cep),
            nota=4.5,
            numero_contratacoes=2
        )
        repo_contratante.insert(contratante)

        repo_agenda = AgendaRepo(test_db)
        repo_agenda.create_table()
        agenda = Agenda(
            id=musico,
            data_hora="2024-07-01 10:00:00",
            disponivel=True
        )
        id_agenda = repo_agenda.insert(agenda)
        agenda.id = id_agenda

        repo_agendamento = AgendamentoRepo(test_db)
        repo_agendamento.create_table()
        agendamento = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Show",
            descricao="Show de teste",
            valor=1000.0,
            data_hora="2024-07-01 10:00:00",
            taxa_aprovacao=0.1,
            aprovado=True
        )
        # Act
        id_agendamento = repo_agendamento.insert(agendamento)
        # Assert
        agendamento_db = repo_agendamento.get_by_id(id_agendamento)
        assert agendamento_db is not None, "Agendamento não deveria ser None ao inserir"
        assert agendamento_db.tipo_servico == "Show", "Tipo de serviço deveria ser 'Show'"
        assert agendamento_db.valor == 1000.0, "Valor deveria ser 1000.0"
        assert agendamento_db.aprovado == True, "Aprovado deveria ser True"

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
        usuario_musico = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Musico Teste",
            nome_usuario="musico_teste",
            senha="senha123",
            email="musico@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        id_usuario_musico = repo_usuario.insert(usuario_musico)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=Usuario(id_usuario_musico, usuario_musico.id_cidade, usuario_musico.nome, usuario_musico.nome_usuario, usuario_musico.senha, usuario_musico.email, usuario_musico.cpf, usuario_musico.telefone, usuario_musico.genero, usuario_musico.logradouro, usuario_musico.numero, usuario_musico.bairro, usuario_musico.complemento, usuario_musico.cep),
            experiencia="Experiência Teste"
        )
        repo_musico.insert(musico)

        usuario_contratante = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Contratante Teste",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="98765432100",
            telefone="27999999998",
            genero="F",
            logradouro="Rua Teste 2",
            numero="456",
            bairro="Centro",
            complemento="Apto 2",
            cep="29000001"
        )
        id_usuario_contratante = repo_usuario.insert(usuario_contratante)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario_contratante, usuario_contratante.id_cidade, usuario_contratante.nome, usuario_contratante.nome_usuario, usuario_contratante.senha, usuario_contratante.email, usuario_contratante.cpf, usuario_contratante.telefone, usuario_contratante.genero, usuario_contratante.logradouro, usuario_contratante.numero, usuario_contratante.bairro, usuario_contratante.complemento, usuario_contratante.cep),
            nota=4.5,
            numero_contratacoes=2
        )
        repo_contratante.insert(contratante)

        repo_agenda = AgendaRepo(test_db)
        repo_agenda.create_table()
        agenda = Agenda(
            id=musico,
            data_hora="2024-07-01 10:00:00",
            disponivel=True
        )
        id_agenda = repo_agenda.insert(agenda)
        agenda.id = id_agenda

        repo_agendamento = AgendamentoRepo(test_db)
        repo_agendamento.create_table()
        agendamento = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Show",
            descricao="Show de teste",
            valor=1000.0,
            data_hora="2024-07-01 10:00:00",
            taxa_aprovacao=0.1,
            aprovado=True
        )
        id_agendamento = repo_agendamento.insert(agendamento)
        # Act
        agendamento_db = repo_agendamento.get_by_id(id_agendamento)
        # Assert
        assert agendamento_db is not None, "Agendamento não deveria ser None ao buscar por ID"
        assert agendamento_db.tipo_servico == "Show"
        assert agendamento_db.valor == 1000.0
        assert agendamento_db.aprovado == True

    def test_count_agendamento(self, test_db):
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
        usuario_musico = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Musico Teste",
            nome_usuario="musico_teste",
            senha="senha123",
            email="musico@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        id_usuario_musico = repo_usuario.insert(usuario_musico)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=Usuario(id_usuario_musico, usuario_musico.id_cidade, usuario_musico.nome, usuario_musico.nome_usuario, usuario_musico.senha, usuario_musico.email, usuario_musico.cpf, usuario_musico.telefone, usuario_musico.genero, usuario_musico.logradouro, usuario_musico.numero, usuario_musico.bairro, usuario_musico.complemento, usuario_musico.cep),
            experiencia="Experiência Teste"
        )
        repo_musico.insert(musico)

        usuario_contratante = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Contratante Teste",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="98765432100",
            telefone="27999999998",
            genero="F",
            logradouro="Rua Teste 2",
            numero="456",
            bairro="Centro",
            complemento="Apto 2",
            cep="29000001"
        )
        id_usuario_contratante = repo_usuario.insert(usuario_contratante)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario_contratante, usuario_contratante.id_cidade, usuario_contratante.nome, usuario_contratante.nome_usuario, usuario_contratante.senha, usuario_contratante.email, usuario_contratante.cpf, usuario_contratante.telefone, usuario_contratante.genero, usuario_contratante.logradouro, usuario_contratante.numero, usuario_contratante.bairro, usuario_contratante.complemento, usuario_contratante.cep),
            nota=4.5,
            numero_contratacoes=2
        )
        repo_contratante.insert(contratante)

        repo_agenda = AgendaRepo(test_db)
        repo_agenda.create_table()
        agenda = Agenda(
            id=musico,
            data_hora="2024-07-01 10:00:00",
            disponivel=True
        )
        id_agenda = repo_agenda.insert(agenda)
        agenda.id = id_agenda

        repo_agendamento = AgendamentoRepo(test_db)
        repo_agendamento.create_table()
        agendamento1 = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Show",
            descricao="Show de teste",
            valor=1000.0,
            data_hora="2024-07-01 10:00:00",
            taxa_aprovacao=0.1,
            aprovado=True
        )
        agendamento2 = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Evento",
            descricao="Evento de teste",
            valor=2000.0,
            data_hora="2024-07-02 15:00:00",
            taxa_aprovacao=0.2,
            aprovado=False
        )
        repo_agendamento.insert(agendamento1)
        repo_agendamento.insert(agendamento2)
        # Act
        count = repo_agendamento.count()
        # Assert
        assert count == 2, "Contagem de agendamentos deveria ser igual a 2"

    def test_get_all_agendamento(self, test_db):
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
        usuario_musico = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Musico Teste",
            nome_usuario="musico_teste",
            senha="senha123",
            email="musico@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        id_usuario_musico = repo_usuario.insert(usuario_musico)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=Usuario(id_usuario_musico, usuario_musico.id_cidade, usuario_musico.nome, usuario_musico.nome_usuario, usuario_musico.senha, usuario_musico.email, usuario_musico.cpf, usuario_musico.telefone, usuario_musico.genero, usuario_musico.logradouro, usuario_musico.numero, usuario_musico.bairro, usuario_musico.complemento, usuario_musico.cep),
            experiencia="Experiência Teste"
        )
        repo_musico.insert(musico)

        usuario_contratante = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Contratante Teste",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="98765432100",
            telefone="27999999998",
            genero="F",
            logradouro="Rua Teste 2",
            numero="456",
            bairro="Centro",
            complemento="Apto 2",
            cep="29000001"
        )
        id_usuario_contratante = repo_usuario.insert(usuario_contratante)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario_contratante, usuario_contratante.id_cidade, usuario_contratante.nome, usuario_contratante.nome_usuario, usuario_contratante.senha, usuario_contratante.email, usuario_contratante.cpf, usuario_contratante.telefone, usuario_contratante.genero, usuario_contratante.logradouro, usuario_contratante.numero, usuario_contratante.bairro, usuario_contratante.complemento, usuario_contratante.cep),
            nota=4.5,
            numero_contratacoes=2
        )
        repo_contratante.insert(contratante)

        repo_agenda = AgendaRepo(test_db)
        repo_agenda.create_table()
        agenda = Agenda(
            id=musico,
            data_hora="2024-07-01 10:00:00",
            disponivel=True
        )
        id_agenda = repo_agenda.insert(agenda)
        agenda.id = id_agenda

        repo_agendamento = AgendamentoRepo(test_db)
        repo_agendamento.create_table()
        agendamento1 = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Show",
            descricao="Show de teste",
            valor=1000.0,
            data_hora="2024-07-01 10:00:00",
            taxa_aprovacao=0.1,
            aprovado=True
        )
        agendamento2 = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Evento",
            descricao="Evento de teste",
            valor=2000.0,
            data_hora="2024-07-02 15:00:00",
            taxa_aprovacao=0.2,
            aprovado=False
        )
        repo_agendamento.insert(agendamento1)
        repo_agendamento.insert(agendamento2)
        # Act
        agendamentos = repo_agendamento.get_all()
        # Assert
        assert len(agendamentos) == 2, "Deveria retornar dois agendamentos"
        assert agendamentos[0].tipo_servico == "Show"
        assert agendamentos[1].tipo_servico == "Evento"

    def test_update_agendamento(self, test_db):
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
        usuario_musico = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Musico Teste",
            nome_usuario="musico_teste",
            senha="senha123",
            email="musico@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        id_usuario_musico = repo_usuario.insert(usuario_musico)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=Usuario(id_usuario_musico, usuario_musico.id_cidade, usuario_musico.nome, usuario_musico.nome_usuario, usuario_musico.senha, usuario_musico.email, usuario_musico.cpf, usuario_musico.telefone, usuario_musico.genero, usuario_musico.logradouro, usuario_musico.numero, usuario_musico.bairro, usuario_musico.complemento, usuario_musico.cep),
            experiencia="Experiência Teste"
        )
        repo_musico.insert(musico)

        usuario_contratante = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Contratante Teste",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="98765432100",
            telefone="27999999998",
            genero="F",
            logradouro="Rua Teste 2",
            numero="456",
            bairro="Centro",
            complemento="Apto 2",
            cep="29000001"
        )
        id_usuario_contratante = repo_usuario.insert(usuario_contratante)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario_contratante, usuario_contratante.id_cidade, usuario_contratante.nome, usuario_contratante.nome_usuario, usuario_contratante.senha, usuario_contratante.email, usuario_contratante.cpf, usuario_contratante.telefone, usuario_contratante.genero, usuario_contratante.logradouro, usuario_contratante.numero, usuario_contratante.bairro, usuario_contratante.complemento, usuario_contratante.cep),
            nota=4.5,
            numero_contratacoes=2
        )
        repo_contratante.insert(contratante)

        repo_agenda = AgendaRepo(test_db)
        repo_agenda.create_table()
        agenda = Agenda(
            id=musico,
            data_hora="2024-07-01 10:00:00",
            disponivel=True
        )
        id_agenda = repo_agenda.insert(agenda)
        agenda.id = id_agenda

        repo_agendamento = AgendamentoRepo(test_db)
        repo_agendamento.create_table()
        agendamento = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Show",
            descricao="Show de teste",
            valor=1000.0,
            data_hora="2024-07-01 10:00:00",
            taxa_aprovacao=0.1,
            aprovado=True
        )
        id_agendamento = repo_agendamento.insert(agendamento)
        agendamento_db = repo_agendamento.get_by_id(id_agendamento)
        # Act
        agendamento_db.tipo_servico = "Evento"
        agendamento_db.valor = 1500.0
        resultado = repo_agendamento.update(agendamento_db)
        agendamento_atualizado = repo_agendamento.get_by_id(id_agendamento)
        # Assert
        assert resultado == True, "Atualização do agendamento deveria retornar True"
        assert agendamento_atualizado.tipo_servico == "Evento"
        assert agendamento_atualizado.valor == 1500.0

    def test_delete_agendamento(self, test_db):
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
        usuario_musico = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Musico Teste",
            nome_usuario="musico_teste",
            senha="senha123",
            email="musico@email.com",
            cpf="12345678900",
            telefone="27999999999",
            genero="M",
            logradouro="Rua Teste",
            numero="123",
            bairro="Centro",
            complemento="Apto 1",
            cep="29000000"
        )
        id_usuario_musico = repo_usuario.insert(usuario_musico)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=Usuario(id_usuario_musico, usuario_musico.id_cidade, usuario_musico.nome, usuario_musico.nome_usuario, usuario_musico.senha, usuario_musico.email, usuario_musico.cpf, usuario_musico.telefone, usuario_musico.genero, usuario_musico.logradouro, usuario_musico.numero, usuario_musico.bairro, usuario_musico.complemento, usuario_musico.cep),
            experiencia="Experiência Teste"
        )
        repo_musico.insert(musico)

        usuario_contratante = Usuario(
            id=0,
            id_cidade=Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")),
            nome="Contratante Teste",
            nome_usuario="contratante_teste",
            senha="senha123",
            email="contratante@email.com",
            cpf="98765432100",
            telefone="27999999998",
            genero="F",
            logradouro="Rua Teste 2",
            numero="456",
            bairro="Centro",
            complemento="Apto 2",
            cep="29000001"
        )
        id_usuario_contratante = repo_usuario.insert(usuario_contratante)

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=Usuario(id_usuario_contratante, usuario_contratante.id_cidade, usuario_contratante.nome, usuario_contratante.nome_usuario, usuario_contratante.senha, usuario_contratante.email, usuario_contratante.cpf, usuario_contratante.telefone, usuario_contratante.genero, usuario_contratante.logradouro, usuario_contratante.numero, usuario_contratante.bairro, usuario_contratante.complemento, usuario_contratante.cep),
            nota=4.5,
            numero_contratacoes=2
        )
        repo_contratante.insert(contratante)

        repo_agenda = AgendaRepo(test_db)
        repo_agenda.create_table()
        agenda = Agenda(
            id=musico,
            data_hora="2024-07-01 10:00:00",
            disponivel=True
        )
        id_agenda = repo_agenda.insert(agenda)
        agenda.id = id_agenda

        repo_agendamento = AgendamentoRepo(test_db)
        repo_agendamento.create_table()
        agendamento = Agendamento(
            id=0,
            id_musico=musico,
            id_contratante=contratante,
            id_agenda=agenda,
            tipo_servico="Show",
            descricao="Show de teste",
            valor=1000.0,
            data_hora="2024-07-01 10:00:00",
            taxa_aprovacao=0.1,
            aprovado=True
        )
        id_agendamento = repo_agendamento.insert(agendamento)
        # Act
        resultado = repo_agendamento.delete(id_agendamento)
        # Assert
        assert resultado == True, "Deleção do agendamento deveria retornar True"
        agendamento_db = repo_agendamento.get_by_id(id_agendamento)
        assert agendamento_db is None, "Agendamento deveria ser None após deleção"