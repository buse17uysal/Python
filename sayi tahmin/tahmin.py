import random

random_sayi= random.randint(1,100)
sayac=0
for i in range (0,100):
    sayi=int(input("1-100 arasında sayı giriniz: "))
    sayac+=1
    if sayi==random_sayi:
        print(sayac,". tahmin")
        print("Doğru tahmin ettiniz!")
        break
  
    elif sayi<random_sayi:
        print(sayac, ". tahmin")
        print("Daha büyük bir sayı giriniz!")  
     
    elif sayi>random_sayi:
        print(sayac,". tahmin")
        print("Daha küçük bir sayı giriniz!")  
    
    else:
        print("Hatalı giriş!")    
        
