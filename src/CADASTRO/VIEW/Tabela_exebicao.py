import tkinter as tk
from tkinter import ttk

def tabela(main_window):
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
        
        data = [
        (1, "Ana", 23, "São Paulo"),
        (2, "Carlos", 31, "Rio de Janeiro"),
        (3, "Beatriz", 29, "Belo Horizonte"),
        (4, "David", 35, "Curitiba"),
        (5, "Fernanda", 40, "Porto Alegre"),
        (6, "Gabriel", 28, "Salvador"),
        (7, "Helena", 22, "Fortaleza"),
        (8, "Igor", 33, "Recife"),
        (9, "Juliana", 27, "Florianópolis"),
        (10, "Lucas", 38, "Manaus"),
        ]
        for row in data:
            treeview.insert("", "end", values=row)