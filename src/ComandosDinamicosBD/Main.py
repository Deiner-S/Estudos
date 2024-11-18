#Main.py
import DAO as dao
from Pessoa import Pessoa

def main():
    #Construindo Objeto pessoa
    pessoa = Pessoa(10304500099, 'Maria', '1999-07-12', False)
    #iniciando conexão com o banco
    conexao = dao.connect()
    #inserindo dados na tabela pessoa
    dao.insert_dict(conexao,pessoa)
    #fechando conexão
    conexao.close()

if __name__ == "__main__":
    main()