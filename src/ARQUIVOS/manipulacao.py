import os

arquivo1 = open("projeto1.txt", "w");
print(os.path.abspath(arquivo1.name));#retorna o caminho absoluto
arquivo1.write("ola mundo!!!");

print(os.path.relpath(arquivo1.name));
print(arquivo1);
arquivo1.close();


#ATRIBUTOS OBJETO ARQUIVO
# - name = nome
# - mode = modo de abertura: leitura, escrita e adição
# - closed = informa se o arquivo já foi fechado ou não
#Dentro do modulo os temos o objeto path que tem duas funções
# - os.path.abspath("nomearquivo.ext");
# - os.path.relpath("nomearquivo.ext");

# ABRINDO ARQUIVO MODO ESCRITA
arquivo = open('exemplo.txt', 'w', encoding='utf-8');
# EXIBINDO OS ATRIBUTOS DO ARQUIVO
print("Nome do arquivo:", arquivo.name);
print("Nome do arquivo:", arquivo.mode);
print("Nome do arquivo:", arquivo.closed);

#ESCREVENDO NO ARQUIVO
arquivo.write("chega de ola mundo");
#exit()
#FECHANDO ARQUIVO
arquivo.close();
#verificando se o arqvuido foi fechado
print('arquivo está fechado?', arquivo.closed);


#EXTRAINDO CAMINHO RELATIVO E ABSOLUTO.

relPath = os.path.relpath('exemplo.txt');
absPath = os.path.abspath('exemplo.txt');

print('caminho relativo', relPath);
print('caminho absoluto', absPath);
