import os

class Util_dir:
    
    
    def criar(self,diretorio):
        
        if not os.path.exists(diretorio):
                
            try:    
                os.mkdir(diretorio)
                print(f"Diretorio {diretorio} criado com sucesso!")
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
    
    def renomear(self,caminho_antigo,caminho_novo ):
                
        if os.path.exists(caminho_antigo):

            try:
                os.rename(caminho_antigo,caminho_novo)
                print(f"Diretorio {caminho_antigo} removido com sucesso!")
            except PermissionError:
                print("Seu usuário não tem permissão para executar essa ação")
            except Exception as e:
                print(f"Erro inesperado: {e}")
        else:
            print("Diretório não encontrado")
   