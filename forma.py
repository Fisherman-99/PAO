import Magazin
from tkinter import *
root = Tk()
ent = Entry (root, bg="white", fg="black") #Ввод названия
ent.place(x=150, y=0)
ent1 = Entry (root, bg="white", fg="black") #Ввод номера
ent1.place(x=150, y=30)
ent2 = Entry (root, bg="white", fg="black") #Ввод количества
ent2.place(x=150, y=60)
ent3 = Entry (root, bg="white", fg="black") #Ввод цены
ent3.place(x=150, y=90)
def printer(event):
    new = Magazin.Sklad(ent1.get(), ent.get(), ent2.get(), ent3.get())
    #print(new.number, new.name, new.group, new.kolvo, new.price)
    new.display_info()
    print ("Privet")

root.title("Кнопка")
root.geometry("400x250")
#python_logo = PhotoImage(file="./kot2.png")
#image=python_logo,
label = Label( text="Название", compound='righ', font=("Arial", 15))
label.place(x=20, y=0)
label1 = Label( text="Номер", compound='righ', font=("Arial", 15))
label1.place(x=20, y=30)
label1 = Label( text="Количество", compound='righ', font=("Arial", 15))
label1.place(x=20, y=60)
label1 = Label( text="Цена", compound='righ', font=("Arial", 15))
label1.place(x=20, y=90)
label = Label( text="Нажми на кнопку получишь результат", compound='top', font=("Arial", 15))
label.place(x=20, y=140)
but = Button(root)
but["text"] = "Не нажимать"
but.bind("<Double-ButtonPress-1>",printer)
#but.pack(expand=True)
but.place(x=180, y=210, anchor="c", width=100, height=50)
root.mainloop()