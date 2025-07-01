import sys
import os
from data.adm.adm_repo import *
from data.usuario.usuario_repo import *
from data.cidade.cidade_repo import *
from data.uf.uf_repo import *

class TestAdmRepo:
    def test_create_table_administrador(self, test_db):
        repo = AdmRepo(test_db)
        resultado = repo.create_table()
        assert resultado == True, "A criação da tabela deveria retornar True"
    
    def test_insert_administrador(self, test_db):
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
        usuario_teste = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Nome Adm", "nome usuario adm", "senha adm", "email adm", "cpf adm", "289999999999", "m",  "logradouro adm", "43", "bairro adm", "complemento adm", "29454425")
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = AdmRepo(test_db)
        repo.create_table()
        adm_teste = Administrador(id=id_usuario_inserido)
        
        # Act
        id_adm_inserido = repo.insert(adm_teste)
        # Assert
        assert id_adm_inserido is not None, "ID do Administrador inserido não deveria ser None"
        assert adm_teste.id == id_usuario_inserido, "ID do Administrador inserido deveria ser igual ao ID do usuário inserido"

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
        usuario_teste = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Nome Adm", "nome usuario adm", "senha adm", "email adm", "cpf adm", "289999999999", "m",  "logradouro adm", "43", "bairro adm", "complemento adm", "29454425")
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = AdmRepo(test_db)
        repo.create_table()
        adm_teste = Administrador(id=id_usuario_inserido)
        id_adm_inserido = repo.insert(adm_teste)
        
        # Act
        adm_db = repo.get_by_id(id_adm_inserido)
        # Assert
        assert adm_db is not None, "Administrador não deveria ser None ao buscar por ID"
        assert adm_db.id == id_usuario_inserido, "ID do Administrador deveria ser igual ao ID do usuário inserido"
    
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
        usuario_teste1 = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Adm 1", "nome usuario 1", "senha 1", "email 1", "cpf 1", "289999999991", "m",  "logradouro 1", "41", "bairro 1", "complemento 1", "29454421")
        id_usuario_inserido1 = repo_usuario.insert(usuario_teste1)
        usuario_teste2 = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Adm 2", "nome usuario 2", "senha 2", "email 2", "cpf 2", "289999999992", "f",  "logradouro 2", "42", "bairro 2", "complemento 2", "29454422")
        id_usuario_inserido2 = repo_usuario.insert(usuario_teste2)
        
        repo = AdmRepo(test_db)
        repo.create_table()
        adm_teste1 = Administrador(id=id_usuario_inserido1)
        adm_teste2 = Administrador(id=id_usuario_inserido2)
        repo.insert(adm_teste1)
        repo.insert(adm_teste2)
        # Act
        adms = repo.get_all()
        # Assert
        assert len(adms) == 2, "Deveria retornar dois Administradores"
        assert adms[0].id == id_usuario_inserido1
        assert adms[1].id == id_usuario_inserido2
      
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
        usuario_teste1 = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Adm 1", "nome usuario 1", "senha 1", "email 1", "cpf 1", "289999999991", "m",  "logradouro 1", "41", "bairro 1", "complemento 1", "29454421")
        id_usuario_inserido1 = repo_usuario.insert(usuario_teste1)
        usuario_teste2 = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Adm 2", "nome usuario 2", "senha 2", "email 2", "cpf 2", "289999999992", "f",  "logradouro 2", "42", "bairro 2", "complemento 2", "29454422")
        id_usuario_inserido2 = repo_usuario.insert(usuario_teste2)
        
        repo = AdmRepo(test_db)
        repo.create_table()
        adm_teste1 = Administrador(id=id_usuario_inserido1)
        adm_teste2 = Administrador(id=id_usuario_inserido2)
        repo.insert(adm_teste1)
        repo.insert(adm_teste2)
        # Act
        count = repo.count()
        # Assert
        assert count == 2, "Contagem de Administradores deveria ser igual a 2"

    def test_update_administrador_com_id_antigo(self, test_db):
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
        usuario_teste = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Nome Adm", "nome usuario adm", "senha adm", "email adm", "cpf adm", "289999999999", "m",  "logradouro adm", "43", "bairro adm", "complemento adm", "29454425")
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = AdmRepo(test_db)
        repo.create_table()
        adm_teste = Administrador(id=id_usuario_inserido)
        repo.insert(adm_teste)

        # Crie um novo usuário para ser o novo administrador
        novo_usuario = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Novo Adm", "novo usuario adm", "senha adm", "email adm", "cpf novo", "289999999998", "m",  "logradouro novo", "44", "bairro novo", "complemento novo", "29454426")
        novo_id = repo_usuario.insert(novo_usuario)

        id_antigo = adm_teste.id
        adm_teste.id = novo_id
        resultado = repo.update(adm_teste, id_antigo)
        assert resultado == True, "Atualização do Administrador deveria retornar True"
        adm_db = repo.get_by_id(novo_id)
        assert adm_db is not None, "Administrador atualizado deveria existir"
        assert adm_db.id == novo_id, "ID do Administrador deveria ser atualizado"

    def test_delete_administrador(self, test_db):
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
        usuario_teste = Usuario(0, Cidade(id_cidade_inserida, "Test Cidade", Uf(id_uf_inserida, "Test UF")), "Nome Adm", "nome usuario adm", "senha adm", "email adm", "cpf adm", "289999999999", "m",  "logradouro adm", "43", "bairro adm", "complemento adm", "29454425")
        id_usuario_inserido = repo_usuario.insert(usuario_teste)
        
        repo = AdmRepo(test_db)
        repo.create_table()
        adm_teste = Administrador(id=id_usuario_inserido)
        repo.insert(adm_teste)
        # Act
        resultado = repo.delete(id_usuario_inserido)
        # Assert
        assert resultado == True, "Deleção do Administrador deveria retornar True"
        adm_db = repo.get_by_id(id_usuario_inserido)
        assert adm_db is None, "Administrador não deveria existir após deleção"