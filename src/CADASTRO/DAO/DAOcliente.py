from DAO.DAOabc import DAO

class DAOcliente(DAO):
    primaryKey = "cpf"
    tabela = "Cliente"        
    
    def create(self,obj):
        try:
            comando = f"""INSERT INTO Pessoa VALUES (:cpf, :nome, :endereco, :data_cadastro, :utima_compra);"""        
            self.cursor.execute(comando, vars(obj))
            self.conexao.commit()
            print("Cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
    
    
    
    
