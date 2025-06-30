SQL_CREATE_TABLE_GALERIA = """
CREATE TABLE IF NOT EXISTS galeria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_musico INTEGER NOT NULL,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_musico) REFERENCES musico(id)
);
"""

SQL_INSERT_GALERIA = """
INSERT INTO galeria (id_musico, nome, descricao) 
VALUES (?, ?, ?);
"""

SQL_SELECT_RANGE_GALERIA = """
SELECT id, id_musico, nome, descricao
FROM galeria
ORDER BY id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_GALERIA = """
SELECT g.id, g.nome, g.id_musico, g.descricao, m.nome AS nome_musico
FROM galeria g
JOIN musico m ON g.id_musico = m.id
WHERE g.nome LIKE ?
ORDER BY g.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_GALERIA_BY_ID = """
SELECT g.id, g.nome, g.id_musico, g.descricao, m.nome AS nome_musico
FROM galeria g
JOIN musico m ON g.id_musico = m.id
WHERE g.id = ?;
"""

SQL_SELECT_COUNT_GALERIA = """
SELECT COUNT(*) FROM galeria;
"""

SQL_SELECT_GALERIA = """
SELECT id, id_musico, nome, descricao
FROM galeria
ORDER BY nome;
"""

SQL_UPDATE_GALERIA = """
UPDATE galeria
SET id_musico = ?, nome = ?, descricao = ?
WHERE id = ?;
"""

SQL_DELETE_GALERIA = """
DELETE FROM galeria
WHERE id = ?;
"""