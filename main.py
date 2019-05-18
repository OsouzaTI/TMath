from tkinter import *
from tkinter import ttk
from FunctionsMenu import *

matAba = ['#D7E7F8','#E8F2FC','#b9c1c9']
fisAba = ['#D7E7F8']

OPselected = ''
font_ = 'Helvetica, 16'
def menu(self, p):
    # ======================================#
    # iniciando a variavel menu
    self.MenuBar = Menu(self.container1)
    # adicionando na tela a barra de menu
    p.configure(menu=self.MenuBar)
    # criando a listagem de itens do menu
    self.filemenu = Menu(self.MenuBar, tearoff=0)
    self.filemenu.add_command(label='Sobre', command=sobre)
    self.filemenu.add_command(label='Sair', command=p.quit)
    self.MenuBar.add_cascade(label="Arquivo", menu=self.filemenu)
    # ======================================#
def lista(self,p):

    def MudouOP(*args):
        self.lb.destroy()
        fm = Frame(p,bg=matAba[1])
        lb1 = Label(fm,text="Criou!",bg=matAba[1],font=font_).pack()
        fm.pack(side=LEFT,fill=BOTH,expand=1)

    lista_ = ['Média Aritmética','Média Ponderada']
    op_ = StringVar(p)
    op_.set(lista_[0])
    op_.trace('w',MudouOP)
    self.op = OptionMenu(p,op_,lista_[0],lista_[1])
    self.op.pack(side=TOP,anchor=E)

    self.lb = Label(p,text="MATEMÁTICA",bg=matAba[0],font=font_)
    self.lb.pack(side=LEFT, expand=1)

def abas(self, p):
    self.abas = ttk.Notebook(p)
    self.frame_aba1 = Frame(self.abas)
    self.frame_aba2 = Frame(self.abas)
    self.frame_aba3 = Frame(self.abas)

    #listas
    lista(self,self.frame_aba1)

    self.frame_aba1['background'] = matAba[0]
    self.frame_aba2['background'] = fisAba[0]
    self.frame_aba3['background'] = "#D7E7F8"

    self.abas.add(self.frame_aba1, text="Matemática")
    self.abas.add(self.frame_aba2, text="Física")
    self.abas.add(self.frame_aba3, text="Em breve")

    self.abas.pack(side=LEFT, fill=BOTH, expand=1)


class main:
    def __init__(self, p):
        p.title('TMath')
        self.container1 = Frame(p)
        self.container1.pack()
        # menu
        menu(self, p)
        # abas de tela
        abas(self, p)


raiz = Tk()
raiz.configure(background='white')
raiz.resizable(width=False, height=False)
raiz.geometry('600x600')
main(raiz)
raiz.mainloop()
