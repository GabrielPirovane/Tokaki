SQL_CREATE_TABLE_AGENDA = """
CREATE TABLE IF NOT EXISTS agenda (
    id INTEGER PRIMARY KEY,
    data_hora DATETIME NOT NULL,
    disponivel BOOLEAN NOT NULL,
    FOREIGN KEY (id) REFERENCES musico(id)
);
"""

SQL_INSERT_AGENDA = """
INSERT INTO agenda (id, data_hora, disponivel) 
VALUES (?, ?, ?);
"""

SQL_SELECT_RANGE_AGENDA = """
SELECT a.id, a.data_hora, a.disponivel, u.nome AS nome_usuario
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
ORDER BY a.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_AGENDA = """
SELECT a.id, a.data_hora, a.disponivel, u.nome AS nome_usuario
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
WHERE nome_usuario LIKE ?
ORDER BY m.
LIMIT ? OFFSET ?;
"""

SQL_SELECT_AGENDA_BY_ID = """
SELECT a.id, a.data_hora, a.disponivel, u.nome AS nome_usuario
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
WHERE m.id = ?;
"""

SQL_SELECT_COUNT_AGENDA = """
SELECT COUNT(*) FROM agenda;
"""

SQL_SELECT_AGENDA = """
SELECT a.id, a.data_hora, a.disponivel, u.nome AS nome_usuario
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
ORDER BY nome_usuario;
"""

SQL_UPDATE_AGENDA = """
UPDATE agenda
SET data_hora = ?, disponivel = ?
WHERE id = ?;
"""

SQL_DELETE_AGENDA = """
DELETE FROM agenda
WHERE id = ?;
"""