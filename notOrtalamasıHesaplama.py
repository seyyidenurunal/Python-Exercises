vize = int(input("VİZE 1 :"))
vize2 = int(input("VİZE 2 :"))
final = int(input("FİNAL :"))


notOrtalaması = (vize * 30 / 100) + (vize2 * 30 / 100) + (final * 40 / 100) 

gecmeNotu = ""

if notOrtalaması >= 90:
    gecmeNotu = "AA"
elif notOrtalaması >= 85:
    gecmeNotu = "BA"
elif notOrtalaması >= 80:
    gecmeNotu = "BB"
elif notOrtalaması >= 75:
    gecmeNotu = "CB"
elif notOrtalaması >= 70:
    gecmeNotu = "CC"
elif notOrtalaması >= 65:
    gecmeNotu = "DC"
elif notOrtalaması >= 60:
    gecmeNotu = "DD" 
elif notOrtalaması >= 55:
    gecmeNotu = "FD"
else:
    gecmeNotu = "FF"

print("GEÇME NOTU : {}".format(gecmeNotu));
