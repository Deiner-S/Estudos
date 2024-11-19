#Trabalahndo com padronização de textos

"""
Dicionário:

--PALAVRAS RESERVADAS E FUNÇÕES--
def --> definir funções
main() --> função principal responssável pela execução e chamada de outros objetos e funções e métodos estáticos. 
print()  --> imprime no console variaveis strings documentos 
while  --> loop de repetiçãowhile
input()  --> função que permite a entrada de dados pelo console
break  --> interrompe execução em seu escopo
with as --> premite que um arquivo seja aberto com uma variavel temporária e este arquivo e fechado automaticamente após uso sem necessidade do .close()
open()  --> arbe um arquivo.
for in  --> loop de repetição for

------------------------

--FUNÇÕES DO OBJETO STRING--
.lower() --> passa uma string para minusculo
.strip() --> remove espaçamentos finais e iniciais de uma string
.upper() --> passa uma string para maiusculo

----------------------------

--FUNÇÕES DO OBJETO ARQUIVO-
.append() --> adiciona itens à um arquivo sem sobrescrever os existentes
.write() --> escreve em um arquivo

-----------------------------
"""

def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == "sair": # lower utilizado para passar string para minusculo
            break
        frases.append(entrada) # append -> utilizado para adicionar dados ao arquivo sem sobrescrever os inseridos anteriormente. 
    
    with open("meu_arquivo.txt", "w") as arquivo: # forma de abrir um arquvio de modo que ao terminar a manipução ele seja fechado automaticamente
        for frase in frases:
            arquivo.write(frase + "\n")
    
    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open("meu_arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper())  # Exemplo de manipulação: converter para maiúsculas
    
    with open("meu_arquivo.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    
    print("O arquivo foi sobrescrito com os dados modificados.")
 
if __name__ == "__main__":
    main()
            
    