import os

class Dir_util:
    def __init__(self):
        pass
    
    def criar(self,caminho):
        
        if not os.path.exists(caminho):
                
            try:    
                os.mkdir(caminho)
                print(f"Diretorio {caminho} criado com sucesso!")
            except PermissionError:
                print("Seu usuário não tem permissão para executar essa ação")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        else:
            print("Diretório já existe")
    
    def excluir(self,caminho):

        if os.path.exists(caminho):

            try:
                os.rmdir(caminho)
                print(f"Diretorio {caminho} removido com sucesso!")
            except PermissionError:
                print("Seu usuário não tem permissão para executar essa ação")
            except Exception as e:
                print(f"Erro inesperado: {e}")
        else:
            print("Diretório não encontrado")
        
   