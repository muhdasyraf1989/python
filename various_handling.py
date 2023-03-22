"""
LATIHAN 3-2 (Various File Handlings Example)
"""

FileName: test_pelbagai.py

import os

fn = input("Apa nama fail? ")

menu_txt = """
PILIHAN MENU
============

1 - Cari fail
2 - Buat fail baru
3 - Kemaskini fail
4 - Padam fail
"""
print(menu_txt)

pilihan_pengguna = int(input("Masukkan nombor pilihan anda: "))
if pilihan_pengguna == 1:
    #cari fail - fail tu ada ke tak?
    if os.path.exists(fn):
        print(fn, "wujud")
    else:
        print(fn, "tak wujud")
elif pilihan_pengguna == 2:
    #buka fail baru menggunakan mode "x"
    f = open(fn, "x")
    f.write("Yey! Berjaya dicipta")
    print("Fail",fn,"berjaya dicipta")
    f.close()
elif pilihan_pengguna == 3:
    # kemaskini fail dgn mode "a"
    f = open(fn, "a")
    f.write("\n\nData berjaya ditambah")
    f.close()
    print(fn, "berjaya dikemaskini")
elif pilihan_pengguna == 4:
    # padam fail jika wujud
    os.remove(fn)
    print(fn,"berjaya dihapuskan")
else:
    print("Maaf! Hanya nombor 1 hingga 4 sahaja yg diterima")
