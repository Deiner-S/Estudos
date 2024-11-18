from abc import ABC, abstractmethod
import sqlite3 as conexao
#Create
#Read
#Update
#Delete
class DAO(ABC):
    def __init__(self,name):
        self.conexao = conexao.connect("./data_base.db") 
        self.cursor = self.conexao.cursor()
        self.name = name
    @abstractmethod
    def create(self,obj):
        pass

    
    def read(self,cod):
        comando = f"SELECT * FROM {self.name} WHERE cpf = '{cod}' "
        self.cursor.execute(comando)        
        return self.cursor.fetchall()

    @abstractmethod
    def update(self):
        pass

    @abstractmethod 
    def delete(self):
        pass