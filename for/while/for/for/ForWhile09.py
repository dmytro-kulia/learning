total = int(0)
number = int(input("Введите число:" ))
while number != 0:
    total = total + number
    number = int(input("Введите следующее число:" ))
print (total)