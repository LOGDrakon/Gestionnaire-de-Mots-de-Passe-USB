import random
import sqlite3
import string
from tkinter import *
from tkinter import ttk
from functools import partial

passwd = ""

conn = sqlite3.connect("F:/PswdK.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS pswd(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     site TEXT,
     passwd TEXT
)
""")
conn.commit()

def valid(entrySite, cursor, label1, conn) :
    site = entrySite.get()
    cursor.execute("""SELECT passwd FROM pswd WHERE site=?""", (site,))
    response = cursor.fetchone()
    psd = response
    label1["text"] = psd
    print(psd)
    conn.close()

APswd = Tk()
APswd.minsize(500, 250)
APswd.maxsize(500, 250)
APswd.title("Récupérer un mot de passe")
label1 = Label(APswd, text="Mot de passe")
label1.pack()
entrySite = StringVar()
entry1 = Entry(APswd, textvariable=entrySite)
entry1.pack()
button1 = ttk.Button(APswd, text="Valider", command=partial(valid, entrySite, cursor, label1, conn))
button1.pack()
APswd.mainloop()