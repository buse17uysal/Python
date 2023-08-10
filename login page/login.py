import tkinter as tk

window=tk.Tk()
window.geometry("300x125")
label=tk.Label(text=" ")
label.grid(row=3,column=1)
label2=tk.Label(text=" ")
label2.config(text=" ") 

def isTrue():
    label2.config(text=" ")
    label.config(text=" ")
    if ent1.get()=="egemen" and ent2.get()=="yazilim":
        label.config(text="Succesful Login!", font="Calibri",fg="green")
    else:
        label2.config(text="Try Again!", font="Calibri",fg="red")
        label2.grid(row=3,column=1)  
    
lbl1 = tk.Label(text="User Name : ", font="Calibri",  width=15)
lbl1.grid(row=0, column=0)

ent1 = tk.Entry(font="Calibri")
ent1.grid(row=0, column=1)

lbl2 = tk.Label(text="Password : ", font="Calibri",  width=15)
lbl2.grid(row=1, column=0)

ent2 = tk.Entry(font="Calibri")
ent2.grid(row=1, column=1)

button = tk.Button(text="LOGIN", font="Calibri",command=isTrue)
button.grid(row=2, column=1)
  
tk.mainloop()

