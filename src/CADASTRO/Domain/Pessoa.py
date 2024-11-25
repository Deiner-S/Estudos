class Pessoa:
    def __init__(self,cpf, nome,endereco,data_cadastro,ultima_compra ):
        self.cpf = cpf
        self.nome = nome
        self.endereco =endereco 
        self.data_cadastro = data_cadastro
        self.ultima_compra = ultima_compra 
    
    def getCPF(self):
        return self.cpf
    def setCPF(self, new):
        self.cpf = new
    
    def getNome(self):
        return self.nome
    def setNome(self, new):
        self.nome = new
    
    def get_endereco(self):
        return self.endereco
    def set_endereco(self, new):
        self.endereco = new
    
    def get_data_cadastro(self):
        return self.data_cadastro
    def set_data_cadastro(self, new):
        self.data_cadastro = new
    
    def get_ultima_compra(self):
        return self.ultima_compra
    def set_ultima_compra(self, new):
        self.ultima_compra = new
    
    