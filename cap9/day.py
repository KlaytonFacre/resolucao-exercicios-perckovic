# Instruções import e manipulador de evento
# compute() calcula e exibe o dia da semana
from calendar import week, weekday
from time import strftime, strptime
from tkinter import END, Button, Entry, Tk, Label
from tkinter.messagebox import showinfo


def compute():
    global dateEnt
    date = dateEnt.get()

    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

    showinfo(message='{} foi {}'.format(date, weekday))

    dateEnt.delete(0, END)


raiz = Tk()

# Label
label = Label(raiz, text='Digite a data:')
label.grid(row=0, column=0)

# Entry
dateEnt = Entry(raiz)
dateEnt.grid(row=0, column=1)

# Button
button = Button(raiz, text='Entrar', command=compute)
button.grid(row=1, column=0, columnspan=2)

raiz.mainloop()
