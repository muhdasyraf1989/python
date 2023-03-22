"""
LATIHAN 3-1 (ERROR HANDLING)

Dlm tugasan ini, anda diminta utk mengubah kod dlm project yg menentukan gred 
berdasarkan markah.

Buat satu function yg namanya Get_Score yg akan memulangkan nilai antara 0 dan 100
jika pengguna memasukkan nombor skor yg betul.  Jika ada masalah, function ini akan 
memulangkan angka -1

Pastikan arahan2 dlm function itu diletakkan dlm try block.  Anda juga perlu ada satu
Except blok utk sebarang isu yg berlaku.

Utk Except blok, anda boleh tuliskan kod berikut

except Exception as e:
     result = -1
"""

#function to determining the grade


def GetGrade(score):
    tmpGrade = ""

    if score >= 80 and score <= 100:
        tmpGrade = "A"
    elif score >= 70 and score < 80:
        tmpGrade = "B"
    elif score >= 50 and score < 70:
        tmpGrade = "C"
    elif score >= 40 and score < 50:
        tmpGrade = "D"
    elif score < 40:
        tmpGrade = "F"
    else:
        tmpGrade = "-undefined-"

    return tmpGrade


#function to get score from the user
#the accepted score is between 0 and 100 only

def GetScore():
    tmpScore = -1

    try:
        tmpScore = float(input("Enter the score: "))
        if not (tmpScore >= 0 and tmpScore <= 100):
          tmpScore = -1
    except Exception as e:
        tmpScore = -1

    return tmpScore


# testing the codes

# get a score from the user
while True:
    s = GetScore()
    if s != -1: 
        break 
    else:
        print("Please enter a number between 0 and 100 only")

#print out the grade based on the score given
print(GetGrade(s))



  


