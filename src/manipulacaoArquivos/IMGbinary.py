"""
MANIPULAÇÃO DE ARQUIVOS DE DADOS BINÁRIOS

Normalmente trabalhamos com esse tipo de dados quando manipulamos
imagens e videos ou com operações de leitura e escrita em baixo nível

FLUXO DE TRABALHO

*Carregar imagem(open)
*Transformar os dados em array(numpy)
*Escrever em um arquivo cópia
*Redimensionar o array
*Inverter os dados

BIBLIOTECAS UTILIZADAS
* PIL --> utilizado para fazer diverças operações com imagem
* numpy --> bibliotéca numérica poderosa.
"""
#importando bibliotecas
from PIL import Image
import numpy as np

def main():
    #Carregar imagem
    img = Image.open("blue-valorant-logo.jpg")
    
    #Converter imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()
    
    print("/n", img_data.shape, "/n")
     
    #Salvar os dados binários em um arquivo
    with open("original_img.bin", "wb") as file:
        file.write(binary_data)
     
    #Copiar o arquivo binário
    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()
     
    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)
     
    '''manipulando dados do arquivo binário copy_img.bin
    inverter os bytes'''
     
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())
         
    with open("copy_img.bin", "wb") as file:
        file.write(data)
        
    #Carregar e mostrar a imagem manipulada
    modified_data = np.frombuffer(data,dtype=np.uint8).reshape(img_data.shape);
    
    #inverter todos os bytes
    modified_data = np.fliplr(modified_data)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()     
        
    
if __name__ == "__main__":
    main()