print("""
**********************************
        ATM GİRİŞ PROGRAMI
**********************************
""")
kayitli_kullanici_adi= "Vales"
kayitli_sifre= "asdre123"
giris_hakki=2
bakiye = 1000

while True:
 kullanici_adi= (input("Kullanıcı adınızı giriniz: "))
 kullanici_sifre= (input("Şifrenizi giriniz: "))    
 if (kullanici_adi != kayitli_kullanici_adi and kullanici_sifre == kayitli_sifre):
        print("Kullanıcı adınız hatalıdır yeniden deneyiniz...")
        giris_hakki -= 1
 elif (kullanici_sifre != kayitli_sifre and kullanici_adi== kayitli_kullanici_adi):
   giris_hakki-=1
   print("Girmiş olduğunuz şifre hatalıdır yeniden deneyiniz...")
 else:
    print("""
    Başarıyla giriş yaptınız.
          İşlemler;
          1) Bakiye sorgulama (s)
          2) Para çekme (ç)
          3) Para yatırma (y)
          4) Çıkış (q)
""")
    islem=input("İşlem Seçiniz: ")
    if (islem=="s"):
            print("Bakiyeniz: ", bakiye)
            yapilacak_islem=input("başka yapılacak işlemi seçin: ")
            if (yapilacak_islem=="q"or "ç"or"y"):
                if (yapilacak_islem=="ç"):
                    print("Bakiyeniz: " , bakiye)
                    miktar= int(input("Çekilecek miktarı giriniz: "))
                    bakiye-=miktar
                    print("Kalan bakiyeniz: ", bakiye)
                    sonislem=input("Çıkış için q ya basın: ")
                    if (sonislem=="q"):
                        print("sistemden çıkış yaptınız.")
                        break
                elif(yapilacak_islem=="y"):
                    y_miktar=int(input("Yatıralacak miktarı giriniz: "))
                    bakiye+=y_miktar
                    ("Güncel bakiyeniz: ",bakiye)
                    sonislem=input("Çıkış için q ya basın: ")
                    if (sonislem=="q"):
                        print("sistemden çıkış yaptınız.")
                        break
                elif (yapilacak_islem=="q"):
                    print("sistemden  çıkış yaptınız.")
                    break
            else:
                print("Geçersiz işlem ")
    elif (islem == "ç"):
            print("Bakiyeniz: " , bakiye)
            miktar= int(input("Çekilecek miktarı giriniz: "))
            bakiye-=miktar
            print("Kalan bakiyeniz: ", bakiye)
            yapilacak_islem=input("başka yapılacak işlemi seçin: ")
            if (yapilacak_islem=="q"or "s"or"y"):
                if (yapilacak_islem=="s"):
                    print("Bakiyeniz: ", bakiye)
                    sonislem=input("Çıkış için q ya basın: ")
                    if (sonislem=="q"):
                        print("sistemden çıkış yaptınız.")
                        break
                elif(yapilacak_islem=="y"):
                    y_miktar=int(input("Yatıralacak miktarı giriniz: "))
                    bakiye+=y_miktar
                    ("Güncel bakiyeniz: ",bakiye)
                    sonislem=input("Çıkış için q ya basın: ")
                    if (sonislem=="q"):
                        print("sistemden çıkış yaptınız.")
                        break
                elif (yapilacak_islem=="q"):
                    print("sistemden  çıkış yaptınız.")
                    break
            else:
                print("Geçersiz işlem ")
    elif(islem=="y"):
       y_miktar=int(input("Yatıralacak miktarı giriniz: "))
       bakiye+=y_miktar
       print("Güncel bakiyeniz: ",bakiye)
       yapilacak_islem=input("başka yapılacak işlemi seçin: ")
       if (yapilacak_islem=="q"or "s"or"ç"):
                if (yapilacak_islem=="s"):
                    print("Bakiyeniz: ", bakiye)
                    sonislem=input("Çıkış için q ya basın: ")
                    if (sonislem=="q"):
                        print("sistemden çıkış yaptınız.")
                        break
                elif(yapilacak_islem=="ç"):
                    print("Bakiyeniz: " , bakiye)
                    miktar= int(input("Çekilecek miktarı giriniz: "))
                    bakiye-=miktar
                    print("Kalan bakiyeniz: ", bakiye)
                    sonislem=input("Çıkış için q ya basın: ")
                    if (sonislem=="q"):
                        print("sistemden çıkış yaptınız.")
                        break
                elif (yapilacak_islem=="q"):
                    print("sistemden  çıkış yaptınız.")
                    break
                else:
                    print("Geçersiz işlem ")

    elif(islem=="q"):
       print("sistemden  çıkış yaptınız.")   
    else:
       print("Geçersiz işlem")
    break
 if (giris_hakki==0):
   print("hakkınız bitti şahmat liberal")
   break