from Domain.Pessoa import Pessoa
from DAO.DAOpessoa import DAOpessoa

import tkinter as tk
from tkinter import ttk




def main():

    def create():
        dao = DAOpessoa()
        pessoa = Pessoa("%s" % (nome.get()),"%s"% (cpf.get()),"%s"% (nascimento.get()),"%s" % (oculos.get()))
        dao.create(pessoa)
        dao.cursor.close()
        dao.conexao.close()

    def update():
        pass
    def delete():
        pass            

    janela = tk.Tk()
    janela.title("Dados cadastrais")

    form_container = tk.Frame(janela)
    button_container = tk.Frame(janela)
    form_container.pack(padx=24,pady=16)
    button_container.pack(padx=24,pady=(0,16))

    tk.Label(form_container,text="Nome:",anchor="w").grid(row=0,padx=(0,16),pady=4,sticky="w")
    nome = tk.Entry(form_container)
    nome.grid(row=0,column=1, padx=(0,32))

    tk.Label(form_container,text="CPF:",anchor="w").grid(row=1,column=0,padx=(0,16),pady=4,sticky="w")
    cpf = tk.Entry(form_container)
    cpf.grid(row=1,column=1, padx=(0,32))

    tk.Label(form_container,text="Data de nascimento:",anchor="w").grid(row=0,column=2,padx=(0,16),pady=4,sticky="w")
    nascimento = tk.Entry(form_container)
    nascimento.grid(row=0,column=3)

    tk.Label(form_container,text="Oculos:",anchor="w").grid(row=1,column=2,padx=(0,16),pady=4,sticky="w")
    oculos = tk.Entry(form_container)
    oculos.grid(row=1,column=3)

    tk.Button(button_container,text="Enviar",command=create).grid(row=4,column=0,pady=0,padx=6,ipadx=8,ipady=2)
    tk.Button(button_container,text="Editar",command=update).grid(row=4,column=1,pady=0,padx=6,ipadx=8,ipady=2)
    tk.Button(button_container,text="Excluir",command=delete).grid(row=4,column=2,pady=0,padx=6,ipadx=8,ipady=2)
    janela.mainloop()
 
    
    
   
if __name__ == "__main__":
    main()