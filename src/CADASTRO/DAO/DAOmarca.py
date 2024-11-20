from DAO.DAOabc import DAO

class DAOveiculo(DAO):
    #chave primaria
    primaryKey = "id"
    #nome da tabela
    tabela = "Marca"        
    
    
    def create(self,obj):
        try:
            comando = f"""INSERT INTO {self.tabela} VALUES (:id, :ome, :sigla);"""        
            self.cursor.execute(comando, vars(obj))
            self.conexao.commit()
            print("Cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
    
    
    
    
