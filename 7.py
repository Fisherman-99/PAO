from tkinter import *
def printer(event):
    print ("Privet")
root = Tk()
root.title("Кнопка")
root.geometry("400x400")

entry = Entry()
entry.pack(anchor=NW, padx=6, pady=6)
python_logo = PhotoImage(file="./kot2.png")

label = Label(image=python_logo, text="Нажми на кнопку получишь результат", compound='top', font=("Arial", 14))
label.pack()
but = Button(root)
but["text"] = "Печать"
but.bind("<Double-ButtonPress-1>",printer)
but.pack(expand=True)
root.mainloop()