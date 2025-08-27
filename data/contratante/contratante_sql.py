SQL_CREATE_TABLE_CONTRATANTE = """
CREATE TABLE IF NOT EXISTS contratante (
    id INTEGER PRIMARY KEY,
    nota FLOAT,
    numero_contratacoes,
    FOREIGN KEY (id) REFERENCES usuario(id)
);
"""

SQL_INSERT_CONTRATANTE = """
INSERT INTO contratante (id, nota, numero_contratacoes) 
VALUES (?, ?, ?);
"""

SQL_SELECT_RANGE_CONTRATANTE = """
SELECT c.id, c.nota, c.numero_contratacoes,
       u.nome || ' ' || u.sobrenome AS nome_completo, u.nome_usuario AS login_usuario, u.senha, u.email,
       u.cpf, u.telefone, u.genero, u.logradouro, u.numero AS numero_endereco, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
       u.id_cidade, cida.nome AS nome_cidade, cida.id_uf, uf.nome AS nome_uf
FROM contratante c
JOIN usuario u ON c.id = u.id
JOIN cidade cida ON u.id_cidade = cida.id
JOIN uf ON cida.id_uf = uf.id
ORDER BY c.id
LIMIT ? OFFSET ?;
"""

SQL_SELECT_RANGE_BUSCA_CONTRATANTE = """
SELECT c.id, c.nota, c.numero_contratacoes,
      u.nome || ' ' || u.sobrenome AS nome_completo, u.nome_usuario AS login_usuario, u.senha, u.email,
       u.cpf, u.telefone, u.genero, u.logradouro, u.numero AS numero_endereco, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
       u.id_cidade, cida.nome AS nome_cidade, cida.id_uf, uf.nome AS nome_uf
FROM contratante c
JOIN usuario u ON c.id = u.id
JOIN cidade cida ON u.id_cidade = cida.id
JOIN uf ON cida.id_uf = uf.id
WHERE u.nome LIKE ? OR u.sobrenome LIKE ?
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""

SQL_SELECT_CONTRATANTE_BY_ID = """
SELECT c.id, c.nota, c.numero_contratacoes,
       u.nome || ' ' || u.sobrenome AS nome_completo, u.nome_usuario AS login_usuario, u.senha, u.email,
       u.cpf, u.telefone, u.genero, u.logradouro, u.numero AS numero_endereco, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
       u.id_cidade, cida.nome AS nome_cidade, cida.id_uf, uf.nome AS nome_uf
FROM contratante c
JOIN usuario u ON c.id = u.id
JOIN cidade cida ON u.id_cidade = cida.id
JOIN uf ON cida.id_uf = uf.id
WHERE c.id = ?;
"""

SQL_SELECT_COUNT_CONTRATANTE = """
SELECT COUNT(*) FROM contratante;
"""

SQL_SELECT_CONTRATANTE = """
SELECT c.id, c.nota, c.numero_contratacoes,
       u.nome || ' ' || u.sobrenome AS nome_completo, u.nome_usuario AS login_usuario, u.senha, u.email,
       u.cpf, u.telefone, u.genero, u.logradouro, u.numero AS numero_endereco, u.bairro, u.complemento, u.cep, u.data_nascimento, u.verificado,
       u.id_cidade, cida.nome AS nome_cidade, cida.id_uf, uf.nome AS nome_uf
FROM contratante c
JOIN usuario u ON c.id = u.id
JOIN cidade cida ON u.id_cidade = cida.id
JOIN uf ON cida.id_uf = uf.id
ORDER BY u.nome;
"""

SQL_UPDATE_CONTRATANTE = """
UPDATE contratante
SET nota = ?, numero_contratacoes = ?
WHERE id = ?;
"""

SQL_DELETE_CONTRATANTE = """
DELETE FROM contratante
WHERE id = ?;
"""