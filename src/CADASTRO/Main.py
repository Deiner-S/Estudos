import tkinter as tk
from tkinter import ttk
import VIEW.Cadastro_pessoa as cadastro
import VIEW.Tabela_exebicao as table
def main():
    
    main_window = tk.Tk()
    main_window.title("Livraria")
    button_container = tk.Frame(main_window)


    
        
    button_container.pack(padx=24,pady=(0,16))
    tk.Button(button_container,text="Cadastro de pessoas",command=cadastro.cadastro).grid(padx=8,pady=8,ipadx=10,ipady=2)    
     
    table.tabela(main_window)

            

    main_window.mainloop() 
if __name__ == "__main__":
    main()