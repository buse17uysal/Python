import turtle

shape=turtle.Turtle()
ic_aci=int(turtle.textinput("Açı Bilgisi","Şeklin iç açısını giriniz"))
renk=turtle.textinput("Renk","Şelin rengini giriniz: ")
dis_aci=180 - ic_aci
kenar=int(360/dis_aci)
shape.begin_fill()
shape.pencolor(renk) 
shape.color(renk) 

for i in range(0,kenar):
    shape.forward(100)
    shape.left(dis_aci)
       
shape.end_fill()    
      
turtle.done()

