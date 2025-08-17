from data.util import get_connection
from data.uf.uf_repo import UfRepo
from data.cidade.cidade_sql import SQL_INSERT_CIDADE
import sqlite3
import json


def open_json(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            return json.load(file)
    except Exception as e:
        raise Exception(f"Erro ao abrir o arquivo JSON: {e}")

def insert_cidades():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            json_cidades = open_json('inserts/cidades.json')
            json_estados = open_json('inserts/estados.json')
            values = list()
            for cidade in json_cidades:
                #Acha o nome do estado pelo id do json importado no github
                nome_uf = next((e['nome'] for e in json_estados if e['codigo_uf'] == cidade["codigo_uf"]), None)
                id_uf = get_id_uf(nome_uf)
                values.append((cidade['nome'], id_uf))
            cursor.executemany(
                SQL_INSERT_CIDADE,
                values
            )
            return cursor.rowcount 
    except sqlite3.IntegrityError as e:
        print("Erro de integridade:", e)
        return 0


def get_id_uf(nome_uf: str) -> int:
    uf_repo = UfRepo('dados.db')
    uf = uf_repo.get_by_name(nome_uf)
    return uf.id
    
    
if __name__ == "__main__":
    print("Cidades inseridas" if insert_cidades() else "Erro ao inserir cidades")