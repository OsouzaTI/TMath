from tkinter import *
from tkinter import messagebox
from Cor import cores
c = cores.cores
font_ = 'Helvetica, 16'
# class janela:
#     def __init__(self,tk):
#         def adicionaLista():
#             n = self.ed.get()
#             if n.isnumeric():
#                 self.lt.insert(END,self.ed.get())
#                 self.ed.delete(0, END)
#             else:
#                 self.ed.delete(0,END)
#                 messagebox.showerror('Caixa vazia','Digite um valor numerico!')
#         def MArit():
#             if self.fmRp.winfo_exists():
#                 self.fmRp.destroy()
#             self.fmRp = Frame(self.fmBt, bg='#c1cfdf') # Frame pai
#             tsoma,tmedia = StringVar(),StringVar()
#             fmrp_1 = Frame(self.fmRp, bg='#c1cfdf')
#             fmrp_1.pack(anchor=W) #filho 1
#             lb3 = Label(fmrp_1, text="Soma dos Valores: ",bg='#c1cfdf',font=font_)
#             lb3.pack(side=LEFT)
#             self.lbSoma = Label(fmrp_1, textvariable=tsoma,bg='#c1cfdf',font=font_)
#             self.lbSoma.pack(side=LEFT)
#
#             fmrp_2 = Frame(self.fmRp, bg='#c1cfdf')
#             fmrp_2.pack(anchor=W)  # filho 2
#             lb4 = Label(fmrp_2, text="Média : ", bg='#c1cfdf',font=font_)
#             lb4.pack(side=LEFT)
#             lbMedia = Label(fmrp_2, textvariable=tmedia, bg='#c1cfdf',font=font_)
#             lbMedia.pack(side=LEFT)
#
#             def calc():
#                 soma,media = 0,0
#                 n = int(self.lt.size())
#                 if n > 0:
#                     for i in range(n):
#                         soma += int(self.lt.get(i))
#                     tsoma.set(str(soma))
#                     tmedia.set('%.2f'%(soma/n))
#                 else:
#                     messagebox.showerror('Lista Vazia', 'Coloque pelo menos um número!')
#                 print('oi')
#
#             fmrp_3 = Frame(self.fmRp, bg='#c1cfdf')
#             fmrp_3.pack()  # filho 3
#             btCalc = Button(fmrp_3,text='Calcular',command=calc).pack(pady=10)
#
#
#             self.fmRp.pack(fill=BOTH, expand=1)
#
#
#
#         def MPond():
#             if self.fmRp.winfo_exists():
#                 self.fmRp.destroy()
#             self.fmRp = Frame(self.fmBt, bg='#b67f7a')
#             self.tst = Label(self.fmRp, text="Ponderada").pack()
#             self.fmRp.pack(fill=BOTH, expand=1)
#
#
#         self.fm = Frame(tk,bg='#D7E7F8')
#         self.lb1 = Label(self.fm,text="Números:     ",font=font_,bg='#D7E7F8')
#         self.lb1.pack(side=LEFT,anchor=W)
#         self.ed = Entry(self.fm,font=font_,width=10)
#         self.ed.pack(side=LEFT,anchor=W)
#         self.bt = Button(self.fm,text="Adcionar",command=adicionaLista).pack(padx=10,pady=3,anchor=W)
#         self.fm.pack(side=TOP,anchor=W,fill=X)
#
#         self.fm1 = Frame(tk,bg='#D7E7F8')
#
#         self.lt = Listbox(self.fm1,font=font_,width=10)
#         self.lt.pack(side=LEFT,anchor=W,fill=Y,padx=2,pady=2)
#
#         self.fm1.pack(side=TOP,anchor=W,fill=BOTH,expand=1)
#
#         #caixas de opções =======================================#
#         self.fmBt = Frame(self.fm1,bg='#D7E7F8')
#
#         self.lbOp = Label(self.fmBt,text="Opções",font=font_,bg='#D7E7F8').pack()
#         #Frame da caixa de opções
#         self.fmOp = Frame(self.fmBt,bg='#D7E7F8')
#         self.lb2 = Label(self.fmOp,text="Tipo de média:",font=font_,bg='#D7E7F8')
#         self.lb2.pack(side=LEFT)
#         self.rdbV = IntVar()
#         self.rdb = Radiobutton(self.fmOp,text="Aritmética",variable=self.rdbV,value=1,command=MArit,bg='#D7E7F8').pack(side=LEFT,anchor=N)
#         self.rdb1 = Radiobutton(self.fmOp,text="Ponderada",variable=self.rdbV,value=2,command=MPond,bg='#D7E7F8').pack(side=LEFT,anchor=N)
#         self.fmOp.pack() # frame de op
#         self.fmRp = Frame(self.fmBt,bg='#c1cfdf')
#         self.lb4 = Label(self.fmRp,text="Olá").pack()
#         self.fmRp.pack(fill=BOTH,expand=1)
#         # setando o radio button
#         self.rdbV.set(1)
#         MArit()
#
#         self.fmBt.pack(side=LEFT,anchor=N,fill=Y)
#
#
#
#
#tk = Tk()
# tk.geometry('600x400')
# tk.resizable(width=False, height=False)
# janela(tk)
# tk.mainloop()
def MediaScr(self,tk):
    self.fm_ = Frame(tk)
    self.fm_.pack(side=LEFT,fill=BOTH,expand=1)
    def adicionaLista():
        isNun = 0
        try:
            n = float(self.ed.get())/1
            isNun = 1
        except:
            isNun = 0

        if isNun:
            self.lt.insert(END, self.ed.get())
            self.ed.delete(0, END)
        else:
            self.ed.delete(0, END)
            messagebox.showerror('Caixa vazia', 'Digite um valor numerico!')
    def adicionaListaP():
        n = self.edP.get()
        if n.isnumeric():
            self.ltP.insert(END, self.edP.get())
            self.edP.delete(0, END)
        else:
            self.edP.delete(0, END)
            messagebox.showerror('Caixa vazia', 'Digite um valor numerico!')

