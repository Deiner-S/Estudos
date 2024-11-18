from DAOabc import DAO

class DAOpessoa(DAO):
    pass    

    def create(self,obj):
        comando = f"""INSERT INTO {self.name} VALUES (:cpf, :nome, :nascimento, :oculos);"""        
        self.cursor.execute(comando, vars(obj))
        self.conexao.commit()
    
    def update(self):
        pass

    
    def delete(self):
        pass
    
