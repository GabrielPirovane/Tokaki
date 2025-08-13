SQL_CREATE_TABLE_CATEGORIA_MUSICO = """
CREATE TABLE IF NOT EXISTS categoria_musico (
    id_categoria INTEGER PRIMARY KEY,
    id_musico INTEGER NOT NULL,
    FOREIGN KEY (id_musico) REFERENCES musico(id),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);
"""

SQL_INSERT_CATEGORIA_MUSICO = """
INSERT INTO categoria_musico (id_categoria, id_musico) 
VALUES (?, ?);
"""

SQL_SELECT_RANGE_CATEGORIA_MUSICO = """
SELECT 
    cm.id_categoria, cm.id_musico,
    cat.nome AS nome_categoria, cat.descricao AS descricao_categoria,
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
FROM categoria_musico cm
JOIN categoria cat ON cm.id_categoria = cat.id
JOIN musico m ON cm.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY cm.id_categoria
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CATEGORIA_MUSICO = """
SELECT 
    cm.id_categoria, cm.id_musico,
    cat.nome AS nome_categoria, cat.descricao AS descricao_categoria,
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
FROM categoria_musico cm
JOIN categoria cat ON cm.id_categoria = cat.id
JOIN musico m ON cm.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE cat.nome LIKE ?
ORDER BY cat.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_CATEGORIA_MUSICO_BY_ID = """
SELECT 
    cm.id_categoria, cm.id_musico,
    cat.nome AS nome_categoria, cat.descricao AS descricao_categoria,
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
FROM categoria_musico cm
JOIN categoria cat ON cm.id_categoria = cat.id
JOIN musico m ON cm.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE cm.id_categoria = ?;
"""

SQL_SELECT_COUNT_CATEGORIA_MUSICO = """
SELECT COUNT(*) FROM categoria_musico;
"""

SQL_SELECT_CATEGORIA_MUSICO = """
SELECT 
    cm.id_categoria, cm.id_musico,
    cat.nome AS nome_categoria, cat.descricao AS descricao_categoria,
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
FROM categoria_musico cm
JOIN categoria cat ON cm.id_categoria = cat.id
JOIN musico m ON cm.id_musico = m.id
JOIN usuario u ON m.id = u.id
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY cat.nome;
"""

SQL_UPDATE_CATEGORIA_MUSICO = """
UPDATE categoria_musico
SET id_categoria = ?, id_musico = ?
WHERE id_categoria = ?;
"""

SQL_DELETE_CATEGORIA_MUSICO = """
DELETE FROM categoria_musico
WHERE id_categoria = ?;
"""