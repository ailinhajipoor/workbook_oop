from tkinter import *


def Insert_data():



def Clear_entry():
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")


root = Tk()
root.configure(bg="orange")
l1 = Label(root, text="Name", bg="orange")
l2 = Label(root, text="Last Name", bg="orange")
l3 = Label(root, text="Age", bg="orange")
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
b1 = Button(root, text="Insert", bg="orange", command=Insert_data)
b2 = Button(root, text="Reset", bg="orange", command=Clear_entry)
# ----------grid-----------
l1.grid(row=0, column=0, padx=5, pady=5)
e1.grid(row=0, column=1, padx=5, pady=5)
l2.grid(row=1, column=0, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
l3.grid(row=2, column=0, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)
b1.grid(row=3, column=0, padx=5, pady=5)
b2.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
