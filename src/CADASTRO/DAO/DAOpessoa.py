from DAO.DAOabc import DAO

class DAOpessoa(DAO):
    primaryKey = "cpf"
    tabela = "Pessoa"        
    
    def create(self,obj):
        try:
            comando = f"""INSERT INTO Pessoa VALUES (:cpf, :nome, :nascimento, :oculos);"""        
            self.cursor.execute(comando, vars(obj))
            self.conexao.commit()
            print("Cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
    
    
    
    
