#DAO.py
import sqlite3 as dao


def connect():
    conexao_dao = dao.connect("data_base.db")
    return conexao_dao

def insert(conexao_dao, pessoa):
    cursor = conexao_dao.cursor()
    comando = """INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
       VALUES (?,?,?,?);"""    
    cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos))
    conexao_dao.commit()
    cursor.close()

def insert_dict(conexao_dao, pessoa):
    
    cursor = conexao_dao.cursor()
    comando = """INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
       VALUES (:cpf, :nome, :nascimento, :oculos);"""    
    cursor.execute(comando, {"cpf" : pessoa.cpf, "nome": pessoa.nome, "nascimento" : pessoa.nascimento, "oculos" : pessoa.oculos})
    conexao_dao.commit()
    cursor.close()
