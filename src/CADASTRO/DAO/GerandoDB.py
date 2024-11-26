import sqlite3 as conexao
try: 
    con = conexao.connect("src\CADASTRO\DAO\data.db")
    cursor = con.cursor()

    comand = """CREATE TABLE Cliente(
                    cpf TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    endereco TEXT NOT NULL,
                    data_cadastro DATE NOT NULL,
                    ultima_compra  DATE NOT NULL,
                    PRIMARY KEY(cpf)           
                );"""
    
    comand1 = """DROP TABLE Cliente"""
    
    comand3 = """SELECT * FROM Cliente
                    WHERE ultima_compra > "2023-07-20"
                    ORDER BY ultima_compra
                    LIMIT 5 OFFSET 0;"""

    cursor.execute(comand1)

    
    con.commit()
    cursor.close()

except conexao.DatabaseError as e:
    print(f"Erro banco de dados: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    if con:        
        con.close()
