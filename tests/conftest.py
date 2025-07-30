import pytest
import os
import sys
import tempfile

# Adiciona o diretório raiz do projeto ao PYTHONPATH
# Isso permite importar módulos do projeto nos testes
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Fixture para criar um banco de dados temporário para testes
@pytest.fixture
def test_db():
    # Cria um arquivo temporário para o banco de dados
    db_fd, db_path = tempfile.mkstemp(suffix='.db')
    # Configura a variável de ambiente para usar o banco de teste
    os.environ['TEST_DATABASE_PATH'] = db_path
    # Retorna o caminho do banco de dados temporário
    yield db_path
    # Aguarde um pouco para garantir que todas as conexões foram fechadas (opcional)
    import time; time.sleep(0.1)
    os.close(db_fd)
    try:
        os.unlink(db_path)
    except PermissionError:
        print(f"Não foi possível remover {db_path}. Certifique-se de fechar todas as conexões.")