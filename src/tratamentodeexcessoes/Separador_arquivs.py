from Util_dir import Util_dir
from Util_file import Util_file
import os



'''Função para separar arquivos de acordo com suas extenções'''

def separador(origem):
    file = Util_file()
    for arquivo in os.listdir(origem):
        caminho_arquivo = os.path.join(origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            extencao = arquivo.split(".")[-1].lower()
            if extencao in ['pdf','txt','jpg']:
                destino = os.path.join(origem, extencao)
                file.mover(caminho_arquivo, destino)
            
            
            
        

def main():
    dir = Util_dir()
    file = Util_file()
    
    origem = "Separador"        
    dir.criar(origem)
    
    for i in ['txt','jpg','pdf']:        
        dir.criar(os.path.join(origem, i))
        file.criar(os.path.join(origem, "Teste."+i))
        
    separador(origem)    
    
if __name__ == "__main__":
    main()
