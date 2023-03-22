def Luas_Segiempat (panjang, lebar):
    return panjang*lebar

def Ukurlilit_Segiempat(panjang, lebar):
    return 2*(panjang + lebar)

mesej = """
APLIKASI INI BOLEH MENGIRA LUAS DAN UKURLILIT
SEGIEMPAT
"""
print(mesej)
p = float(input("Panjang? "))
l = float(input("Lebar? "))

print("Luas segiempat = ", Luas_Segiempat(p,l))
print("Ukurlilit Segiempat = ", Ukurlilit_Segiempat(p,l))