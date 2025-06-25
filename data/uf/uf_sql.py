SQL_CREATE_TABLE_UF = """
CREATE TABLE IF NOT EXISTS uf (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
"""

SQL_INSERT_UF = """
INSERT INTO uf (nome) 
VALUES (?);
"""

SQL_SELECT_UF_BY_ID = """
SELECT id, nome
FROM uf
WHERE id = ?;
"""

SQL_SELECT_COUNT_UF = """
SELECT COUNT(*) FROM uf;
"""

SQL_SELECT_UF = """
SELECT id, nome
FROM uf
ORDER BY nome;
"""

SQL_UPDATE_UF = """
UPDATE uf   
SET nome = ?
WHERE id = ?;
"""

SQL_DELETE_UF = """
DELETE FROM uf
WHERE id = ?;
"""