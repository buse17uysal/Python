from googletrans import Translator, LANGUAGES


def metni_cevir(metin, kullanilan_dil, cevrilen_dil):
    translator = Translator()
    ceviri = translator.translate(metin, src=kullanilan_dil, dest=cevrilen_dil)
    return ceviri.text

if __name__ == "__main__":
    print("Desteklenen Dil Sayisi:", len(LANGUAGES))

    kullanilan_dil = input("Çevirmek istediğiniz metnin dil kodunu giriniz: ")
    metin = input("Çevirmek istediğiniz metni giriniz: ")
    cevrilen_dil = input("Çevrilecek dil kodunu giriniz: ")

    ceviri = metni_cevir(metin, kullanilan_dil, cevrilen_dil)
    print("Çeviri Sonucu:", ceviri)

