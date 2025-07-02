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
SELECT 
    os.id_servico, os.id_musico,
    s.nome AS nome_servico,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome AS usuario_nome,
    u.nome_usuario,
    u.senha,
    u.email,
    u.cpf,
    u.telefone,
    u.genero,
    u.logradouro,
    u.numero,
    u.bairro,
    u.complemento,
    u.cep,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM oferta_servico os
JOIN servico s ON os.id_servico = s.id
JOIN musico m ON os.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY os.id_servico
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_OFERTA_SERVICO = """
SELECT 
    os.id_servico, os.id_musico,
    s.nome AS nome_servico,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome AS usuario_nome,
    u.nome_usuario,
    u.senha,
    u.email,
    u.cpf,
    u.telefone,
    u.genero,
    u.logradouro,
    u.numero,
    u.bairro,
    u.complemento,
    u.cep,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM oferta_servico os
JOIN servico s ON os.id_servico = s.id
JOIN musico m ON os.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE s.nome LIKE ?
ORDER BY s.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_OFERTA_SERVICO_BY_ID = """
SELECT 
    os.id_servico, os.id_musico,
    s.nome AS nome_servico,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome AS usuario_nome,
    u.nome_usuario,
    u.senha,
    u.email,
    u.cpf,
    u.telefone,
    u.genero,
    u.logradouro,
    u.numero,
    u.bairro,
    u.complemento,
    u.cep,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM oferta_servico os
JOIN servico s ON os.id_servico = s.id
JOIN musico m ON os.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE os.id_servico = ?;
"""

SQL_SELECT_COUNT_OFERTA_SERVICO = """
SELECT COUNT(*) FROM oferta_servico;
"""

SQL_SELECT_OFERTA_SERVICO = """
SELECT 
    os.id_servico, os.id_musico,
    s.nome AS nome_servico,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome AS usuario_nome,
    u.nome_usuario,
    u.senha,
    u.email,
    u.cpf,
    u.telefone,
    u.genero,
    u.logradouro,
    u.numero,
    u.bairro,
    u.complemento,
    u.cep,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM oferta_servico os
JOIN servico s ON os.id_servico = s.id
JOIN musico m ON os.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY s.nome;
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