SQL_CREATE_TABLE_CATEGORIA = """
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL
);
"""

SQL_INSERT_CATEGORIA = """
INSERT INTO categoria (nome, descricao) 
VALUES (?, ?);
"""

SQL_SELECT_RANGE_CATEGORIA = """
SELECT id, nome, descricao
FROM categoria
ORDER BY id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CATEGORIA = """
SELECT id, nome, descricao
FROM categoria  
WHERE nome LIKE ?
ORDER BY nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_CATEGORIA_BY_ID = """
SELECT id, nome, descricao
FROM categoria
WHERE id = ?;
"""

SQL_SELECT_COUNT_CATEGORIA= """
SELECT COUNT(*) FROM categoria;
"""

SQL_SELECT_CATEGORIA = """
SELECT id, nome, descricao
FROM categoria
ORDER BY nome;
"""

SQL_UPDATE_CATEGORIA = """
UPDATE categoria
SET nome = ?, descricao = ?
WHERE id = ?;
"""

SQL_DELETE_CATEGORIA = """
DELETE FROM categoria
WHERE id = ?;
"""