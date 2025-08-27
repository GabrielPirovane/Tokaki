SQL_CREATE_TABLE_USUARIO = """
-- Criação da tabela usuario
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL CHECK(LENGTH(nome) <= 100),
    sobrenome TEXT NOT NULL CHECK(LENGTH(sobrenome) <= 100),
    nome_usuario TEXT NOT NULL CHECK(LENGTH(nome_usuario) <= 20),
    senha TEXT NOT NULL CHECK(LENGTH(senha) <= 100),
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
<<<<<<< HEAD
    tipo_usuario TEXT CHECK(tipo_usuario IN ('musico', 'contratante')),
    token_redefinicao TEXT DEFAULT NULL,
    token_expiracao DATETIME DEFAULT NULL,
=======
    tipo_usuario TEXT CHECK(tipo_usuario IN ('musico', 'contratante', 'administrador')),
>>>>>>> d13389b6294c30561cf60de826eaf635bc504ffb
    FOREIGN KEY (id_cidade) REFERENCES cidade(id)
);
"""

SQL_INSERT_USUARIO = """
INSERT INTO usuario (id_cidade, nome, sobrenome, nome_usuario, senha, email, cpf, telefone, genero, logradouro, numero, bairro, complemento, cep, data_nascimento, verificado, tipo_usuario) 
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
"""

SQL_SELECT_RANGE_USUARIO = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
ORDER BY u.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_USUARIO_NOME = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario,
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
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE LOWER(TRIM(u.nome)) LIKE LOWER(?) AND LOWER(TRIM(u.sobrenome)) LIKE LOWER(?)
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_USUARIO_EMAIL = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario,
c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
JOIN cidade c ON u.id_cidade = c.id
JOIN uf ON c.id_uf = uf.id
WHERE u.email LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_USUARIO_BY_NOMEUSUARIO = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
       u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario,
       c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
LEFT JOIN cidade c ON u.id_cidade = c.id
LEFT JOIN uf ON c.id_uf = uf.id
WHERE u.nome_usuario = ?;
"""

SQL_GET_SENHA_POR_EMAIL = """
SELECT senha
FROM usuario
WHERE email = ?
"""

SQL_GET_DADOS_POR_EMAIL = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
       u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario, c.id_uf, uf.nome AS nome_uf
FROM usuario u
LEFT JOIN cidade c ON u.id_cidade = c.id
LEFT JOIN uf ON c.id_uf = uf.id
WHERE u.email = ?
"""

SQL_SELECT_USUARIO_BY_ID = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
       u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario,
       c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
LEFT JOIN cidade c ON u.id_cidade = c.id
LEFT JOIN uf ON c.id_uf = uf.id
WHERE u.id = ?;
"""

SQL_SELECT_COUNT_USUARIO = """
SELECT COUNT(*) FROM usuario;
"""

SQL_SELECT_USUARIO = """
SELECT u.id, u.id_cidade, u.nome, u.sobrenome, u.nome_usuario, u.senha, u.email, u.cpf, u.telefone, u.genero,
       u.logradouro, u.numero, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado, u.tipo_usuario,
       c.nome AS nome_cidade, c.id_uf, uf.nome AS nome_uf
FROM usuario u
LEFT JOIN cidade c ON u.id_cidade = c.id
LEFT JOIN uf ON c.id_uf = uf.id
ORDER BY u.nome;
"""

SQL_SELECT_BY_TOKEN = """
SELECT id, email
FROM usuario
WHERE token_redefinicao = ?
  AND token_expiracao > CURRENT_TIMESTAMP;
"""


SQL_UPDATE_USUARIO = """
UPDATE usuario
SET id_cidade = ?, nome = ?, sobrenome = ?, nome_usuario = ?, senha = ?, email = ?, cpf = ?, telefone = ?, genero = ?, logradouro = ?, numero = ?, bairro = ?, complemento = ?, cep = ?, data_nascimento = ?, verificado = ?, tipo_usuario = ?
WHERE id = ?;
"""

SQL_UPDATE_SENHA = """
UPDATE usuario
SET senha = ?
WHERE id = ?;
"""



SQL_UPDATE_TOKEN = """
UPDATE usuario
SET token_redefinicao = ?, token_expiracao = ?
WHERE email = ?;
"""


SQL_SELECT_BY_TOKEN = """
SELECT id, email
FROM usuario
WHERE token_redefinicao = ?
  AND token_expiracao > CURRENT_TIMESTAMP;
"""


SQL_CLEAR_TOKEN = """
UPDATE usuario
SET token_redefinicao = NULL, token_expiracao = NULL
WHERE id = ?;
"""



SQL_DELETE_USUARIO = """
DELETE FROM usuario
WHERE id = ?;
"""
