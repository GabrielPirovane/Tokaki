SQL_CREATE_TABLE_SERVICO = """
CREATE TABLE IF NOT EXISTS servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
"""

SQL_INSERT_SERVICO = """
INSERT INTO servico (nome) 
VALUES (?);
"""

SQL_SELECT_RANGE_SERVICO = """
SELECT id, nome
FROM servico
ORDER BY id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_SERVICO = """
SELECT id, nome
FROM servico
WHERE nome LIKE ?
ORDER BY nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_SERVICO_BY_ID = """
SELECT id, nome
FROM servico
WHERE id = ?;
"""

SQL_SELECT_COUNT_SERVICO= """
SELECT COUNT(*) FROM servico;
"""

SQL_SELECT_SERVICO = """
SELECT id, nome, descricao
FROM servico
ORDER BY nome;
"""

SQL_UPDATE_SERVICO = """
UPDATE servico
SET nome = ?
WHERE id = ?;
"""

SQL_DELETE_SERVICO = """
DELETE FROM servico
WHERE id = ?;
"""