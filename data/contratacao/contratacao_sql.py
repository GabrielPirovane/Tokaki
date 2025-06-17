SQL_CREATE_TABLE_CONTRATACAO = """
CREATE TABLE IF NOT EXISTS contratacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_agendamento INTEGER NOT NULL,
    data_hora DATETIME NOT NULL,
    valor REAL NOT NULL,
    status_pagamento TEXT NOT NULL,
    nota FLOAT,
    comentario TEXT,
    autor TEXT,
    FOREIGN KEY (id_agendamento) REFERENCES agendamento(id)
);
"""

SQL_INSERT_CONTRATACAO = """
INSERT INTO contratacao (id_agendamento, data_hora, valor, status_pagamento, nota, comentario, autor)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

SQL_SELECT_RANGE_CONTRATACAO = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor, u1.nome AS nome_contratante, u2.nome AS nome_musico
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
JOIN contratante ct ON ag.id_contratante = ct.id
JOIN usuario u1 ON ct.id = u1.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
WHERE c.id = ?
ORDER BY u2.nome_musico
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CONTRATACAO = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor, u1.nome AS nome_contratante, u2.nome AS nome_musico
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
JOIN contratante ct ON ag.id_contratante = ct.id
JOIN usuario u1 ON ct.id = u1.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
WHERE nome_musico LIKE ?
ORDER BY nome_musico
LIMIT ? OFFSET ?;
"""

SQL_SELECT_CONTRATACAO_BY_ID = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor, u1.nome AS nome_contratante, u2.nome AS nome_musico
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
JOIN contratante ct ON ag.id_contratante = ct.id
JOIN usuario u1 ON ct.id = u1.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
WHERE c.id = ?;
"""

SQL_SELECT_COUNT_CONTRATACAO = """
SELECT COUNT(*) FROM contratacao;
"""

SQL_SELECT_CONTRATACAO = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor, u1.nome AS nome_contratante, u2.nome AS nome_musico
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
JOIN contratante ct ON ag.id_contratante = ct.id
JOIN usuario u1 ON ct.id = u1.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
ORDER BY nome_musico;
"""

SQL_UPDATE_CONTRATACAO = """
UPDATE contratacao
SET id_agendamento = ?,
    data_hora = ?,
    valor = ?,
    status_pagamento = ?,
    nota = ?,
    comentario = ?,
    autor = ?
WHERE id = ?;
"""

SQL_DELETE_CONTRATACAO = """
DELETE FROM contratacao
WHERE id = ?;
"""