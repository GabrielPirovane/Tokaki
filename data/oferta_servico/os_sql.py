SQL_CREATE_TABLE_OFERTA_SERVICO = """
CREATE TABLE IF NOT EXISTS oferta_servico (
    id_servico INTEGER PRIMARY KEY,
    id_musico INTEGER NOT NULL,
    FOREIGN KEY (id_servico) REFERENCES servico(id),
    FOREIGN KEY (id_musico) REFERENCES musico(id)
);
"""

SQL_INSERT_OFERTA_SERVICO = """
INSERT INTO oferta_servico (id_servico, id_musico)
VALUES (?, ?);
"""

SQL_SELECT_RANGE_OFERTA_SERVICO = """
SELECT os.id_servico, os.id_musico, s.nome AS nome_categoria, m.nome AS nome_musico
FROM oferta_servico os
JOIN servico s ON os.id_servico = s.id
JOIN musico m ON os.id_musico = m.id
ORDER BY os.id_servico
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_OFERTA_SERVICO = """
SELECT os.id_servico, os.id_musico, s.nome AS nome_categoria, m.nome AS nome_musico
FROM oferta_servico os
JOIN servico s ON os.id_servico = s.id
JOIN musico m ON os.id_musico = m.id
WHERE nome_musico LIKE ?
ORDER BY nome_musico
LIMIT ? OFFSET ?;
"""

SQL_SELECT_OFERTA_SERVICO_BY_ID = """
SELECT os.id_servico, os.id_musico, s.nome AS nome_categoria, m.nome AS nome_musico
FROM oferta_servico os
JOIN servico s ON os.id_servico = s.id
JOIN musico m ON os.id_musico = m.id
WHERE os.id_servico = ?;
"""

SQL_SELECT_COUNT_OFERTA_SERVICO = """
SELECT COUNT(*) FROM oferta_servico;
"""

SQL_SELECT_OFERTA_SERVICO = """
SELECT id_servico, id_musico
FROM oferta_servico
ORDER BY nome;
"""

SQL_UPDATE_OFERTA_SERVICO = """
UPDATE oferta_servico
SET id_servico = ?, id_musico = ?
WHERE id_servico = ?;
"""

SQL_DELETE_OFERTA_SERVICO = """
DELETE FROM oferta_servico
WHERE id_servico = ?;
"""