from DAO.DAOabc import DAO

class DAOveiculo(DAO):
    #chave primaria
    primaryKey = "placa"
    #nome da tabela
    tabela = "Veiculo"        
    
    
    def create(self,obj):
        try:
            comando = f"""INSERT INTO {self.tabela} VALUES (:placa, :ano, :cor, :motor, :propietario, :marca);"""        
            self.cursor.execute(comando, vars(obj))
            self.conexao.commit()
            print("Cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
    
    
    
    
