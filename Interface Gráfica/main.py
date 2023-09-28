from customtkinter import *
from tkinter import ttk
import sqlite3

janela = CTk()

class Funcs():
    def limpa_tela(self):
        self.entr_codigo.delete(0, END)
        self.entr_nome.delete(0, END)
        self.entr_tel.delete(0, END)
        self.entr_cidade.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao Banco de Dados...")

    def desconecta_bd(self):
        self.conn.close(); print("Banco de Dados desconectado...")
    
    def monta_tabelas(self):
        self.conecta_bd();
        ### criando tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente VARCHAR (40) NOT NULL,
                telefone INTEGER (11),
                cidade VARCHAR (20)
            
        );""")
        self.conn.commit(); print("Banco de Dados criado!")
        self.desconecta_bd()






class Aplication(Funcs):
    def __init__(self):
        self.janela = janela    # variavel janela
        self.tela()              # chama a função tela
        self.frames_Da_tela()     # chama os frames
        self.widgets_frame1()
        self.lista_frame2()
        self.monta_tabelas()
        janela.mainloop()          # mantem  a janela aberta

    def tela(self):
        self.janela.title('Cadastro de Clientes')
        self.janela.geometry('700x500')               # tamanho da tela
        self.janela.configure(fg_color='#446C65')      # fg_color altera cor de fundo da janela
        self.janela.resizable(True, True)  # para aumentar e diminuir o tamanho da janela
        self.janela.maxsize(width= 900, height= 700)    # tamanho max para aumentar janela
        self.janela.minsize(width= 500, height= 400)     # tamanho min

    def frames_Da_tela(self):
            # primeiro frame                        # fg_color muda cor do frame
        self.frame_1 = CTkFrame(master=self.janela, fg_color='#B3B3B3',
                                bg_color='transparent', border_width= 5, border_color='#ACACAC') # bg_color altera cor das quinas
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)
            # segundo frame
        self.frame_2 = CTkFrame(master=self.janela, fg_color='#B3B3B3', bg_color='transparent', border_width=5,
                                border_color='#ACACAC')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        ### botao limpar
        self.bt_limpar = CTkButton(self.frame_1, text= 'Limpar', border_width= 2, bg_color='transparent', border_color='#345E56', fg_color= '#446C65', text_color= 'white', font= ('poppins', 11, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        ### botao Buscar
        self.bt_buscar = CTkButton(self.frame_1, text= 'Buscar', border_width= 2, bg_color='transparent',border_color='#345E56', fg_color= '#446C65', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.bt_buscar.place(relx= 0.31, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        ### botao novo
        self.bt_novo = CTkButton(self.frame_1, text= 'Novo', border_width= 2, bg_color='transparent',border_color='#345E56', fg_color= '#446C65', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.bt_novo.place(relx= 0.61, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        ### botao alterar
        self.bt_alterar = CTkButton(self.frame_1, text= 'Alterar', border_width= 2, bg_color='transparent',border_color='#345E56', fg_color= '#446C65', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.bt_alterar.place(relx= 0.71, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        ### botao apagar
        self.bt_apagar = CTkButton(self.frame_1, text= 'Apagar',border_width= 2, bg_color='transparent',border_color='#345E56', fg_color= '#446C65', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.bt_apagar.place(relx= 0.81, rely= 0.1, relwidth= 0.1, relheight= 0.15)



        ### label e entrada do código
        self.lb_codigo = CTkLabel(self.frame_1, text='Código', fg_color= '#B3B3B3', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.lb_codigo.place(relx= 0.05, rely= 0.02)

        self.entr_codigo = CTkEntry(self.frame_1, fg_color='white', text_color='black', border_color='#C5C5C5')
        self.entr_codigo.place(relx= 0.05, rely= 0.12,relwidth= 0.1)

        ### label e entrada do nome
        self.lb_nome = CTkLabel(self.frame_1, text='Nome', fg_color= '#B3B3B3', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.lb_nome.place(relx= 0.05, rely= 0.35)

        self.entr_nome = CTkEntry(self.frame_1, fg_color='white', text_color='black', border_color='#C5C5C5')
        self.entr_nome.place(relx= 0.05, rely= 0.45,relwidth= 0.45)

        ### label e entrada do telefone
        self.lb_tel = CTkLabel(self.frame_1, text='Telefone', fg_color= '#B3B3B3', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.lb_tel.place(relx= 0.05, rely= 0.6)

        self.entr_tel = CTkEntry(self.frame_1, fg_color='white', text_color='black', border_color='#C5C5C5')
        self.entr_tel.place(relx= 0.05, rely= 0.7,relwidth= 0.2)

        ### label e entrada da cidade
        self.lb_cidade = CTkLabel(self.frame_1, text='Cidade', fg_color= '#B3B3B3', text_color= 'white', font= ('poppins', 11, 'bold'))
        self.lb_cidade.place(relx= 0.3, rely= 0.6)

        self.entr_cidade = CTkEntry(self.frame_1, fg_color='white', text_color='black', border_color='#C5C5C5')
        self.entr_cidade.place(relx= 0.3, rely= 0.7,relwidth= 0.2)
    
    def lista_frame2(self):
        self.lista_cli = ttk.Treeview(self.frame_2, height= 3, column=('col1', 'col2', 'col3', 'col4'))
        self.lista_cli.heading("#0", text= '')
        self.lista_cli.heading("#1", text= 'Código')
        self.lista_cli.heading("#2", text= 'Nome')
        self.lista_cli.heading("#3", text= 'Telefone')
        self.lista_cli.heading("#4", text= 'Cidade')


        self.lista_cli.column("#0", width= 1)
        self.lista_cli.column("#1", width= 50)         ### a proporção total é 500, de acordo com a quantidade
        self.lista_cli.column("#2", width= 200)        ### de colunas podemos escolher a proporção correspondente
        self.lista_cli.column("#3", width= 125)        ### para cada uma.
        self.lista_cli.column("#4", width= 125)

        self.lista_cli.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)
        
        self.scrool_lista = CTkScrollbar(self.frame_2, orientation='vertical')
        self.lista_cli.configure(yscroll=self.scrool_lista.set)
        self.scrool_lista.place(relx= 0.96, rely= 0.1, relwidth= 0.04, relheight= 0.85)        


Aplication()
 
