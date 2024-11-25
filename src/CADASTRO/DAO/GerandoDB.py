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
    
    comand1 = """INSERT INTO Cliente (cpf, nome, endereco, data_cadastro, ultima_compra)
                VALUES                
                    ('123.456.789-00', 'João Silva', 'Rua das Flores, 123, Bairro Centro, São Paulo, SP', '2023-02-10', '2023-10-15'),
                    ('234.567.890-11', 'Maria Oliveira', 'Avenida Paulista, 2000, São Paulo, SP', '2023-03-12', '2023-11-01'),
                    ('345.678.901-22', 'José Pereira', 'Rua Rio de Janeiro, 55, Bairro Alto, Rio de Janeiro, RJ', '2023-05-25', '2023-07-20'),
                    ('456.789.012-33', 'Ana Costa', 'Rua das Palmeiras, 198, Bairro Jardim, Belo Horizonte, MG', '2023-07-30', '2023-09-05'),
                    ('567.890.123-44', 'Carlos Souza', 'Rua do Comércio, 88, Bairro Santa Cruz, Recife, PE', '2023-08-10', '2023-10-25'),
                    ('678.901.234-55', 'Fernanda Rocha', 'Avenida Brasil, 500, Bairro Boa Vista, Salvador, BA', '2023-01-05', '2023-11-10'),
                    ('789.012.345-66', 'Lucas Almeida', 'Rua Amazonas, 777, Bairro Vila Nova, Fortaleza, CE', '2023-06-15', '2023-10-30'),
                    ('890.123.456-77', 'Juliana Martins', 'Avenida Rio Branco, 300, Centro, Curitiba, PR', '2023-09-25', '2023-12-01'),
                    ('901.234.567-88', 'Roberto Gomes', 'Rua das Laranjeiras, 45, Bairro Primavera, Florianópolis, SC', '2023-11-01', '2023-12-05'),
                    ('012.345.678-99', 'Patrícia Silva', 'Rua das Acácias, 999, Bairro Porto, Porto Alegre, RS', '2023-02-15', '2023-08-20'),
                    ('123.456.789-01', 'Felipe Santos', 'Rua Sete de Setembro, 750, Bairro Jardim, Campinas, SP', '2023-03-10', '2023-09-18'),
                    ('234.567.890-12', 'Beatriz Lima', 'Rua São João, 200, Bairro Horizonte, Natal, RN', '2023-05-02', '2023-08-15'),
                    ('345.678.901-23', 'Eduardo Costa', 'Rua do Sol, 333, Bairro Paraíso, Goiânia, GO', '2023-04-20', '2023-10-25'),
                    ('456.789.012-34', 'Lúcia Souza', 'Avenida dos Bandeirantes, 555, Bairro Bela Vista, Campinas, SP', '2023-07-17', '2023-11-15'),
                    ('567.890.123-45', 'Marcos Alves', 'Rua dos Ingás, 999, Bairro Jardim América, Rio de Janeiro, RJ', '2023-01-22', '2023-06-30'),
                    ('678.901.234-56', 'Sofia Pereira', 'Avenida Independência, 700, Bairro Centro, Recife, PE', '2023-08-25', '2023-12-05'),
                    ('789.012.345-67', 'Ricardo Ferreira', 'Rua das Acácias, 220, Bairro São Luiz, São Paulo, SP', '2023-06-05', '2023-11-10'),
                    ('890.123.456-78', 'Gabriela Martins', 'Rua do Porto, 345, Bairro Santa Clara, Curitiba, PR', '2023-02-01', '2023-07-18'),
                    ('901.234.567-89', 'André Rocha', 'Avenida Marechal Deodoro, 122, Bairro Cambuí, Campinas, SP', '2023-04-25', '2023-10-12'),
                    ('012.345.678-00', 'Júlia Oliveira', 'Rua Monte Alegre, 90, Bairro Boa Vista, Fortaleza, CE', '2023-05-10', '2023-09-08'),
                    ('123.456.789-12', 'Gabriel Silva', 'Rua São Pedro, 200, Bairro Alto, Recife, PE', '2023-06-15', '2023-11-10'),
                    ('234.567.890-23', 'Cláudia Costa', 'Avenida dos Três Rios, 350, Bairro Jardim, Porto Alegre, RS', '2023-07-01', '2023-10-30'),
                    ('345.678.901-34', 'Ricardo Almeida', 'Rua José Bonifácio, 500, Centro, Salvador, BA', '2023-03-05', '2023-09-12'),
                    ('456.789.012-45', 'Vera Lima', 'Rua do Comércio, 67, Bairro Jardim Europa, Belo Horizonte, MG', '2023-08-10', '2023-12-10'),
                    ('567.890.123-56', 'Tiago Costa', 'Rua dos Três, 123, Bairro São Cristóvão, Curitiba, PR', '2023-01-05', '2023-10-10'),
                    ('678.901.234-67', 'Tatiane Souza', 'Avenida Santos Dumont, 900, Bairro Nossa Senhora, Fortaleza, CE', '2023-09-22', '2023-12-20'),
                    ('789.012.345-78', 'Fábio Rocha', 'Rua Porto Seguro, 320, Bairro Jardim das Acácias, Porto Alegre, RS', '2023-02-25', '2023-06-15'),
                    ('890.123.456-89', 'Amanda Martins', 'Rua das Flores, 300, Bairro Vila Nova, Goiânia, GO', '2023-06-05', '2023-11-20'),
                    ('901.234.567-90', 'Juliano Pereira', 'Avenida dos Pássaros, 150, Bairro Cruzeiro, São Paulo, SP', '2023-03-15', '2023-10-05'),
                    ('012.345.678-11', 'Ricardo Gomes', 'Rua dos Eucaliptos, 430, Bairro Alto, Natal, RN', '2023-07-10', '2023-09-20'),
                    ('123.456.789-23', 'Mariana Lima', 'Rua dos Jacarandás, 99, Bairro Nova Esperança, Recife, PE', '2023-04-15', '2023-12-10'),
                    ('234.567.890-34', 'Eduardo Oliveira', 'Avenida do Sol, 200, Bairro São Francisco, Porto Alegre, RS', '2023-05-30', '2023-08-25'),
                    ('345.678.901-45', 'Patrícia Ferreira', 'Rua da Paz, 200, Bairro Bela Vista, Rio de Janeiro, RJ', '2023-06-10', '2023-09-30'),
                    ('456.789.012-56', 'Carlos Lima', 'Rua das Palmeiras, 850, Bairro Jardim Paulista, São Paulo, SP', '2023-02-05', '2023-07-25'),
                    ('567.890.123-67', 'Luciana Pereira', 'Rua dos Pirineus, 400, Bairro São Cristóvão, Fortaleza, CE', '2023-07-18', '2023-12-15'),
                    ('678.901.234-78', 'Lucas Gomes', 'Rua dos Cedros, 99, Bairro Jardim São Luís, Recife, PE', '2023-08-05', '2023-11-05'),
                    ('789.012.345-89', 'Cláudia Souza', 'Avenida Rio Branco, 45, Bairro Nova América, Salvador, BA', '2023-01-25', '2023-10-20'),
                    ('890.123.456-90', 'Felipe Rocha', 'Rua do Centro, 120, Bairro Santa Clara, Belo Horizonte, MG', '2023-04-30', '2023-09-05'),
                    ('901.234.567-01', 'Sofia Martins', 'Rua da Felicidade, 300, Bairro Nova Esperança, Goiânia, GO', '2023-06-22', '2023-12-01'),
                    ('012.345.678-22', 'Gabriela Silva', 'Rua dos Guarujás, 200, Bairro Jardim Morumbi, Porto Alegre, RS', '2023-05-17', '2023-10-15'),
                    ('123.456.789-34', 'Marcos Lima', 'Avenida São João, 1100, Centro, Florianópolis, SC', '2023-02-20', '2023-07-10');
        



             """
    
    comand3 = """SELECT * FROM Cliente
                    WHERE ultima_compra > "2023-07-20"
                    ORDER BY ultima_compra
                    LIMIT 5 OFFSET 0;"""

    lista = cursor.execute(comand3).fetchall()

    for i in lista:
        print(i)

    con.commit()
    cursor.close()

except conexao.DatabaseError as e:
    print(f"Erro banco de dados: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    if con:        
        con.close()
