class Veiculo:
    def __init__(self, placa, ano, cor, motor, proprietario, marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.proprietario = proprietario
        self.marca = marca
        
    def get_placa(self):
        return self.placa
    def set_placa(self,new):
        self.placa= new
        
    def get_ano(self):
        return self.ano
    def set_ano(self,new):
        self.ano= new
        
    def get_cor(self):
        return self.cor
    def set_cor(self,new):
        self.cor= new
        
    def get_motor(self):
        return self.motor
    def set_motor(self,new):
        self.motor= new
    
    def get_propietario(self):
        return self.propietario
    def set_propietario(self,new):
        self.propietario= new
    
    def get_marca(self):
        return self.marca
    def set_marca(self,new):
        self.marca= new