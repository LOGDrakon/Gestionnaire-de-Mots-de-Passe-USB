import random
import sqlite3
import string
from tkinter import *
from tkinter import ttk
from functools import partial

length_of_string = 64
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
    passwd = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length_of_string))
    cursor.execute("""
    INSERT INTO pswd(site, passwd) VALUES(?, ?)""", (site, passwd))
    label1["text"] = passwd
    print(passwd)
    conn.close()

APswd = Tk()
APswd.minsize(500,250)
APswd.maxsize(500,250)
APswd.title("Générer un mot de passe")
label1 = Label(APswd, text="Mot de passe")
label1.pack()
entrySite = StringVar()
entry1 = Entry(APswd, textvariable=entrySite)
entry1.pack()
button1 = ttk.Button(APswd, text="Valider", command=partial(valid,entrySite, cursor, label1, conn))
button1.pack()
APswd.mainloop()