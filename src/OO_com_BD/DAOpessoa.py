from DAOabc import DAO

class DAOpessoa(DAO):
    def __init__(self):
        super().__init__()

    self.name = "Pessoa" # type: ignore

    def create(self,obj):
        comando = f"""INSERT INTO {self.name} VALUES (:cpf, :nome, :nascimento, :oculos);"""        
        self.cursor.execute(comando, vars(obj))
        self.conexao.commit()
    
    def update(self):
        pass

    
    def delete(self):
        pass
    
