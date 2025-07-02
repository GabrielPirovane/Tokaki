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

SQL_SELECT_CONTRATACAO_BY_ID = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor,
       ag.id AS agendamento_id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao,
       ag.valor AS agendamento_valor, ag.data_hora AS agendamento_data_hora, ag.taxa_aprovacao, ag.aprovado
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
WHERE c.id = ?;
"""

SQL_SELECT_RANGE_CONTRATACAO = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor,
       ag.id AS agendamento_id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao,
       ag.valor AS agendamento_valor, ag.data_hora AS agendamento_data_hora, ag.taxa_aprovacao, ag.aprovado
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
ORDER BY c.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CONTRATACAO = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor,
       ag.id AS agendamento_id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao,
       ag.valor AS agendamento_valor, ag.data_hora AS agendamento_data_hora, ag.taxa_aprovacao, ag.aprovado
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u ON m.id = u.id
WHERE u.nome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_COUNT_CONTRATACAO = """
SELECT COUNT(*) FROM contratacao;
"""

SQL_SELECT_CONTRATACAO = """
SELECT c.id, c.id_agendamento, c.data_hora, c.valor, c.status_pagamento, c.nota, c.comentario, c.autor,
       ag.id AS agendamento_id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao,
       ag.valor AS agendamento_valor, ag.data_hora AS agendamento_data_hora, ag.taxa_aprovacao, ag.aprovado
FROM contratacao c
JOIN agendamento ag ON c.id_agendamento = ag.id
ORDER BY c.id;
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