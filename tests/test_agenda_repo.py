import sys
import os
from data.agenda.agenda_repo import *
from data.musico.musico_repo import *
from data.usuario.usuario_repo import *
from data.cidade.cidade_repo import *
from data.uf.uf_repo import *

class TestAgendaRepo:
    def test_create_table_agenda(self, test_db):
        repo = AgendaRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"
    
    def test_insert_agenda(self, test_db):
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
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01")  # Adicionado campo data_nascimento
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01"), "experiencia teste")  # Adicionado campo data_nascimento
        id_musico = repo_musico.insert(musico)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda = Agenda(id=musico, data_hora="2025-07-01 10:00:00", disponivel=True)
        # Act
        id_agenda = repo.insert(agenda)
        # Assert
        assert id_agenda is not None, "ID da agenda inserida não deveria ser None"
        agenda_db = repo.get_by_id(id_musico)
        assert agenda_db is not None, "Agenda não deveria ser None ao buscar por ID"
        assert agenda_db.id.id.id == id_usuario, "ID do musico na agenda deveria ser igual ao ID do usuário inserido"
        assert agenda_db.data_hora == "2025-07-01 10:00:00"
        assert agenda_db.disponivel == True

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
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01")  # Adicionado campo data_nascimento
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01"), "experiencia teste")  # Adicionado campo data_nascimento
        id_musico = repo_musico.insert(musico)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda = Agenda(id=musico, data_hora="2025-07-01 10:00:00", disponivel=True)
        repo.insert(agenda)
        # Act
        agenda_db = repo.get_by_id(id_musico)
        # Assert
        assert agenda_db is not None, "Agenda não deveria ser None ao buscar por ID"
        assert agenda_db.id.id.id == id_usuario
        assert agenda_db.data_hora == "2025-07-01 10:00:00"
        assert agenda_db.disponivel == True

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
        usuario1 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01")  # Adicionado campo data_nascimento
        id_usuario1 = repo_usuario.insert(usuario1)
        usuario2 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02")  # Adicionado campo data_nascimento
        id_usuario2 = repo_usuario.insert(usuario2)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico1 = Musico(Usuario(id_usuario1, cidade, "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01"), "experiencia 1")  # Adicionado campo data_nascimento
        musico2 = Musico(Usuario(id_usuario2, cidade, "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02"), "experiencia 2")  # Adicionado campo data_nascimento
        id_musico1 = repo_musico.insert(musico1)
        id_musico2 = repo_musico.insert(musico2)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda1 = Agenda(id=musico1, data_hora="2025-07-01 10:00:00", disponivel=True)
        agenda2 = Agenda(id=musico2, data_hora="2025-07-02 11:00:00", disponivel=False)
        repo.insert(agenda1)
        repo.insert(agenda2)
        # Act
        agendas = repo.get_all_paged(page_number=1, page_size=10)
        # Assert
        assert len(agendas) == 2, "Deveria retornar duas agendas"
        assert agendas[0].id.id.id == id_usuario1, "ID do usuário do musico na primeira agenda deveria ser igual ao esperado"
        assert agendas[1].id.id.id == id_usuario2, "ID do usuário do musico na segunda agenda deveria ser igual ao esperado"

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
        usuario1 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01")  # Adicionado campo data_nascimento
        id_usuario1 = repo_usuario.insert(usuario1)
        usuario2 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02")  # Adicionado campo data_nascimento
        id_usuario2 = repo_usuario.insert(usuario2)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico1 = Musico(Usuario(id_usuario1, cidade, "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01"), "experiencia 1")  # Adicionado campo data_nascimento
        musico2 = Musico(Usuario(id_usuario2, cidade, "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02"), "experiencia 2")  # Adicionado campo data_nascimento
        id_musico1 = repo_musico.insert(musico1)
        id_musico2 = repo_musico.insert(musico2)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda1 = Agenda(id=musico1, data_hora="2025-07-01 10:00:00", disponivel=True)
        agenda2 = Agenda(id=musico2, data_hora="2025-07-02 11:00:00", disponivel=False)
        repo.insert(agenda1)
        repo.insert(agenda2)
        # Act
        agendas = repo.search_paged(termo="Musico", page_number=1, page_size=10)
        # Assert
        assert len(agendas) == 2, "Deveria retornar duas agendas"
        assert agendas[0].id.id.id == id_usuario1, "ID do usuário do musico na primeira agenda deveria ser igual ao esperado"
        assert agendas[1].id.id.id == id_usuario2, "ID do usuário do musico na segunda agenda deveria ser igual ao esperado"

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
        usuario1 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01")  # Adicionado campo data_nascimento
        id_usuario1 = repo_usuario.insert(usuario1)
        usuario2 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02")  # Adicionado campo data_nascimento
        id_usuario2 = repo_usuario.insert(usuario2)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico1 = Musico(Usuario(id_usuario1, cidade, "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01"), "experiencia 1")  # Adicionado campo data_nascimento
        musico2 = Musico(Usuario(id_usuario2, cidade, "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02"), "experiencia 2")  # Adicionado campo data_nascimento
        id_musico1 = repo_musico.insert(musico1)
        id_musico2 = repo_musico.insert(musico2)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda1 = Agenda(id=musico1, data_hora="2025-07-01 10:00:00", disponivel=True)
        agenda2 = Agenda(id=musico2, data_hora="2025-07-02 11:00:00", disponivel=False)
        repo.insert(agenda1)
        repo.insert(agenda2)
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de agendas deveria ser igual a 2"

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
        usuario1 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01")  # Adicionado campo data_nascimento
        id_usuario1 = repo_usuario.insert(usuario1)
        usuario2 = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02")  # Adicionado campo data_nascimento
        id_usuario2 = repo_usuario.insert(usuario2)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico1 = Musico(Usuario(id_usuario1, cidade, "Musico 1", "usuario1", "senha", "email1", "cpf1", "289999999991", "m", "logradouro1", "41", "bairro1", "complemento1", "29454421", data_nascimento="1990-01-01"), "experiencia 1")  # Adicionado campo data_nascimento
        musico2 = Musico(Usuario(id_usuario2, cidade, "Musico 2", "usuario2", "senha", "email2", "cpf2", "289999999992", "f", "logradouro2", "42", "bairro2", "complemento2", "29454422", data_nascimento="1992-02-02"), "experiencia 2")  # Adicionado campo data_nascimento
        id_musico1 = repo_musico.insert(musico1)
        id_musico2 = repo_musico.insert(musico2)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda1 = Agenda(id=musico1, data_hora="2025-07-01 10:00:00", disponivel=True)
        agenda2 = Agenda(id=musico2, data_hora="2025-07-02 11:00:00", disponivel=False)
        repo.insert(agenda1)
        repo.insert(agenda2)
        # Act
        agendas = repo.get_all()
        # Assert
        assert len(agendas) == 2, "Deveria retornar duas agendas"
        assert agendas[0].id.id.id == id_usuario1, "ID do usuário do musico na primeira agenda deveria ser igual ao esperado"
        assert agendas[1].id.id.id == id_usuario2, "ID do usuário do musico na segunda agenda deveria ser igual ao esperado"

    def test_update_agenda(self, test_db):
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
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01")  # Adicionado campo data_nascimento
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01"), "experiencia teste")  # Adicionado campo data_nascimento
        id_musico = repo_musico.insert(musico)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda = Agenda(id=musico, data_hora="2025-07-01 10:00:00", disponivel=True)
        repo.insert(agenda)
        agenda.data_hora = "2025-07-02 12:00:00"
        agenda.disponivel = False
        # Act
        resultado = repo.update(agenda)
        # Assert
        assert resultado == True, "Atualização da agenda deveria retornar True"
        agenda_db = repo.get_by_id(id_musico)
        assert agenda_db.data_hora == "2025-07-02 12:00:00"
        assert agenda_db.disponivel == False

    def test_delete_agenda(self, test_db):
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
        usuario = Usuario(0, Cidade(id_cidade, "Test Cidade", Uf(id_uf, "Test UF")), "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01")  # Adicionado campo data_nascimento
        id_usuario = repo_usuario.insert(usuario)

        repo_musico = MusicoRepo(test_db)
        repo_musico.create_table()
        musico = Musico(Usuario(id_usuario, cidade, "Nome Musico", "nome usuario", "senha", "email", "cpf", "289999999999", "m", "logradouro", "43", "bairro", "complemento", "29454425", data_nascimento="2000-01-01"), "experiencia teste")  # Adicionado campo data_nascimento
        id_musico = repo_musico.insert(musico)

        repo = AgendaRepo(test_db)
        repo.create_table()
        agenda = Agenda(id=musico, data_hora="2025-07-01 10:00:00", disponivel=True)
        repo.insert(agenda)
        # Act
        resultado = repo.delete(id_musico)
        # Assert
        assert resultado == True, "Deleção da agenda deveria retornar True"
        agenda_db = repo.get_by_id(id_musico)
        assert agenda_db is None, "Agenda não deveria existir após deleção"