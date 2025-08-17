SQL_CREATE_TABLE_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL CHECK(LENGTH(nome) <= 100),
    sobrenome TEXT NOT NULL CHECK(LENGTH(sobrenome) <= 100),
    nome_usuario TEXT NOT NULL CHECK(LENGTH(nome_usuario) <= 30),
    senha TEXT NOT NULL CHECK(LENGTH(senha) <= 20),
    email TEXT NOT NULL CHECK(LENGTH(email) <= 254),
    cpf TEXT UNIQUE CHECK(LENGTH(cpf) == 11),
    telefone TEXT CHECK(LENGTH(telefone) <= 11),
    genero TEXT CHECK(genero IN ('Masculino', 'Feminino', 'Outro', 'Prefiro não informar')),
    logradouro TEXT CHECK(LENGTH(logradouro) <= 150),
    id_cidade INTEGER,
    numero INTEGER CHECK(numero > 0),
    bairro TEXT CHECK(LENGTH(bairro) <= 50),
    complemento TEXT CHECK(LENGTH(complemento) <= 200),
    cep TEXT CHECK(LENGTH(cep) == 8),
    data_nascimento DATE,
    verificado BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_cidade) REFERENCES cidade(id)
);
"""

SQL_INSERT_USUARIO = """
INSERT INTO usuario (id_cidade, nome, sobrenome, nome_usuario, senha, email, cpf, telefone, genero, logradouro, numero, bairro, complemento, cep, data_nascimento, verificado) 
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
"""

SQL_SELECT_RANGE_USUARIO = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY u.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_USUARIO_NOME = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.nome LIKE ? or u.sobrenome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_USUARIO_NOMECOMPLETO = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.nome LIKE ? AND u.sobrenome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_USUARIO_EMAIL = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.email LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_USUARIO_BY_ID = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
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
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY u.nome;
"""

SQL_UPDATE_USUARIO = """
UPDATE usuario
SET id_cidade = ?, nome = ?, sobrenome = ?, nome_usuario = ?, senha = ?, email = ?, cpf = ?, telefone = ?, genero = ?, logradouro = ?, numero = ?, bairro = ?, complemento = ?, cep = ?, data_nascimento = ?, verificado = ?,
WHERE id = ?;
"""

SQL_DELETE_USUARIO = """
DELETE FROM usuario
WHERE id = ?;
"""
