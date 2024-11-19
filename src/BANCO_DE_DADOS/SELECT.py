import sqlite3 as conector
from Pessoa import Pessoa

def SELECT_SIMPLES(): 
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Definição dos registros
    comando = '''SELECT nome, oculos FROM Pessoa;'''
    cursor.execute(comando)

    # Recuperação dos dados
    registros = cursor.fetchall()
    print("Tipo retornado pelo fetchall():", type(registros))

    for registro in registros:
        print("Tipo:", type(registro), "- Conteúdo:", registro)

    # Fechamento das conexões
    cursor.close()
    conexao.close()

def SELECT_CONSTRUCAO_OBJETO():    
    
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Definição dos comandos
    comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": True})

    # Recuperação dos registros
    registros = cursor.fetchall()
    for registro in registros:
        pessoa = Pessoa(*registro)
        print("cpf:", type(pessoa.cpf), pessoa.cpf)
        print("nome:", type(pessoa.nome), pessoa.nome)
        print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
        print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

    # Fechamento das conexões
    cursor.close()
    conexao.close()

def SELECT_AJUSTE_TIPO_DE_DADOS():
    
    # Abrindo conexão com: PARSE_DECLTYPES. Isso indica que o conector deve tentar fazer uma conversão dos dados, tomando como base o tipo da coluna declarada no CREATE TABLE.
    conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES)
    cursor = conexao.cursor()

    # Funções conversoras
    def conv_bool(dado):
        return True if dado == 1 else False

    # Registro de conversores
    conector.register_converter("BOOLEAN", conv_bool)

    # Definição dos comandos
    comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": True})

    # Recuperação dos registros
    registros = cursor.fetchall()
    for registro in registros:
        pessoa = Pessoa(*registro)
        print("cpf:", type(pessoa.cpf), pessoa.cpf)
        print("nome:", type(pessoa.nome), pessoa.nome)
        print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
        print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

    # Fechamento das conexões
    cursor.close()
    conexao.close()