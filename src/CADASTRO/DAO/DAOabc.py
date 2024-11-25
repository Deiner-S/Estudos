
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
    primaryKey = ""
    tabela = ""    
    conexao = conexao.connect("src\CADASTRO\DAO\data.db", detect_types=conexao.PARSE_DECLTYPES) 
    cursor = conexao.cursor()
                    
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
    def read(self,cod):
        try:
            comando = f"""SELECT * FROM {self.tabela} WHERE {self.primaryKey} = '{cod}' """
            self.cursor.execute(comando)
            return self.cursor.fetchall()        
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    #   
    #
    #
    #     
    def update(self,chave,coluna,update):
        try:
            comando = f"""UPDATE {self.tabela} SET {coluna}= ? WHERE {self.primaryKey}={chave};"""           
            self.cursor.execute(comando, (update,))
            self.conexao.commit()
            print("Dados atualizados com sucesso!")
            return True            
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
    #   
    #
    #
    # 
    def delete(self,cpf):
        self.conexao.execute("PRAGMA foreign_keys = on")
        try:
            comando = f'''DELETE FROM {self.tabela} WHERE {self.primaryKey}= {cpf};'''
            self.cursor.execute(comando)
            self.conexao.commit()
            print("Cadastro removido")
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False