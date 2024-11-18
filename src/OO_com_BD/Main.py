from Pessoa import Pessoa
from DAOpessoa import DAOpessoa

def main():

    dao = DAOpessoa("Pessoa")
    #dao.create(pessoa3)
    ana = dao.read("98765432102")
    obj_ana = Pessoa(*ana[0])
    print(type(ana[0]))    
    dao.cursor.close()
    dao.conexao.close()
    
       

if __name__ == "__main__":
    main()