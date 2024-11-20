from Domain.Pessoa import Pessoa
from DAO.DAOpessoa import DAOpessoa
import time

def main():
    pessoa = Pessoa('70124673120', 'Deiner Rodrigues de Souza', '2000-08-14', 0)
    dao = DAOpessoa()
    dao.create(pessoa)
    time.sleep(5)
    print(dao.read("70124673120"))
    time.sleep(5)
    dao.update("70124673120","nome","Hisoka")
    time.sleep(5)
    dao.delete("70124673120")
    time.sleep(5)
    print(dao.read("70124673120"))
    dao.cursor.close()
    dao.conexao.close() 
    
    
    
    
   
if __name__ == "__main__":
    main()