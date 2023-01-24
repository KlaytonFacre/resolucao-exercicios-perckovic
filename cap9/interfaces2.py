from cgitb import text
from tkinter import Tk, Button, Label, Entry, PhotoImage
from tkinter.messagebox import showinfo
from time import strftime, strptime
from turtle import width


def clicked():
    global caixa
    data = caixa.get()
    dia_semana = strftime('%A', strptime(data, '%d %b %Y'))
    showinfo(message='{} foi um {}'.format(data, dia_semana))


# Cria o objeto que será a janela principal do programa
janela_principal = Tk()
janela_secundaria = Tk()

# Cria os widgets que estarão dentro da janela principal
rotulo = Label(janela_principal, text='Digite uma data:')
caixa = Entry(janela_principal)
botao = Button(janela_principal, text='Clique', command=clicked)

# Estes widgets ficarão na janela secundaria
#Hom = PhotoImage(file='cat.gif')
#imagem = Label(master=janela_secundaria, image=Hom)

# Posiciona os widgets dentro da janela principal
rotulo.grid(row=0, column=0)
caixa.grid(row=0, column=1)
botao.grid(row=1, column=0, columnspan=2)

# Posiciona os widgets dentro da janela secundária
#imagem.grid(row=0, column=0)

# Inicia a exibição da janela através do loop infinito
janela_principal.mainloop()
janela_secundaria.mainloop()
