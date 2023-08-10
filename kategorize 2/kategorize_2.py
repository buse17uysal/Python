import xlsxwriter 

file=xlsxwriter.Workbook("kategorize.xlsx")
frame=file.add_worksheet()
adet=int(input("Kaç adet ürün gireceksiniz: "))
frame.write(0,0,"Kadın Giyim")
frame.write(0,1,"Erkek Giyim")
frame.write(0,2,"Çocuk Giyim")

k_row,e_row,c_row=1,1,1

for i in range(0,adet):
    urun=input("Ürün kategorisi seçiniz(k/e/c): ")
    urun.lower
    if urun== "k":
        col=0
        urun_adi=input("Ürün adı giriniz: ")
        frame.write(k_row,col,urun_adi) 
        k_row+=1  
             
    elif urun== "e":
        col=1
        urun_adi=input("Ürün adı giriniz: ")
        frame.write(e_row,col,urun_adi)
        e_row+=1
        
    elif urun=="c":
        col=2
        urun_adi=input("Ürün adı giriniz: ")
        frame.write(c_row,col,urun_adi)    
        c_row+=1    
       
    else:
        print("Hatalı giriş")

file.close()

