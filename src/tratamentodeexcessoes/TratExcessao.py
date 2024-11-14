import os
import time

def criar_arquivo(nome):
    try:
        with open(nome, "w", encoding='utf-8') as arquivo:
            arquivo.write("sim eu sei\nde muita coisa\nmas eu minto\npara não saberem\nque sei")
            print("arquivo criado com sucesso")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def remover_arquivo(arquivo):
    try:
        os.remove(arquivo)
        print(f"arquivo {arquivo} removido com sucesso")
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado")
    except IsADirectoryError:
        print("o que você está tentando excluir não é um arquivo e sim um diretório")
    except Exception as e:
        print(f"erro insperado: {e}") 
        
        
def renomear_arquivo(arquivo, novo_nome):
    try:
        os.rename(arquivo, novo_nome)
        print(f"arquivo {arquivo} renomeado para {novo_nome}")
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
def criar_diretorio(nome_dir):
    try:
        os.mkdir(nome_dir)
        print("Diretório criado com sucesso!")
    except PermissionError:
        print("Você não tem permissão para criar diretórios neste local")
    except FileExistsError:
        print("O diretorio que você está tentando criar já existe")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def escrever_arquivo(arquivo, conteudo):

    try:
        with open(arquivo, "a", encoding='utf-8') as e_arquivo:
            e_arquivo.writelines(conteudo)
        return print(f"Conteudo adicionado com sucesso")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        


def excluir_diretorio(nome_dir):
    try:
        os.rmdir(nome_dir)
        print("Diretório excluido com sucesso")
    except PermissionError:
        print("Você não tem permissão para excluir diretórios neste local")
    except FileNotFoundError:
        print(f"Arquivo {nome_dir} não foi encontrado")
    except Exception as e:
        print(f"Erro inesperado: {e}")
def scandir(caminho):
    try:
        with os.scandir(caminho) as list_dir:
            for i in list_dir:
                print(i.name)
    except Exception as e:
        print(f"Erro inesperado: {e}")        
        
def main():
    nome_dir = "Arquivos"
    
    criar_diretorio(nome_dir)
    time.sleep(5)
    
    '''print(f"É um diretório ? {os.DirEntry.is_dir(nome_dir)}")
    print(f"É um arquivo ?{os.DirEntry.is_file(nome_dir)}")
    print(f"Status: {os.DirEntry.stat(nome_dir)}")'''
    
    nome_arquivo = f"{nome_dir}/arquivo.txt"
    novo_nome = f"{nome_dir}/novo_arquivo.txt"
    
    criar_arquivo(nome_arquivo)
    time.sleep(5)
    renomear_arquivo(nome_arquivo, novo_nome)   
    
    '''print(f"É um diretório ? {os.DirEntry.is_dir(novo_nome)}")
    print(f"É um arquivo ?{os.DirEntry.is_file(novo_nome)}")
    print(f"Status: {os.DirEntry.stat(novo_nome)}")'''
    
    scandir(nome_dir)
    time.sleep(5)
    remover_arquivo(novo_nome)    
    time.sleep(5)  
    excluir_diretorio(nome_dir)
    
    
if __name__ == "__main__":
    main()