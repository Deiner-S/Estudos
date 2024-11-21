#pip install tkinter

import tkinter as tk

#Widget Window (tk.Tk())
def window():
    janela = tk.Tk()
    janela.title(" Aplicação GUI")
    janela.mainloop()
#Widget Label
from tkinter import ttk
def label():
    janela = tk.Tk()
    janela.title(" Aplicação GUI com o Widget Label")
    ttk.Label(janela, text="Componente Label" ).grid(column=0, row=0)
    janela.mainloop()
#Widget Button
contador = 0
def button():

    def contador_label(lblRotulo):
        def funcao_contar():
            global contador
            contador = contador + 1
            lblRotulo.config(text=str(contador))
            lblRotulo.after(1000, funcao_contar)
        funcao_contar()
    janela = tk.Tk()
    janela.title("Contagem dos Segundos")
    lblRotulo = tk.Label(janela, fg="green")
    lblRotulo.pack()
    contador_label(lblRotulo)
    btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
    btnAcao.pack()
    janela.mainloop()

def main():
    button()
if __name__ == "__main__":
    main()
