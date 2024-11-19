import sqlite3 as conector

try:
    #abertura de conexão e aquisição de cursor
    conexao = conector.connect("./data_base.db")
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
    
    
    cursor.execute(comando1)
    cursor.execute(comando2)
    cursor.execute(comando3)
    cursor.execute(comando4)
    cursor.execute(comando5)
    cursor.execute(comando6)
    
    
    #Efetivação do comando
    conexao.commit()
except conector.DatabaseError as e:
    print(f"Erro bando de dados: {e}")

finally:
    #Fechamento de conexões
    if conexao:
        cursor.close()
        conexao.close()