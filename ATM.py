print("*************************************")
print("Hoşgeldiniz")
print("İşlemler:\n1. Bakiye Sorgulama\n2. Para Yatırma\n3. Para Çekme\nÇıkmak için q'ya basın.")
print("*************************************")

bakiye = 1000

while True :
    islem = int(input("İşlem Seçiniz : "))

    if islem == "q":
        print("Yine Bekleriz...")
        break
    elif islem == 1:
        print("Bakiyeniz : {}".format(bakiye))
    elif islem == 2:
        miktar = int(input("Miktarı Giriniz: "))
        print("İşleminiz gerçekleştiriliyor.")
        bakiye += miktar
        print("Bakiyeniz : {}".format(bakiye))
    elif islem == 3:
        miktar = int(input("Miktarı Giriniz: "))
    
        if (bakiye - miktar < 0):
            print("Yetersiz Bakiye...")
            continue
        bakiye -= miktar
        print("Bakiyeniz : {}".format(bakiye))
    else:
        print("Geçersiz İşlem")
