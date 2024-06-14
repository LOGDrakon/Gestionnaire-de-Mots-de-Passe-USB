import random
import sqlite3
import string
from tkinter import *
from tkinter import ttk

length_of_string = 64
passwd = ""

def addSite() :
    MPass.destroy()
    exec(open("addPaswd.py").read())
def getSite() :
    MPass.destroy()
    exec(open("getPaswd.py").read())

MPass = Tk()
MPass.minsize(500, 250)
MPass.maxsize(500, 250)
MPass.title("MPassword")
button1 = ttk.Button(MPass, text="Générer un mot de passe", command=addSite)
button1.pack()
button2 = ttk.Button(MPass, text="Récupérer un mot de passe", command=getSite)
button2.pack()
mainloop()