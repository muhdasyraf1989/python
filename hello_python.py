no_sifir = int(input("Jadual sifir apa? "))
for x in range(1,13):
   output = "{} X {} = {}"
   answer = x * no_sifir
   print(output.format(x,no_sifir,answer))