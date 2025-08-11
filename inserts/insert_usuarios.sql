INSERT INTO usuario (
    id_cidade, nome, nome_usuario, senha, email, cpf, telefone,
    genero, logradouro, numero, bairro, complemento, cep, data_nascimento
) VALUES
(1, 'João Silva', 'joaos', '12345678', 'joao.silva@example.com', '11111111111', '27999990001',
 'Masculino', 'Rua das Flores', 10, 'Centro', 'Apto 101', '29000000', '2000-05-15'),

(1, 'Maria Oliveira', 'mariao', '87654321', 'maria.oliveira@example.com', '22222222222', '27999990002',
 'Feminino', 'Avenida Brasil', 200, 'Jardim América', NULL, '29010000', '1998-10-20'),

(1, 'Carlos Pereira', 'carlosp', 'senha123', 'carlos.pereira@example.com', '33333333333', '27999990003',
 'Masculino', 'Rua Vitória', 55, 'Praia do Canto', 'Casa', '29020000', '1995-03-08'),

(1, 'Ana Souza', 'anas', 'minhasenha', 'ana.souza@example.com', '44444444444', '27999990004',
 'Feminino', 'Travessa das Palmeiras', 88, 'Parque Residencial', NULL, '29030000', '2002-07-12'),

(1, 'Pedro Lima', 'pedrol', 'abc12345', 'pedro.lima@example.com', '55555555555', '27999990005',
 'Masculino', 'Rua Sete', 12, 'Centro', 'Fundos', '29040000', '1999-12-01');
