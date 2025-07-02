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
from data.contratacao.contratacao_repo import ContratacaoRepo
from data.contratacao.contratacao_model import Contratacao

class TestContratacaoRepo:
    def test_create_table_contratacao(self, test_db):
        repo = ContratacaoRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_insert_contratacao(self, test_db):
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
        usuario_musico.id = id_usuario_musico

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=usuario_musico,
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
        usuario_contratante.id = id_usuario_contratante

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=usuario_contratante,
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
        agendamento.id = id_agendamento

        repo_contratacao = ContratacaoRepo(test_db)
        repo_contratacao.create_table()
        contratacao = Contratacao(
            id=0,
            id_agendamento=agendamento,
            data_hora="2024-07-01 10:00:00",
            valor=1000.0,
            status_pagamento="Pago",
            nota=5.0,
            comentario="Ótimo serviço",
            autor="Cliente"
        )
        # Act
        id_contratacao = repo_contratacao.insert(contratacao)
        # Assert
        contratacao_db = repo_contratacao.get_by_id(id_contratacao)
        assert contratacao_db is not None, "Contratação não deveria ser None ao inserir"
        assert contratacao_db.valor == 1000.0, "Valor deveria ser 1000.0"
        assert contratacao_db.status_pagamento == "Pago"
        assert contratacao_db.nota == 5.0
        assert contratacao_db.comentario == "Ótimo serviço"
        assert contratacao_db.autor == "Cliente"

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
        usuario_musico.id = id_usuario_musico

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=usuario_musico,
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
        usuario_contratante.id = id_usuario_contratante

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=usuario_contratante,
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
        agendamento.id = id_agendamento

        repo_contratacao = ContratacaoRepo(test_db)
        repo_contratacao.create_table()
        contratacao = Contratacao(
            id=0,
            id_agendamento=agendamento,
            data_hora="2024-07-01 10:00:00",
            valor=1000.0,
            status_pagamento="Pago",
            nota=5.0,
            comentario="Ótimo serviço",
            autor="Cliente"
        )
        id_contratacao = repo_contratacao.insert(contratacao)
        # Act
        contratacao_db = repo_contratacao.get_by_id(id_contratacao)
        # Assert
        assert contratacao_db is not None, "Contratação não deveria ser None ao buscar por ID"
        assert contratacao_db.valor == 1000.0
        assert contratacao_db.status_pagamento == "Pago"
        assert contratacao_db.nota == 5.0
        assert contratacao_db.comentario == "Ótimo serviço"
        assert contratacao_db.autor == "Cliente"

    def test_count_contratacao(self, test_db):
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
        usuario_musico.id = id_usuario_musico

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=usuario_musico,
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
        usuario_contratante.id = id_usuario_contratante

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=usuario_contratante,
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
        id_agendamento1 = repo_agendamento.insert(agendamento1)
        id_agendamento2 = repo_agendamento.insert(agendamento2)
        agendamento1.id = id_agendamento1
        agendamento2.id = id_agendamento2

        repo_contratacao = ContratacaoRepo(test_db)
        repo_contratacao.create_table()
        contratacao1 = Contratacao(
            id=0,
            id_agendamento=agendamento1,
            data_hora="2024-07-01 10:00:00",
            valor=1000.0,
            status_pagamento="Pago",
            nota=5.0,
            comentario="Ótimo serviço",
            autor="Cliente"
        )
        contratacao2 = Contratacao(
            id=0,
            id_agendamento=agendamento2,
            data_hora="2024-07-02 15:00:00",
            valor=2000.0,
            status_pagamento="Pendente",
            nota=4.0,
            comentario="Bom serviço",
            autor="Cliente"
        )
        id_contratacao1 = repo_contratacao.insert(contratacao1)
        id_contratacao2 = repo_contratacao.insert(contratacao2)
        assert id_contratacao1 is not None, "Falha ao inserir contratacao1"
        assert id_contratacao2 is not None, "Falha ao inserir contratacao2"
        # Act
        count = repo_contratacao.count()
        # Assert
        assert count == 2, "Contagem de contratações deveria ser igual a 2"

    def test_get_all_contratacao(self, test_db):
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
        usuario_musico.id = id_usuario_musico

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=usuario_musico,
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
        usuario_contratante.id = id_usuario_contratante

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=usuario_contratante,
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
        id_agendamento1 = repo_agendamento.insert(agendamento1)
        id_agendamento2 = repo_agendamento.insert(agendamento2)
        agendamento1.id = id_agendamento1
        agendamento2.id = id_agendamento2

        repo_contratacao = ContratacaoRepo(test_db)
        repo_contratacao.create_table()
        contratacao1 = Contratacao(
            id=0,
            id_agendamento=agendamento1,
            data_hora="2024-07-01 10:00:00",
            valor=1000.0,
            status_pagamento="Pago",
            nota=5.0,
            comentario="Ótimo serviço",
            autor="Cliente"
        )
        contratacao2 = Contratacao(
            id=0,
            id_agendamento=agendamento2,
            data_hora="2024-07-02 15:00:00",
            valor=2000.0,
            status_pagamento="Pendente",
            nota=4.0,
            comentario="Bom serviço",
            autor="Cliente"
        )
        id_contratacao1 = repo_contratacao.insert(contratacao1)
        id_contratacao2 = repo_contratacao.insert(contratacao2)

        assert id_contratacao1 is not None, "Falha ao inserir contratacao1"
        assert id_contratacao2 is not None, "Falha ao inserir contratacao2"
        # Act
        contratacoes = repo_contratacao.get_all()
        # Assert
        assert len(contratacoes) == 2, "Deveria retornar duas contratações"
        assert contratacoes[0].valor == 1000.0
        assert contratacoes[1].valor == 2000.0

    def test_update_contratacao(self, test_db):
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
        usuario_musico.id = id_usuario_musico

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=usuario_musico,
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
        usuario_contratante.id = id_usuario_contratante

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=usuario_contratante,
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
        agendamento.id = id_agendamento

        repo_contratacao = ContratacaoRepo(test_db)
        repo_contratacao.create_table()
        contratacao = Contratacao(
            id=0,
            id_agendamento=agendamento,
            data_hora="2024-07-01 10:00:00",
            valor=1000.0,
            status_pagamento="Pago",
            nota=5.0,
            comentario="Ótimo serviço",
            autor="Cliente"
        )
        id_contratacao = repo_contratacao.insert(contratacao)
        contratacao_db = repo_contratacao.get_by_id(id_contratacao)
        # Act
        contratacao_db.valor = 1500.0
        contratacao_db.status_pagamento = "Pendente"
        contratacao_db.nota = 4.0
        contratacao_db.comentario = "Bom serviço"
        contratacao_db.autor = "Cliente Atualizado"
        resultado = repo_contratacao.update(contratacao_db)
        contratacao_atualizada = repo_contratacao.get_by_id(id_contratacao)
        # Assert
        assert resultado == True, "Atualização da contratação deveria retornar True"
        assert contratacao_atualizada.valor == 1500.0
        assert contratacao_atualizada.status_pagamento == "Pendente"
        assert contratacao_atualizada.nota == 4.0
        assert contratacao_atualizada.comentario == "Bom serviço"
        assert contratacao_atualizada.autor == "Cliente Atualizado"

    def test_delete_contratacao(self, test_db):
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
        usuario_musico.id = id_usuario_musico

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(
            id=usuario_musico,
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
        usuario_contratante.id = id_usuario_contratante

        repo_contratante = ContratanteRepo(test_db)
        repo_contratante.create_table()
        contratante = Contratante(
            id=usuario_contratante,
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
        agendamento.id = id_agendamento

        repo_contratacao = ContratacaoRepo(test_db)
        repo_contratacao.create_table()
        contratacao = Contratacao(
            id=0,
            id_agendamento=agendamento,
            data_hora="2024-07-01 10:00:00",
            valor=1000.0,
            status_pagamento="Pago",
            nota=5.0,
            comentario="Ótimo serviço",
            autor="Cliente"
        )
        id_contratacao = repo_contratacao.insert(contratacao)
        # Act
        resultado = repo_contratacao.delete(id_contratacao)
        # Assert
        assert resultado == True, "Deleção da contratação deveria retornar True"
        contratacao_db = repo_contratacao.get_by_id(id_contratacao)
        assert contratacao_db is None, "Contratação deveria ser None após deleção"