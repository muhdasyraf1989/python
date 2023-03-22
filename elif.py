"""
Markah>=80 dan <=100 ➡️ gred A
Markah>=70 dan <80 ➡️ gred B
Markah>=50 dan <70 ➡️ gred C
Markah>=40 dan <50 ➡️ gred D
Markah<40 ➡️ gred F
"""

mark = float(input("Masukkan Markah :"))
gred = ""

if mark >= 80 and mark <= 100:
 print("Gred A")
elif mark >= 70 and mark < 80:
 print("Gred B")
elif mark >= 50 and mark < 70:
 print("Gred C")
elif mark >= 40 and mark < 50:
 print("Gred D")
elif mark < 40:
 print("Gref F")
else:
 print("Please Enter 1 to 100")
        