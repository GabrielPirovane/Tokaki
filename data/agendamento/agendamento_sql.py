SQL_CREATE_TABLE_AGENDAMENTO = """
CREATE TABLE IF NOT EXISTS agendamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_musico INTEGER NOT NULL,
    id_contratante INTEGER NOT NULL,
    id_agenda INTEGER NOT NULL,
    tipo_servico TEXT NOT NULL,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    data_hora DATETIME NOT NULL,
    taxa_aprovacao REAL NOT NULL,
    aprovado BOOLEAN NOT NULL,
    FOREIGN KEY (id_musico) REFERENCES musico(id),
    FOREIGN KEY (id_contratante) REFERENCES contratante(id),
    FOREIGN KEY (id_agenda) REFERENCES agenda(id)
);
"""

SQL_INSERT_AGENDAMENTO = """
INSERT INTO agendamento (id_musico, id_contratante, id_agenda, tipo_servico, descricao, valor, data_hora, taxa_aprovacao, aprovado)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

SQL_SELECT_RANGE_AGENDAMENTO = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado, u.nome AS nome_contratante, u2.nome AS nome_musico
FROM agendamento ag
JOIN contratante c ON ag.id_contratante = c.id
JOIN usuario u ON c.id = u.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
JOIN agenda a ON ag.id_agenda = a.id
ORDER BY ag.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_AGENDAMENTO = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado, u.nome AS nome_contratante, u2.nome AS nome_musico
FROM agendamento ag
JOIN contratante c ON ag.id_contratante = c.id
JOIN usuario u ON c.id = u.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
JOIN agenda a ON ag.id_agenda = a.id
WHERE nome_musico LIKE ?
ORDER BY nome_musico
LIMIT ? OFFSET ?;
"""

SQL_SELECT_AGENDAMENTO_BY_ID = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado, u.nome AS nome_contratante, u2.nome AS nome_musico
FROM agendamento ag
JOIN contratante c ON ag.id_contratante = c.id
JOIN usuario u ON c.id = u.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
JOIN agenda a ON ag.id_agenda = a.id
WHERE ag.id = ?;
"""

SQL_SELECT_COUNT_AGENDAMENTO = """
SELECT COUNT(*) FROM agendamento;
"""

SQL_SELECT_AGENDAMENTO = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado, u.nome AS nome_contratante, u2.nome AS nome_musico
FROM agendamento ag
JOIN contratante c ON ag.id_contratante = c.id
JOIN usuario u ON c.id = u.id
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u2 ON m.id = u2.id
JOIN agenda a ON ag.id_agenda = a.id
ORDER BY nome_musico;
"""

SQL_UPDATE_AGENDAMENTO = """
UPDATE agendamento
SET id_musico = ?,
    id_contratante = ?,
    id_agenda = ?,
    tipo_servico = ?,
    descricao = ?,
    valor = ?,
    data_hora = ?,
    taxa_aprovacao = ?,
    aprovado = ?
WHERE id = ?;
"""

SQL_DELETE_AGENDAMENTO = """
DELETE FROM agendamento
WHERE id = ?;
"""