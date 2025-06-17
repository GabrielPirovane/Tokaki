SQL_CREATE_TABLE_GALERIA = """
CREATE TABLE IF NOT EXISTS galeria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
);
"""

SQL_INSERT_GALERIA = """
INSERT INTO galeria (nome, descricao) 
VALUES (?, ?);
"""

SQL_SELECT_RANGE_GALERIA = """
SELECT id, nome, descricao
FROM galeria
ORDER BY id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CIDADE = """
SELECT c.id, c.nome, c.id_uf, u.nome AS nome_uf
FROM cidade c
JOIN uf u ON c.id_uf = u.id
WHERE nome LIKE ?
ORDER BY c.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_CIDADE_BY_ID = """
SELECT c.id, c.nome, c.id_uf, u.nome AS nome_uf
FROM cidade c
JOIN uf u ON c.id_uf = u.id
WHERE c.id = ?;
"""

SQL_SELECT_COUNT_CIDADE = """
SELECT COUNT(*) FROM cidade;
"""

SQL_SELECT_CIDADE = """
SELECT id, nome, id_uf
FROM cidade
ORDER BY nome;
"""

SQL_UPDATE_CIDADE = """
UPDATE cidade
SET nome = ?, id_uf = ?
WHERE id = ?;
"""

SQL_DELETE_CIDADE = """
DELETE FROM cidade
WHERE id = ?;
"""