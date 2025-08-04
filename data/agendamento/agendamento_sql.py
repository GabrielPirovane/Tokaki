SQL_CREATE_TABLE_AGENDAMENTO = """
CREATE TABLE IF NOT EXISTS agendamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_musico INTEGER NOT NULL,
    id_contratante INTEGER NOT NULL,
    id_agenda INTEGER NOT NULL,
    tipo_servico TEXT NOT NULL,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    data_hora TEXT NOT NULL,
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

SQL_SELECT_AGENDAMENTO_BY_ID = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado
FROM agendamento ag
WHERE ag.id = ?;
"""

SQL_SELECT_RANGE_AGENDAMENTO = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado
FROM agendamento ag
ORDER BY ag.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_AGENDAMENTO = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado
FROM agendamento ag
JOIN musico m ON ag.id_musico = m.id
JOIN usuario u ON m.id = u.id
WHERE u.nome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_COUNT_AGENDAMENTO = """
SELECT COUNT(*) FROM agendamento;
"""

SQL_SELECT_AGENDAMENTO = """
SELECT ag.id, ag.id_musico, ag.id_contratante, ag.id_agenda, ag.tipo_servico, ag.descricao, ag.valor, ag.data_hora, ag.taxa_aprovacao, ag.aprovado
FROM agendamento ag
ORDER BY ag.id;
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