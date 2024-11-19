from DAO.DAOabc import DAO
import sqlite3 as conexao

class DAOpessoa(DAO):
    def __init__(self):
        super().__init__()

    def create(self,obj):
        try:
            comando = f"""INSERT INTO Pessoa VALUES (:cpf, :nome, :nascimento, :oculos);"""        
            self.cursor.execute(comando, vars(obj))
            self.conexao.commit()
            return True
        except conexao.DatabaseError:
            print("Erro de conexão com banco de dados")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    
    
    
