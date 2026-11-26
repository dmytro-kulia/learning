print("Это программа поможет найти тебе большее число из двух.")
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
if number2 > number1:
    print("Второе число больше первого.")
elif number1 < number2:
    print("Первое число больше второго.")
elif number1 == number2:
    print("Числа равны.")