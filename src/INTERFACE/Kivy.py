#Ele é escrito em python e Cython, baseado em OpenGL ES 2, suporta vários dispositivos de entrada 
#e possui uma extensa biblioteca de componentes (widgets). Com o mesmo código, a aplicação funciona 
#para Windows, macOS, Linux, Android e iOS. Todos os widgets Kivy são construídos com suporte multitoque.

#pip install Kivy

from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')
    

def main():
    
    exemplo = ExemploApp()
    exemplo.build()

if __name__ == "__main__":
    main()