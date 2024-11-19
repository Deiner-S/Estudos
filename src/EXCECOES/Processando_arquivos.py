import os
import TratExcessao
import time

def processar_arquivos(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, "r", encoding='utf-8') as file_origem:
            conteudo = file_origem.read()
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except PermissionError:
        print("Você não tem permição para fazer esta operação")
    except Exception as e:
        print(f"Erro inesperado: {e}")


    try: 
        with open(arquivo_destino, "w", encoding='utf-8') as file_destino:
            file_destino.write("Cabeçalho: Conteúdo do arquivo")
            file_destino.write(conteudo)
            print(f"Conteudo escrito em {arquivo_destino}")
    except PermissionError:
        print(f"sem permição para escrever neste arquivo")
    except Exception as e:
        print(f"Erro inesperado: {e}")
def main():


    diretorio_trabalho = "Tratamento"
    TratExcessao.criar_diretorio(diretorio_trabalho)
    time.sleep(5)
    TratExcessao.criar_arquivo(os.path.join(diretorio_trabalho, "origem.txt"))
    time.sleep(5)
    TratExcessao.criar_arquivo(os.path.join(diretorio_trabalho, "destino.txt"))
    time.sleep(5)
    TratExcessao.escrever_arquivo(os.path.join(diretorio_trabalho, "origem.txt"), "La vem o pato pato aqui pato a cola")
    time.sleep(5)


    arquivo_origem = os.path.join(diretorio_trabalho, "origem.txt")
    arquivo_destino = os.path.join(diretorio_trabalho, "destino.txt")

    processar_arquivos(arquivo_origem, arquivo_destino)
    time.sleep(5)
    TratExcessao.remover_arquivo(os.path.join(diretorio_trabalho, "origem.txt"))
    time.sleep(5)
    TratExcessao.remover_arquivo(os.path.join(diretorio_trabalho, "destino.txt"))
    time.sleep(5)
    TratExcessao.excluir_diretorio(diretorio_trabalho)



if __name__ == "__main__":
    main()            