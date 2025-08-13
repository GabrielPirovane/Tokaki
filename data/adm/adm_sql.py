SQL_CREATE_TABLE_ADMINISTRADOR = """
CREATE TABLE IF NOT EXISTS administrador (
    id INTEGER PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES usuario(id)
);
"""

SQL_INSERT_ADMINISTRADOR = """
INSERT INTO administrador (id) VALUES (?);
"""

SQL_SELECT_ADMINISTRADOR_BY_ID = """
SELECT a.id, u.nome AS nome_administrador
FROM administrador a
JOIN usuario u ON a.id = u.id
WHERE a.id = ?;
"""

SQL_SELECT_COUNT_ADMINISTRADOR = """
SELECT COUNT(*) FROM administrador;
"""

SQL_SELECT_ADMINISTRADOR = """
SELECT a.id, u.nome AS nome_administrador, u.email AS email_administrador
FROM administrador a
JOIN usuario u ON a.id = u.id
ORDER BY nome_administrador;
"""

SQL_UPDATE_ADMINISTRADOR = """
UPDATE administrador
SET id = ?
WHERE id = ?;
"""

SQL_DELETE_ADMINISTRADOR = """
DELETE FROM administrador
WHERE id = ?;
"""

