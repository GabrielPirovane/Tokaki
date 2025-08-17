from dataclasses import dataclass
from data.cidade.cidade_model import Cidade

@dataclass
class Usuario:
    id: int
    id_cidade: Cidade
    nome: str
    sobrenome: str
    nome_usuario: str
    senha: str
    email: str
    cpf: str
    telefone: str
    genero: str
    logradouro: str
    numero: int
    bairro: str
    complemento: str | None
    cep: str
    data_nascimento: str
    
