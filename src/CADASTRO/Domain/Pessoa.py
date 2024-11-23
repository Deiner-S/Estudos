class Pessoa:
    def __init__(self,cpf, nome, nascimento, oculos):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos
    
    def getCPF(self):
        return self.cpf
    def setCPF(self, new):
        self.cpf = new
    
    def getNome(self):
        return self.nome
    def setNome(self, new):
        self.nome = new
    
    def getNascimento(self):
        return self.nascimento
    def setNascimento(self, new):
        self.nascimento = new
    
    def getOculos(self):
        return self.oculos
    def setOculos(self, new):
        self.oculos = new
        
    def too_string(self):
        return f""" Nome: {self.nome}\n
                    Cpf: {self.cpf}\n
                    Data de nascimento:{self.nascimento}\n
                    Oculos: {self.oculos}\n
                    """