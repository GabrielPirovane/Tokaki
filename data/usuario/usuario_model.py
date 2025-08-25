from dataclasses import dataclass
from data.cidade.cidade_model import Cidade

@dataclass
class Usuario:
    id: int
    id_cidade: Cidade | None
    nome: str
    sobrenome: str
    nome_usuario: str
    senha: str
    email: str
    cpf: str | None
    telefone: str | None
    genero: str | None
    logradouro: str | None
    numero: int | None
    bairro: str | None
    complemento: str | None
    cep: str | None
    data_nascimento: str | None
    verificado: bool
    tipo_usuario: str | None
    
