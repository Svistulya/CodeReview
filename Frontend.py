from tkinter import *
from tkinter import ttk
import sqlite3

con = sqlite3.connect("SteamSale.db")
cur = con.cursor()
 
root = Tk()
root.title("Steam Sale")
root.geometry("1200x700") 
 
cur.execute("SELECT * FROM SteamSale")

columns = ("game", "price_b", "price_dis", "price_a")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
 
tree.heading("game", text="Название")
tree.heading("price_b", text="Цена до скидки")
tree.heading("price_dis", text="Скидка")
tree.heading("price_a", text="Цена")
 
for person in cur.fetchall():
    tree.insert("", END, values=person)
 
root.mainloop()