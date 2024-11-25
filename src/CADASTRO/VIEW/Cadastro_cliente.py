from Domain.Pessoa import Pessoa
from CADASTRO.DAO.DAOcliente import DAOpessoa
from tkinter import messagebox as mb
import tkinter as tk

def cadastro():
    def create():        
        pessoa = Pessoa("%s" % (cpf.get()),"%s"% (nome.get()),"%s"% (data_cadastro.get()),"%s" % (endereco.get()))
        print(pessoa.too_string())
        dao = DAOpessoa()
        retorno = dao.create(pessoa)
        if not retorno:
            mb.showerror("ERRO","Não foi possível fazer o cadastro")
        else:
            mb.showinfo("Confirmação","Cadastro efetuado com sucesso!")
        dao.cursor.close()
        dao.conexao.close()                   

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

    tk.Label(form_container,text="Data de cadastro:",anchor="w").grid(row=0,column=2,padx=(0,16),pady=4,sticky="w")
    data_cadastro = tk.Entry(form_container)
    data_cadastro.grid(row=0,column=3)

    tk.Label(form_container,text="endereco:",anchor="w").grid(row=1,column=2,padx=(0,16),pady=4,sticky="w")
    endereco = tk.Entry(form_container)
    endereco.grid(row=1,column=3)

    tk.Button(button_container,text="Enviar",command=create).grid(row=4,column=0,pady=0,padx=6,ipadx=8,ipady=2)
    janela.mainloop()