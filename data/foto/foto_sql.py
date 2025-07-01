SQL_CREATE_TABLE_FOTO = """
CREATE TABLE IF NOT EXISTS foto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_galeria INTEGER NOT NULL,
    url TEXT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_galeria) REFERENCES galeria(id)
);
"""

SQL_INSERT_FOTO = """
INSERT INTO foto (id_galeria, url, descricao) 
VALUES (?, ?, ?);
"""

SQL_SELECT_FOTO_BY_ID = """
SELECT f.id, f.id_galeria, f.url, f.descricao, g.nome AS nome_galeria
FROM foto f
JOIN galeria g ON f.id_galeria = g.id
WHERE f.id = ?;
"""

SQL_SELECT_COUNT_FOTO = """
SELECT COUNT(*) FROM foto;
"""

SQL_SELECT_FOTO = """
SELECT f.id, f.id_galeria, f.url, f.descricao, g.nome AS nome_galeria
FROM foto f
JOIN galeria g ON f.id_galeria = g.id
ORDER BY f.id;
"""

SQL_UPDATE_FOTO = """
UPDATE foto
SET id_galeria = ?, url = ?, descricao = ?
WHERE id = ?;
"""

SQL_DELETE_FOTO = """
DELETE FROM foto
WHERE id = ?;
"""