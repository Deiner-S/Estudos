from Pessoa import Pessoa
from DAOpessoa import DAOpessoa

def main():
    pessoa = Pessoa('98765432100', 'Maria', '1985-05-15', 0)
    dao = DAOpessoa()
    dao.create(pessoa)
    dao.cursor.close()
    dao.conexao.close()    

if __name__ == "__main__":
    main()