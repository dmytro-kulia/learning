print ("Я вам помогу перевести сумму с евро в гривны, ниже введите сумму а потом курс.")
euro = float(input("Введите сумму в Евро: "))
kurs_ukr = float(input("Введите курс гривны: "))
result = euro * kurs_ukr
print(f"{euro} Евро это {result} Гривен.")