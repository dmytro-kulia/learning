print ("Вы вводите сумму к оплате, а программа считаем вам скидку.")
preis = float(input("Введите сумму: "))
if preis >= 100:
    print ("Сумма к оплате:", preis * 0.90)
elif preis >= 50:
    print ("Сумма к оплате:", preis * 0.95)
else:
    print (preis)