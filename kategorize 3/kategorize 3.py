import xlsxwriter 

file=xlsxwriter.Workbook("stok.xlsx")
adet=int(input("Kaç adet ürün gireceksiniz: "))
frame=file.add_worksheet()
frame.write(0,0,"Ürün Adı")
frame.write(0,1,"Beden")
frame.write(0,2,"Stok")

u_row,b_row,s_row=1,1,1

for i in range(0,adet):
    urun=input("Ürün giriniz: ").upper()
    frame.write(u_row,0,urun)
    u_row+=1
    
    beden=input("Beden giriniz: ").upper()
    frame.write(b_row,1,beden)
    b_row+=1
    
    stok=int(input("Stok giriniz: "))
    frame.write(s_row,2,stok)
    s_row+=1
    
grafik=file.add_chart({'type': 'column'})    
grafik.add_series({'values':'=Sheet1!C2:C11'})
frame.insert_chart('D1',grafik)
file.close()

