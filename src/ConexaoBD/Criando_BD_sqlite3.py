import sqlite3 as conector

try:
    #abertura de conexão e aquisição de cursor
    conexao = conector.connect("./data_base.db", detect_types=conector.PARSE_DECLTYPES)
    cursor = conexao.cursor()

    # Execução de um comando:
    # comando é passado por meio de uma variável string
    comando1 = """CREATE TABLE Pessoa(
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    );"""
                    
    comando2 ="""CREATE TABLE Marca(
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                    );"""
                
    comando3 ="""CREATE TABLE Veiculo(
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    propietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(propietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) References Marca(id)
                    );"""
    
    comando4 ="""ALTER TABLE Veiculo
                    ADD motor REAL;"""
    
    comando5 ="""DROP TABLE Veiculo;"""

    comando6 ="""CREATE TABLE Veiculo(
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    propietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(propietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) References Marca(id)
                    );"""
    comando7 = """INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
       VALUES (12345678900, 'João', '2000-01-31', 1);"""
    
    #cursor.execute(comando1)
    #cursor.execute(comando2)
    #cursor.execute(comando3)
    #cursor.execute(comando4)
    #cursor.execute(comando5)
    #cursor.execute(comando6)
    #cursor.execute(comando7)
    
    #Efetivação do comando
    conexao.commit()
    
    #efetuando consulta 
    comando8 = "SELECT * FROM Pessoa WHERE cpf = '12345678900' "
    cursor.execute(comando8)
    #Capturando resultado do comando SELECT
    resultado = cursor.fetchall()
    #verificando qual o tipo de dado que é retornado
    print(type(resultado)) # <class 'list'> retorna uma lista
    print(type(resultado[0]))# <class 'tuple'> retorna uma tupla
    
    #note que alguns atributos são retornados com o tipo de dado diferente dos dados declarados no banco
    for lista in resultado:
        for atributos in lista:
            print(f"{atributos}: {type(atributos)}")
    #para concertar isso será necessário adicionar esse comando na frente do caminho da conexão do banco:
    #,detect_types=conector.PARSE_DECLTYPES e criar a seguinte função:
    #primeiramente criamos uma função de conversão de dados comum
    def converter_boolean(dado):
        return True if dado == 1 else False
    #apos criar essa função definimos um cnversor no nosso conector
    conector.register_converter("BOOLEAN",converter_boolean)
    #rodamos o comando8 novamente
    cursor.execute(comando8)
    resultado = cursor.fetchall()
    #verificando se deu certo: 
    for lista in resultado:
        for atributos in lista:
            print(f"{atributos}: {type(atributos)}")
    
    
    
except conector.DatabaseError as e:
    print(f"Erro bando de dados: {e}")

finally:
    #Fechamento de conexões
    if conexao:
        cursor.close()
        conexao.close()