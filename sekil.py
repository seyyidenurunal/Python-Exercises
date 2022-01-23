istek = int(input("Geometrik Şekillerden Birini Seçin :\n1- Dötrgen\n2-  Üçgen\nCevap : "))


if istek == 1:
    print("Dörtgenin kenar uzunluklarını giriniz")
    a = input("Kenar 1 : ")
    b = input("Kenar 2 : ")
    c = input("Kenar 3 : ")
    d = input("Kenar 4 : ")
    if a == b == c == d:
        print("Kare")
    elif a ==  c and  b == d or a == b and c == d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")
elif istek == 2:
     print("Üçgenin kenar uzunluklarını giriniz")
     x = input("Kenar 1 : ")
     y = input("Kenar 2 : ")
     z = input("Kenar 3 : ")
     if ( abs(x+y) > z and abs(x+z) > y and abs(y+z) > x):
        if x == y == z:
         print("Eşkenar Üçgen")
        elif x == y or x == z or y == z:
         print("İkizkenar Üçgen")
        else:
         print("Çeşitkenar Üçgen")
     else:
         print("Üçgen Belirtmiyor.")
else:
    print("Geçersiz")