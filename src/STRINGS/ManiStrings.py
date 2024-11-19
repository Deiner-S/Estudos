import os
'''
Funções de manipulação de Strings

Strip()
Split()
Join()
Count()
'''
def cont_linhas():
    print('Representação do arquivo antes de utilizar Strip()')
    with open("texto.txt", encoding='utf-8') as arquivo:
        contador = 0
        for linha in arquivo:
            print(repr(linha))
            if linha:
                contador +=1
                   
    return contador

def cont_linhas_strip():
    print('Representação do arquivo após utilizar Strip()')
    with open("texto.txt", encoding='utf-8') as arquivo:
        contador = 0
        for linha in arquivo:
            linha_limpa = linha.strip()
            print(repr(linha_limpa))
            if linha_limpa:
                contador +=1
                   
    return contador
def count_elementos():
    with open("texto.txt", encoding='utf-8') as arquivo:
        texto = arquivo.read()
        cont = texto.count(",")
        return f"total de virgulas: {cont}" 
    
def criar_arquivo():
    with open("texto.txt", "w", encoding='utf-8') as arquivo:
        arquivo.write("Ola, mundo!\n\nOla, UFU.\n\nOlá, Alun")
        
        return "arquivo criado"  
        
def tiposde_read():
    arquivo = open("texto.txt", "r", encoding='utf-8')
    
    #conteudo = arquivo.read() # leitura do arquivo inteiro / retorna uma string de todo o arquivo
    conteudo = arquivo.readline() # leitura somente de uma lina / retorna uma string da linha 
    #conteudo = arquivo.readlines() # retorna uma lista do arquivo todo
    
    print("tipo de dado: ", type(conteudo))
    
    print("\n conteudo retornado pelo read: ")
    
    print(conteudo, '\n')
    print(repr(conteudo),'\n')   
    
    arquivo.close()

def metodo_split():
    frase1 = "info1, info2, info3, info4, info5, info6"
    frazes_separadas = frase1.split(",")    
    print(frazes_separadas)
    
def formatar():
    #utilizado para alterar texto em tempo de execução
    idade = 24
    status = "casado"
    conjugue = "Rayane"
    salario = 20000,2222222   
    
    frase1 = "Deiner tem {} anos de idade e também é {} com a {} e recebe um salário de {}".format(idade,status,conjugue,)
    frase2 = f"Deiner tem {idade} anos de idade e também é {status} com a {conjugue}"
    
    return f"{frase1}\n{frase2}"

def main():
    
    print(criar_arquivo())
    
    tiposde_read()
            
    print(cont_linhas())
    
    print(cont_linhas_strip())
    
    print(count_elementos())
    
    metodo_split()
    
    print(formatar())
    
    
if __name__ == "__main__":
    main()
    
    
