SQL_CREATE_TABLE_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cidade INTEGER NOT NULL,
    nome TEXT NOT NULL,
    nome_usuario TEXT NOT NULL,
    senha TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL,
    telefone TEXT NOT NULL,
    genero TEXT NOT NULL,
    logradouro TEXT NOT NULL,
    numero INTEGER NOT NULL CHECK(numero > 0),
    bairro TEXT NOT NULL,
    complemento TEXT,
    cep TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidade(id)
);
"""

SQL_INSERT_USUARIO = """
INSERT INTO usuario (id_cidade, nome, nome_usuario, senha, email, cpf, telefone, genero, logradouro, numero, bairro, complemento, cep, data_nascimento) 
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);
"""

SQL_SELECT_RANGE_USUARIO = """
SELECT u.id, u.id_cidade, u.nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY u.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_USUARIO = """
SELECT u.id, u.id_cidade, u.nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.nome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_USUARIO_EMAIL = """
SELECT u.id, u.id_cidade, u.nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.email LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_USUARIO_BY_ID = """
SELECT u.id, u.id_cidade, u.nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.id = ?;
"""

SQL_SELECT_COUNT_USUARIO = """
SELECT COUNT(*) FROM usuario;
"""

SQL_SELECT_USUARIO = """
SELECT u.id, u.id_cidade, u.nome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY u.nome;
"""

SQL_UPDATE_USUARIO = """
UPDATE usuario
SET id_cidade = ?, nome = ?, nome_usuario = ?, senha = ?, email = ?, cpf = ?, telefone = ?, genero = ?, logradouro = ?, numero = ?, bairro = ?, complemento = ?, cep = ?, data_nascimento = ?
WHERE id = ?;
"""

SQL_DELETE_USUARIO = """
DELETE FROM usuario
WHERE id = ?;
"""
