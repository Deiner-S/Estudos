
class Marca():
    def __init__(self, id, ome, sigla):
        self.id = id
        self.ome = ome
        self.sigla = sigla



    def get_id(self):
       return self.id
    def set_id(self,new):
       self.id = new
    
    def get_ome(self):
       return self.ome
    def set_ome(self,new):
       self.ome = new
    
    def get_sigla(self):
       return self.sigla
    def set_sigla(self,new):
       self.sigla = new
        