# =======================================================================================#
    def MArit():
        if self.fmRp.winfo_exists():
            self.fmRp.destroy()
        self.fmRp = Frame(self.fmBt, bg=c[0])  # Frame pai
        tsoma, tmedia = StringVar(), StringVar()
        fmrp_1 = Frame(self.fmRp, bg=c[0])
        fmrp_1.pack(anchor=W)  # filho 1
        lb3 = Label(fmrp_1, text="Soma dos Valores: ", bg=c[0], font=font_)
        lb3.pack(side=LEFT)
        self.lbSoma = Label(fmrp_1, textvariable=tsoma, bg=c[0], font=font_)
        self.lbSoma.pack(side=LEFT)

        fmrp_2 = Frame(self.fmRp, bg=c[0])
        fmrp_2.pack(anchor=W)  # filho 2
        lb4 = Label(fmrp_2, text="Média : ", bg=c[0], font=font_)
        lb4.pack(side=LEFT)
        lbMedia = Label(fmrp_2, textvariable=tmedia, bg=c[0], font=font_)
        lbMedia.pack(side=LEFT)

        def calc():
            soma, media = 0, 0
            n = int(self.lt.size())
            #print(n)
            if n > 0:
                for i in range(n):
                    soma += float(self.lt.get(i))
                    #print(soma)
                tsoma.set(str(soma))
                tmedia.set('%.2f' % (soma / n))
            else:
                messagebox.showerror('Lista Vazia', 'Coloque pelo menos um número!')

        fmrp_3 = Frame(self.fmRp, bg=c[0])
        fmrp_3.pack()  # filho 3
        btCalc = Button(fmrp_3, text='Calcular', command=calc).pack(pady=10)

        self.fmRp.pack(fill=BOTH, expand=1)
