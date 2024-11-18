from abc import ABC, abstractmethod
import sqlite3 as conexao
#Create
#Read
#Update
#Delete
class DAO(ABC):
    def __init__(self):
        self.conexao = conexao.connect("data.bd") 
        self.cursor = self.conexao.cursor()
        self.name = ""
    @abstractmethod
    def create(self,obj):
        pass

    
    def read(self,cpf):
        comando = f"SELECT * FROM {self.name} WHERE cpf = '{cpf}' "
        return self.cursor.execute(comando)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod 
    def delete(self):
        pass