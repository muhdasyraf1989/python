"""
BMI = Weight (kg) / [Height (m) x Height (m)]

Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
"""


def calculate_bmi(w,h):
    return w/(h*h)

def bmi_category(cat):
    return cat

mesej = """ 
APLIKASI INI MENGIRA BMI
SILA MASUKKAN BERAT DALAM KILOGRAM DAN TINGGI DALAM METER.
"""

print(mesej)
w = float(input("Berat?"))
h = float(input("Tinggi?"))
cat = float(calculate_bmi(w,h))

print("BMI ANDA:", calculate_bmi(w,h))

if cat >= 30:
 print("OBESITY")
elif cat >= 25 and cat <= 29.9:
 print("Overweight")
elif cat >= 18.5 and cat <= 24.9:
 print("Normal Weight")
else:
 print("Underweight")
