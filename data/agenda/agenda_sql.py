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
SELECT a.id, a.data_hora, a.disponivel,
       m.experiencia,
       u.id AS usuario_id, u.id_cidade, u.nome AS usuario_nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero, u.logradouro, u.numero, u.bairro, u.complemento, u.cep
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
ORDER BY a.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_AGENDA = """
SELECT a.id, a.data_hora, a.disponivel,
       m.experiencia,
       u.id AS usuario_id, u.id_cidade, u.nome AS usuario_nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero, u.logradouro, u.numero, u.bairro, u.complemento, u.cep
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
WHERE u.nome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_AGENDA_BY_ID = """
SELECT a.id, a.data_hora, a.disponivel,
       m.experiencia,
       u.id AS usuario_id, u.id_cidade, u.nome AS usuario_nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero, u.logradouro, u.numero, u.bairro, u.complemento, u.cep
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
WHERE m.id = ?;
"""

SQL_SELECT_COUNT_AGENDA = """
SELECT COUNT(*) FROM agenda;
"""

SQL_SELECT_AGENDA = """
SELECT a.id, a.data_hora, a.disponivel,
       m.experiencia,
       u.id AS usuario_id, u.id_cidade, u.nome AS usuario_nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero, u.logradouro, u.numero, u.bairro, u.complemento, u.cep
FROM agenda a
JOIN musico m ON a.id = m.id
JOIN usuario u ON m.id = u.id
ORDER BY u.nome;
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