from tkinter import * #interface
from tkinter import filedialog #pedir arquivo
import pandas as pd #biblioca para trabalhar com csv
import os 

os.system("cls")

def abrirArquivo():
    filepath=filedialog.askopenfilename()
    file=open(filepath, 'r') #leia
    print(file.read())
    file.close()

tela=Tk()
button=Button(text='Abrir', command=abrirArquivo)
button.pack()
tela.mainloop()



