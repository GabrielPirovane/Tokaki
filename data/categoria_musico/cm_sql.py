SQL_CREATE_TABLE_CATEGORIA_MUSICO = """
CREATE TABLE IF NOT EXISTS categoria_musico (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    id_musico INTEGER NOT NULL,
    FOREIGN KEY (id_music) REFERENCES (id)
);
"""

SQL_INSERT_CATEGORIA_MUSICO = """
INSERT INTO categoria_musico (nome, id_uf) 
VALUES (?, ?);
"""

SQL_SELECT_RANGE_CATEGORIA_MUSICO = """
SELECT c.id, c.nome, c.id_uf, u.nome AS nome_uf
FROM categoria_musico c
JOIN uf u ON c.id_uf = u.id
ORDER BY c.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CATEGORIA_MUSICO = """
SELECT c.id, c.nome, c.id_uf, u.nome AS nome_uf
FROM categoria_musico c
JOIN uf u ON c.id_uf = u.id
WHERE nome LIKE ?
ORDER BY c.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_CATEGORIA_MUSICO_BY_ID = """
SELECT c.id, c.nome, c.id_uf, u.nome AS nome_uf
FROM categoria_musico c
JOIN uf u ON c.id_uf = u.id
WHERE c.id = ?;
"""

SQL_SELECT_COUNT_CATEGORIA_MUSICO = """
SELECT COUNT(*) FROM categoria_musico;
"""

SQL_SELECT_CATEGORIA_MUSICO = """
SELECT id, nome, id_uf
FROM categoria_musico
ORDER BY nome;
"""

SQL_UPDATE_CATEGORIA_MUSICO = """
UPDATE categoria_musico
SET nome = ?, id_uf = ?
WHERE id = ?;
"""

SQL_DELETE_CATEGORIA_MUSICO = """
DELETE FROM categoria_musico
WHERE id = ?;
"""