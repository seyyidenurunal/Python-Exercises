isValid = True

while isValid:
    i = 1
    toplam = 0

    sayi = int(input("Sayı : "))

    isValid = False
    while i < sayi:
       
        if sayi % i == 0:
            toplam += i
        i += 1

    if toplam == sayi:
        print(sayi, " Mükemmel bir sayıdır.")
    else:
        print(sayi, " Mükemmel bir sayı değildir.")

    cıkıs = input("Çıkmak istiyorsanız q'ya, devam etmek için herhangi bir harfe basın.")

    if cıkıs == "q":
        print("Çıkış yapılıyor")
        isValid = False
    else:
        isValid = True

