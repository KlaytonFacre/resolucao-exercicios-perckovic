# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 9.2
# Description:      Resolução do problema livro Perkovic, capítulo 9, pág 319:
#                   Implementar uma função cal() utilizando GUI.
# Site:
# Linkedin:         www.linkedin.com/in/klaytonfacre
# Escrito por:      Klayton Facre
# Mantido por:      Klayton Facre
# -------------------------------------------------------------------------------#
# Usage:
# -------------------------------------------------------------------------------#
# Python Version:
#                   3.0 ou superior
# -------------------------------------------------------------------------------#
# History:          v1.0 30/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from ctypes import alignment
from tkinter import END, Label, Tk, Button, Entry
from calendar import month, monthrange
from problema9_2v2 import cal


def handler():
    global caixa_entrada
    dados = caixa_entrada.get().split('/')
    mes = eval(dados[1].lstrip('0'))
    ano = eval(dados[2].lstrip('0'))
    caixa_entrada.delete(0, END)
    cal(ano, mes)


janela_inicial = Tk()

botao_mes = Button(janela_inicial, text='Ver calendário', command=handler)
caixa_entrada = Entry(janela_inicial)
botao_fechar = Button(janela_inicial, text='Fechar',
                      command=janela_inicial.destroy)
rotulo_entrada = Label(janela_inicial, text='Digite uma data:')

rotulo_entrada.grid(row=0, column=0)
caixa_entrada.grid(row=0, column=1)
botao_mes.grid(row=1, column=0)
botao_fechar.grid(row=1, column=1)

janela_inicial.mainloop()
