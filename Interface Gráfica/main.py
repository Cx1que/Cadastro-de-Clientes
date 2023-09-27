from customtkinter import *
from tkinter import *


janela = CTk()



class Aplication:
    def __init__(self):
        self.janela = janela    # variavel janela
        self.tela()              # chama a função tela
        self.frames_Da_tela()     # chama os frames
        janela.mainloop()          # mantem  a janela aberta

    def tela(self):
        self.janela.title('Cadastro de Clientes')
        self.janela.geometry('700x500')               # tamanho da tela
        self.janela.configure(fg_color='#446C65')      # fg_color altera cor de fundo da janela
        self.janela.resizable(True, True)  # para aumentar e diminuir o tamanho da janela
        self.janela.maxsize(width= 900, height= 700)    # tamanho max para aumentar janela
        self.janela.minsize(width= 500, height= 300)     # tamanho min

    def frames_Da_tela(self):
            # primeiro frame                        # fg_color muda cor do frame
        self.frame_1 = CTkFrame(master=self.janela, fg_color='#B3B3B3',
                                bg_color='transparent', border_width= 5, border_color='#ACACAC') # bg_color altera cor das quinas
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)
            # segundo frame
        self.frame_2 = CTkFrame(master=self.janela, fg_color='#B3B3B3', bg_color='transparent', border_width=5,
                                border_color='#ACACAC')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)


Aplication()

