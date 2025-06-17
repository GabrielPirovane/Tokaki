SQL_CREATE_TABLE_CONTRATANTE = """
CREATE TABLE IF NOT EXISTS contratante (
    id INTEGER PRIMARY KEY,
    nota FLOAT NOT NULL,
    numero_contratacoes INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES usuario(id)
);
"""

SQL_INSERT_CONTRATANTE = """
INSERT INTO contratante (id, nota, numero_contratacoes) 
VALUES (?, ?, ?);
"""

SQL_SELECT_RANGE_CONTRATANTE = """
SELECT c.id, c.nota, c.numero_contratacoes, u.nome AS nome_usuario
FROM contratante c
JOIN usuario u ON c.id = u.id
ORDER BY c.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CONTRATANTE = """
SELECT c.id, c.nota, c.numero_contratacoes, u.nome AS nome_usuario
FROM contratante c
JOIN usuario u ON c.id = u.id
WHERE nome_usuario LIKE ?
ORDER BY nome_usuario
LIMIT ? OFFSET ?;
"""

SQL_SELECT_CONTRATANTE_BY_ID = """
SELECT c.id, c.nota, c.numero_contratacoes, u.nome AS nome_usuario
FROM contratante c
JOIN usuario u ON c.id = u.id
WHERE c.id = ?;
"""

SQL_SELECT_COUNT_CONTRATANTE = """
SELECT COUNT(*) FROM contratante;
"""

SQL_SELECT_CONTRATANTE = """
SELECT c.id, c.nota, c.numero_contratacoes, u.nome AS nome_usuario
FROM contratante c
JOIN usuario u ON c.id = u.id
ORDER BY nome_usuario;
"""

SQL_UPDATE_CONTRATANTE = """
UPDATE contratante
SET nota = ?, numero_contratacoes = ?
WHERE id = ?;
"""

SQL_DELETE_CONTRATANTE = """
DELETE FROM contratante
WHERE id = ?;
"""