# -------------------------------------------------------------------------------#
# Program Name:     keyLogger.py
# Description:      Codificação do exemplo do livro do Perckovic, página 327.
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
# History:          v1.0 02/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from tkinter import Tk, Text, BOTH
from turtle import width


def record(event):
    print('char = {}'.format(event.keysym))


raiz = Tk()

text = Text(raiz, width=20, height=5)
text.bind('<KeyPress>', record)
text.pack(expand=True, fill=BOTH)

raiz.mainloop()
