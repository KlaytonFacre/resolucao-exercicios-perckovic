# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 9.2 versão 2
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
from tkinter import Button, Tk, Label
from calendar import monthrange


def cal(ano, mes):
    # Rótulos para o mês e dias da semana
    dias_semana = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
             'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

    # Criação do objeto da janela principal
    calendario = Tk()

    # Dados de dia da semana inicial e quantidade de dias do mês
    dados_mes = monthrange(ano, mes)

    # Preenchimento do rótulo do mês
    mes_rotulo = Label(calendario, text=meses[mes - 1])
    mes_rotulo.grid(row=0, column=0, columnspan=4)

    ano_rotulo = Label(calendario, text=ano)
    ano_rotulo.grid(row=0, column=4, columnspan=3)

    botao_fechar = Button(calendario, text='Fechar',
                          command=calendario.destroy)
    botao_fechar.grid(row=8, column=0, columnspan=7)

    # Preenchimento dos rótulos de dia da semana
    for dia_semana in range(7):
        dias_rotulo = Label(calendario,
                            text=dias_semana[dia_semana])
        dias_rotulo.grid(row=1, column=dia_semana)

    # Preenchimento dos rótulos dos dias
    linha_inicial = 2
    coluna_inicial = dados_mes[0]
    for dia in range(dados_mes[1]):
        data = Label(calendario, text=(dia + 1))
        data.grid(row=linha_inicial, column=coluna_inicial)
        coluna_inicial += 1

        if coluna_inicial > 6:
            coluna_inicial = 0
            linha_inicial += 1

    calendario.mainloop()
