SQL_CREATE_TABLE_MUSICO = """
CREATE TABLE IF NOT EXISTS musico (
    id INTEGER PRIMARY KEY,
    experiencia TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES usuario(id)
);
"""

SQL_INSERT_MUSICO = """
INSERT INTO musico (id, nome, experiencia) 
VALUES (?, ?, ?);
"""

SQL_SELECT_RANGE_MUSICO = """
SELECT m.id, m.nome, m.experiencia, u.nome AS nome_usuario
FROM musico m
JOIN usuario u ON m.id = u.id
ORDER BY m.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_MUSICO = """
SELECT m.id, m.nome, m.experiencia, u.nome AS nome_usuario
FROM musico m
JOIN usuario u ON m.id = u.id
WHERE m.nome LIKE ?
ORDER BY m.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_MUSICO_BY_ID = """
SELECT m.id, m.nome, m.experiencia, u.nome AS nome_usuario
FROM musico m
JOIN usuario u ON m.id = u.id
WHERE m.id = ?;
"""

SQL_SELECT_COUNT_MUSICO = """
SELECT COUNT(*) FROM musico;
"""

SQL_SELECT_MUSICO = """
SELECT id, nome, id_uf
FROM musico
ORDER BY nome;
"""

SQL_UPDATE_MUSICO = """
UPDATE musico
SET nome = ?, experiencia = ?
WHERE id = ?;
"""

SQL_DELETE_MUSICO = """
DELETE FROM musico
WHERE id = ?;
"""