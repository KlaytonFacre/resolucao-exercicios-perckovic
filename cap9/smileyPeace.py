from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE
import os

print(os.getcwd())
janela_principal = Tk()

# Widgets da janela principal
texto = Label(janela_principal, font=('Helvetica', 16, 'bold italic'), foreground='white',
              background='black', padx=25, pady=10, text='A pas começa com um sorriso')
gato = PhotoImage(
    file='/home/facrekcfm/Documents/Develop/Python programming/Perckovic/cap9/giphy.gif')
gato_label = Label(janela_principal, image=gato, borderwidth=3, relief=RIDGE)

simpson = PhotoImage(
    file='/home/facrekcfm/Documents/Develop/Python programming/Perckovic/cap9/homer.gif')
simpson_label = Label(janela_principal, image=simpson)

# Posicionamento dos widgets
texto.pack(side=BOTTOM)
gato_label.pack(side=LEFT)
simpson_label.pack(side=RIGHT)

janela_principal.mainloop()
