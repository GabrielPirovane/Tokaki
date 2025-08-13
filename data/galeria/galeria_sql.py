SQL_CREATE_TABLE_GALERIA = """
CREATE TABLE IF NOT EXISTS galeria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_musico INTEGER NOT NULL,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_musico) REFERENCES musico(id)
);
"""

SQL_INSERT_GALERIA = """
INSERT INTO galeria (id_musico, nome, descricao) 
VALUES (?, ?, ?);
"""

SQL_SELECT_RANGE_GALERIA = """
SELECT 
    g.id, g.id_musico, g.nome, g.descricao,
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
    u.data_nascimento,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM galeria g
JOIN musico m ON g.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY g.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_GALERIA = """
SELECT 
    g.id, g.id_musico, g.nome, g.descricao,
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
    u.data_nascimento,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM galeria g
JOIN musico m ON g.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE g.nome LIKE ?
ORDER BY g.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_GALERIA_BY_ID = """
SELECT 
    g.id, g.id_musico, g.nome, g.descricao,
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
    u.data_nascimento,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM galeria g
JOIN musico m ON g.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE g.id = ?;
"""

SQL_SELECT_COUNT_GALERIA = """
SELECT COUNT(*) FROM galeria;
"""

SQL_SELECT_GALERIA = """
SELECT 
    g.id, g.id_musico, g.nome, g.descricao,
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
    u.data_nascimento,
    c.id AS cidade_id,
    c.nome AS nome_cidade,
    uf.id AS uf_id,
    uf.nome AS nome_uf
FROM galeria g
JOIN musico m ON g.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY g.nome;
"""

SQL_UPDATE_GALERIA = """
UPDATE galeria
SET id_musico = ?, nome = ?, descricao = ?
WHERE id = ?;
"""

SQL_DELETE_GALERIA = """
DELETE FROM galeria
WHERE id = ?;
"""