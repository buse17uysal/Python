import turtle

oyun=turtle.Screen()
oyun.setup(500,500)
oyun.tracer(0)

boy=0.5
en=5
sayac=0

skor=turtle.Turtle()
skor.color("blue")
skor.penup()
skor.goto(0,210)
skor.write("Skor: 0",align="center",font=("Arial",20,"bold"))
skor.hideturtle()

gameover=turtle.Turtle()
gameover.color("blue")
gameover.penup()
gameover.goto(0,0)
gameover.hideturtle()

tahta=turtle.Turtle()
tahta.shape("square")
tahta.shapesize(stretch_wid=boy,stretch_len=en)
tahta.color("black")
tahta.penup()
tahta.goto(0,-200)

top=turtle.Turtle()
top.shape("circle")
top.shapesize(0.5)
top.color("red")
top.penup()
top.goto(0,0)
hareketx=0.2
harekety=0.2

def gitme():
    x=tahta.xcor()
    tahta.setx(x)
    
def sag_git():
    x=tahta.xcor()
    x+=50
    tahta.setx(x)
    if tahta.xcor()+(en/2)>220:
        oyun.onkeypress(gitme,"Right")
    
def sola_git():
    x=tahta.xcor()
    x-=50
    tahta.setx(x)
    if tahta.xcor()-(en/2)<-220:
        oyun.onkeypress(gitme,"Left")
    
oyun.listen()
oyun.onkeypress(sag_git,"Right") 
oyun.onkeypress(sola_git,"Left")  

while 1:
    oyun.update()
    top.setx(top.xcor()+ hareketx)
    top.sety(top.ycor()+ harekety)
    
    if top.xcor()<-240 or top.xcor()>240:
        hareketx=-hareketx
        
    elif top.ycor()>240:
        harekety=-harekety    
        
    elif top.ycor()<-240:
        skor.clear()
        skor.write("Skor: {}".format(sayac),align="center",font=("Arial",20,"bold"))
        gameover.write("Oyun Bitti!",align="center",font=("Arial",50,"bold"))
        oyun.mainloop()
        break
        
    elif top.xcor()>=tahta.xcor()-(en*2) and top.xcor()<=tahta.xcor()+(en*2) and top.ycor()<=tahta.ycor():
        top.sety(-200)
        harekety=-harekety
        en=en/1.1
        if en==2:
            en=en
        sayac+=1
        tahta.shapesize(stretch_wid=boy,stretch_len=en)
        skor.clear()
        skor.write("Skor: {}".format(sayac),align="center",font=("Arial",20,"bold"))
        
    else:
        pass



