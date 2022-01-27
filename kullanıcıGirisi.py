sys_kullanıcı_adı  = "Fatmanur"
sys_parola = "123456"

giris_hakkı = 3


while True:
    kullanıcı_adı = input("Kullanıcı Adı : ")
    parola = input("Parola : ")
    if (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parolayı yanlış girdiniz...")
        giris_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı adı ve parolayı yanlış girdiniz")
        giris_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı adını yanlış girdiniz")
        giris_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı...")
        break
    if (giris_hakkı == 0):
        print("Giriş hakkınız bitti...")
        break