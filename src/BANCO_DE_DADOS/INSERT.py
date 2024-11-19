#DAO.py
import sqlite3 as dao


def connect():
    conexao_dao = dao.connect("data_base.db")
    return conexao_dao

def INSERT(conexao_dao, pessoa):
    cursor = conexao_dao.cursor()
    comando = """INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
       VALUES ("10203407008","Maria","2000-05-27",True);"""
    cursor.execute(comando)
    conexao_dao.commit()

def INSERT_DINAMICO(conexao_dao, pessoa):
    cursor = conexao_dao.cursor()
    comando = """INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
       VALUES (?,?,?,?);"""    
    cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos))
    conexao_dao.commit()
    cursor.close()

def INSERT_DINAMICO_COM_DICIONARIO(conexao_dao, pessoa):
    
    cursor = conexao_dao.cursor()
    comando = """INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
       VALUES (:cpf, :nome, :nascimento, :oculos);"""    
    cursor.execute(comando, {"cpf" : pessoa.cpf, "nome": pessoa.nome, "nascimento" : pessoa.nascimento, "oculos" : pessoa.oculos})
    conexao_dao.commit()
    cursor.close()

def INSERT_DINAMICO_COM_VARS_OBJETO(conexao_dao, pessoa):
    cursor = conexao_dao.cursor()
    comando = """INSERT INTO Pessoa VALUES (:cpf, :nome, :nascimento, :oculos);"""        
    cursor.execute(comando, vars(pessoa))
    conexao_dao.commit()
    cursor.close()