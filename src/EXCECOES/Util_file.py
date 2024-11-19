import os
import shutil


class Util_file:
   
    def criar(self,caminho):       
        try:
            with open(caminho,"w", encoding='utf-8'):
                print("arquivo criado com sucesso")
                return True       
        except PermissionError:
            print("Seu usuário não tem permição para essa ação")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
            
 
    
    def sobrescrever(self, caminho, conteudo):
        try:
            with open(caminho, "w", encoding='utf-8') as file:
                file.write(conteudo)
                print("Arquivo sobrescrito com sucesso")
                return True
        except PermissionError:
            print("Seu usuário não tem permição para essa ação")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
        
        
            
    def escrever(selfe, caminho, conteudo):
        try:
            with open(caminho, "a", encoding='utf-8') as file:
                file.writelines(conteudo)
                print("Conteudo adicionado com sucesso")
                return True
        except PermissionError:
            print("Seu usuário não tem permição para essa ação")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
            
            
            
            
    def excluir(self,caminho):
        if os.path.exists(caminho):
            try:
                os.remove(caminho)
                print(f"arquivo {caminho} excluido com sucesso!")
                return True
            except PermissionError:
                print("Seu usuário não tem permição para essa ação")
                return False
            except Exception as e:
                print(f"Erro inesperado: {e}")
                return False
        else:
            print("arquivo não existe ou já foi deletado")
            return False
            
            
            
    
    def renomear(self,caminho,novo_caminho):
        if os.path.exists(caminho):
            if not os.path.exists(novo_caminho):
                try:
                    os.rename(caminho, novo_caminho)
                    print("Arquivo renomeado com sucesso!")
                    return True
                except PermissionError:
                    print("Seu usuário não tem permição para essa ação")
                    return False
                except Exception as e:
                    print(f"Erro inesperado: {e}")
                    return False
            else:
                print(f"já existe um arquivo com este nome {novo_caminho}")    
                return False
        else:
            print("Arquivo não encontrado")
            return False
        
        
        
        
    def ler(self, caminho):
        if os.path.exists(caminho):
            try: 
                with open(caminho, "r", encoding='utf-8') as file:
                    file_read = file.read()
                    print("leitura relaizada!")
                    return file_read
            except PermissionError:
                print("Seu usuário não tem permição para essa ação")
                return False
            except Exception as e:
                print(f"Erro inesperado: {e}")
                return False    
        else:
            print("Arquivo não encontrado")
            return False
        
        
            
            
    def mover(self, origem, destino):
        try:
            shutil.move(origem,destino)
            print(f"arquivo movido para {destino}")
            return True
        except PermissionError:
            print("Seu usuário não tem permição para essa ação")
            return False
        except Exception as e:
             print(f"Erro inesperado: {e}")
             return False    