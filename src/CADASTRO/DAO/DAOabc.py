
#Pacote DAO

from abc import ABC, abstractmethod
import sqlite3 as conexao
#
#Create
#Read
#Update
#Delete
#
class DAO(ABC):
    def __init__(self):
        self.conexao = conexao.connect("data.bd") 
        self.cursor = self.conexao.cursor()        
    #   
    #
    #
    # 
    @abstractmethod
    def create(self,obj):
        pass
    #   
    #
    #
    #  
    def read(self,cod,table):
        try:
            comando = f"SELECT * FROM {table} WHERE cpf = '{cod}' "
            self.cursor.execute(comando)
            return self.cursor.fetchall()
        except conexao.DatabaseError:
            print("Erro de conexão com banco de dados")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    #   
    #
    #
    #     
    def update(self,atributo,table):
        try:
            comando = f"""UPDATE {table} SET {atributo}"""
            print("Dados atualizados com sucesso!")
            self.cursor.execute(comando)
            self.conexao.commit()
            return True
        except conexao.DatabaseError:
            print("Erro de conexão com banco de dados")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
    #   
    #
    #
    # 
    def delete(self):
        comando = f""""""