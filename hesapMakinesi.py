print("................................................ \n1- Birinci İşlem : Toplama\n2- İkinci İşlem : Çıkarma\n3- Üçümcü İşlem : Çarpma\n4- Dördüncü İşlem : Bölme\n................................................")

a = int(input("Birinci Sayı : "))
b = int(input("İkinci Sayı : "))

islem = int(input("İşlemi Giriniz..."))
   
if islem == 1:
    print("{} ile {} toplamı {} dir.".format(a,b,a+b))
elif islem == 2:
    print("{} ile {} farkı {} dir.".format(a,b,a-b))
elif islem == 3:
     print("{} ile {} çarpımı {} dir.".format(a,b,a*b))
elif islem == 4:
     print("{} ile {} bölümü {} dir.".format(a,b,a/b)) 
else:
    print("Geçerli bir işlem giriniz.")   
