import random
import tkinter as tk

oyun=tk.Tk()
oyun.geometry("300x300")
sayac=0

def dogru_mu(): 
    global sayac
    if renkler[7]==kutu.get():
        sayac+=1
        say.config(text=str(sayac))
        yazi_degistir()
        yazi.config(text=str(renkler[0]),fg=str(renkler[7]),font=30)  
          
    elif renkler[7]!=kutu.get():
        sayac-=1
        say.config(text=str(sayac))
        yazi_degistir()
        yazi.config(text=str(renkler[0]),fg=str(renkler[7]),font=30)
        
    elif sayac<0:
        yazi.config(text="Oyun Bitti",font=30)
        say.config(text="-1 ",font=30)  
                    
renkler=["pink","black","purple","green","orange","red","yellow","blue"]

def yazi_degistir():
    degisen_yazi=random.shuffle(renkler)
    return  degisen_yazi

yazi_degistir()
yazi=tk.Label(text=str(renkler[0]),fg=str(renkler[7],),font=30)
yazi.pack()

kutu=tk.Entry()
kutu.pack()

buton=tk.Button(text="Ok",command=dogru_mu,font=30)
buton.pack()

say=tk.Label(text="0",font=30)
say.pack()

tk.mainloop()

