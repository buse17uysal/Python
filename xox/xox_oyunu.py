from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("XOX")
sayac=0
secilen=None
buton=[[0,0,0],
       [0,0,0],
       [0,0,0]]

def kazanma(row,col):
    if (all(buton[row][i]["text"]==secilen for i in range(3))):
        for i in range(3):
            buton[row][i].config(background="green")
        messagebox.showinfo(title="Sonuç", message=secilen +" KAZANDI!")
        return True
        
    if (all(buton[i][col]["text"]==secilen for i in range(3))):
        for i in range(3):
            buton[i][col].config(background="green")
        messagebox.showinfo(title="Sonuç", message=secilen + " KAZANDI!")   
        return True
        
    if (buton[0][0]["text"]==secilen and buton[1][1]["text"]==secilen and buton[2][2]["text"]==secilen):
        buton[0][0].config(background="green")
        buton[1][1].config(background="green")
        buton[2][2].config(background="green")
        messagebox.showinfo(title="Sonuç", message=secilen + " KAZANDI!")
        return True
        
    if (buton[0][2]["text"]==secilen and buton[1][1]["text"]==secilen and buton[2][0]["text"]==secilen):
        buton[0][2].config(background="green")
        buton[1][1].config(background="green")
        buton[2][0].config(background="green")
        messagebox.showinfo(title="Sonuç", message=secilen + " KAZANDI!")    
        return True
        
    elif all(buton[i][j]["text"] != " " and False for i in range(3) for j in range(3)):
        for i in range(0,3):
            for j in range (0,3):
                buton[i][j].config(background="red")
        messagebox.showinfo(title="Sonuç", message=" TEKRAR DENEYİNİZ!")       
    return False     
 
for i in range(0,3):
    for j in range (0,3):
        buton[i][j]=Button(root,text=" ",width=9,height=5,command=lambda 
                           row=i, col=j: tiklama(row, col))
        buton[i][j].grid(row=i,column=j)  
         
def tiklama(row,col):
    global sayac,secilen
    if buton[row][col]["text"] == " ":
        if sayac%2==0:
            secilen="X"

        elif sayac%2==1:
            secilen="O"  
                  
        buton[row][col].config(text=secilen)
        kazanma(row,col) 
        sayac+=1
        return secilen
    
root.mainloop()



