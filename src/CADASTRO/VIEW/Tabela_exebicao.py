import tkinter as tk
from tkinter import ttk
from CADASTRO.DAO.DAOcliente import DAOcliente

def select(info):
    dao = DAOcliente()
    lista = dao.read(info)
    dao.cursor.close()
    dao.conexao.close()
    return lista
    


def tabela(main_window,info):
        


        tabela_container = tk.Frame(main_window)
        tabela_container.pack(padx=24,pady=16)

        #DEFINIÇÃO DO NOME DAS COLUNAS
        colunas = ("CPF","Nome","Nascimento","Oculos")
        treeview = ttk.Treeview(tabela_container,columns=colunas, show="headings")
        
        treeview.heading("CPF", text="CPF",anchor="center")
        treeview.heading("Nome", text="Nome",anchor="center")
        treeview.heading("Nascimento", text="Nascimento",anchor="center")
        treeview.heading("Oculos", text="Oculos", anchor="center")
        
        # Adicionar barras de rolagem
        scrollbar = tk.Scrollbar(tabela_container, orient=tk.VERTICAL, command=treeview.yview)
        treeview.config(yscrollcommand=scrollbar.set)
        
        # Organizar o layout
        treeview.pack(side=tk.LEFT , fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)        
        
        for row in select(info):
            treeview.insert("", "end", values=row)