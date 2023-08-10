def Urunler():
    adet=int(input("Kaç adet ürün gireceksiniz: "))
    
    for i in range(0,adet):   
        urun=input("Ürün kategorisi seçiniz(k/e/c): ")
        urun.lower
        if urun== "k":
            urun_adi=input("Ürün adı giriniz: ")
            filename1="kadin_urunler.txt"
            with open(filename1,"a") as file1:
             file1.write(str(urun_adi + "\n"))
             file1.close 
             
        elif urun== "e":
            urun_adi=input("Ürün adı giriniz: ")
            filename2="erkek_urunler.txt"
            with open(filename2,"a") as file2:
                file2.write(str(urun_adi + "\n"))
                file2.close
    
        elif urun=="c":
            urun_adi=input("Ürün adı giriniz: ")
            filename3="cocuk_urunler.txt"
            with open(filename3,"a") as file3:
                file3.write(str(urun_adi + "\n"))
                file3.close

        else:
            print("Hatalı giriş")
    
    return

if __name__=="__main__":
    Urunler()
   
