import tkinter as tk
from tkinter import ttk
import VIEW.Cadastro_pessoa as cadastro
def main():
    
    main_window = tk.Tk()
    main_window.title("Livraria")
    button_container = tk.Frame(main_window)
    tabela_container = tk.Frame(main_window)
    tabela_container.pack(padx=24,pady=16)
    button_container.pack(padx=24,pady=(0,16))
    
    
    colunas = ("CPF","Nome","Nascimento","Oculos")
    treeview = ttk.Treeview(tabela_container,columns=colunas, show="headings")
    
    treeview.heading("CPF", text="CPF")
    treeview.heading("Nome", text="Nome")
    treeview.heading("Nascimento", text="Nascimento")
    treeview.heading("Oculos", text="Oculos")
    
    # Adicionar barras de rolagem
    scrollbar = tk.Scrollbar(tabela_container, orient=tk.VERTICAL, command=treeview.yview)
    treeview.config(yscrollcommand=scrollbar.set)
    
    # Organizar o layout
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
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
    tk.Button(button_container,text="Cadastro de pessoas",command=cadastro.cadastro).grid(padx=8,pady=8,ipadx=10,ipady=2)    
    main_window.mainloop()          

    
if __name__ == "__main__":
    main()