#=======================================================================================#
    def MPond():
        if self.fmRp.winfo_exists():
            self.fmRp.destroy()
        self.fmRp = Frame(self.fmBt, bg=c[0])  # Frame pai
        tsoma, tmedia = StringVar(), StringVar()

        fmrp_4 = Frame(self.fmRp, bg=c[0])
        self.lb1 = Label(fmrp_4, text="Pesos na ordem:     ", font=font_, bg=c[0])
        self.lb1.pack(side=LEFT, anchor=W)
        self.edP = Entry(fmrp_4, font=font_, width=10)
        self.edP.pack(side=LEFT, anchor=W)
        self.bt = Button(fmrp_4, text="Adcionar", command=adicionaListaP).pack(padx=10, pady=3, anchor=W)
        fmrp_4.pack(fill=X, expand=1)

        fmrp_5 = Frame(self.fmRp, bg=c[0])
        self.ltP = Listbox(fmrp_5, font=font_,height=5)
        self.ltP.pack(fill=X,anchor=W)
        fmrp_5.pack(fill=X, expand=1)

        fmrp_1 = Frame(self.fmRp, bg=c[0])
        fmrp_1.pack(anchor=W)  # filho 1
        lb3 = Label(fmrp_1, text="Soma dos Valores: ", bg=c[0], font=font_)
        lb3.pack(side=LEFT)
        self.lbSoma = Label(fmrp_1, textvariable=tsoma, bg=c[0], font=font_)
        self.lbSoma.pack(side=LEFT)

        fmrp_2 = Frame(self.fmRp, bg=c[0])
        fmrp_2.pack(anchor=W)  # filho 2
        lb4 = Label(fmrp_2, text="Média : ", bg=c[0], font=font_)
        lb4.pack(side=LEFT)
        lbMedia = Label(fmrp_2, textvariable=tmedia, bg=c[0], font=font_)
        lbMedia.pack(side=LEFT)

        def calc():
            soma, media, somaP = 0, 0, 0
            n = int(self.lt.size())
            nP = int(self.ltP.size())
            #print(n)
            if n > 0 and n == nP:
                for i in range(n):
                    soma += float(self.lt.get(i))*float(self.ltP.get(i))
                    somaP += float(self.ltP.get(i))
                    #print(soma)
                tsoma.set(str(soma))
                tmedia.set('%.2f' % (soma / somaP))
            else:
                messagebox.showerror('Lista Vazia', 'Coloque pelo menos um número!')

        fmrp_3 = Frame(self.fmRp, bg=c[0])
        fmrp_3.pack()  # filho 3
        btCalc = Button(fmrp_3, text='Calcular', command=calc).pack(pady=10)

        self.fmRp.pack(fill=BOTH, expand=1,anchor=N)

# =======================================================================================#

    self.fm = Frame(self.fm_, bg=c[2])
    self.lb1 = Label(self.fm, text="Números:     ", font=font_, bg=c[2])
    self.lb1.pack(side=LEFT, anchor=W)
    self.ed = Entry(self.fm, font=font_, width=10)
    self.ed.pack(side=LEFT, anchor=W)
    self.bt = Button(self.fm, text="Adcionar", command=adicionaLista).pack(padx=10, pady=3, anchor=W)
    self.fm.pack(side=TOP, anchor=W, fill=X)

    self.fm1 = Frame(self.fm_, bg=c[0])

    self.lt = Listbox(self.fm1, font=font_, width=10)
    self.lt.pack(side=LEFT, anchor=W, fill=Y, padx=2, pady=2)

    self.fm1.pack(side=TOP, anchor=W, fill=BOTH, expand=1)

    # caixas de opções =======================================#
    self.fmBt = Frame(self.fm1, bg=c[0])

    self.lbOp = Label(self.fmBt, text="Opções", font=font_, bg=c[0]).pack()
    # Frame da caixa de opções
    self.fmOp = Frame(self.fmBt, bg=c[0])
    self.lb2 = Label(self.fmOp, text="Tipo de média:", font=font_, bg=c[0])
    self.lb2.pack(side=LEFT)
    self.rdbV = IntVar()
    self.rdb = Radiobutton(self.fmOp, text="Aritmética", font = font_,variable=self.rdbV, value=1, command=MArit, bg=c[0]).pack(
        side=LEFT, anchor=N)
    self.rdb1 = Radiobutton(self.fmOp, text="Ponderada", font = font_, variable=self.rdbV, value=2, command=MPond, bg=c[0]).pack(
        side=LEFT, anchor=N)
    self.fmOp.pack()  # frame de op
    self.fmRp = Frame(self.fmBt, bg=c[0])
    self.lb4 = Label(self.fmRp, text="Olá").pack()
    self.fmRp.pack(fill=BOTH, expand=1)
    # setando o radio button
    self.rdbV.set(1)
    MArit()

    self.fmBt.pack(side=LEFT, anchor=N, fill=BOTH,expand=1)