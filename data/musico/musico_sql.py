SQL_CREATE_TABLE_MUSICO = """
CREATE TABLE IF NOT EXISTS musico (
    id INTEGER PRIMARY KEY,
    experiencia TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES usuario(id)
);
"""

SQL_INSERT_MUSICO = """
INSERT INTO musico (id, experiencia) 
VALUES (?, ?);
"""

SQL_SELECT_RANGE_MUSICO = """
SELECT 
    m.id,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome,
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
FROM musico m
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY m.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_MUSICO = """
SELECT 
    m.id,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome,
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
FROM musico m
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.nome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_MUSICO_BY_ID = """
SELECT 
    m.id,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome,
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
FROM musico m
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE m.id = ?;
"""

SQL_SELECT_COUNT_MUSICO = """
SELECT COUNT(*) FROM musico;
"""

SQL_SELECT_MUSICO = """
SELECT 
    m.id,
    m.experiencia,
    u.id AS usuario_id,
    u.id_cidade,
    u.nome,
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
FROM musico m
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY u.nome;
"""

SQL_UPDATE_MUSICO = """
UPDATE musico
SET experiencia = ?
WHERE id = ?;
"""

SQL_DELETE_MUSICO = """
DELETE FROM musico
WHERE id = ?;
"""