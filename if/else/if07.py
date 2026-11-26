print ("Программа поможет вам из 3 чисел найти самое большое.")
num1 = float(input("Введите певое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
if num1 >= num2 and num1 >= num3:
    print ("Самое большое число: ", num1)
elif num2 >= num1 and num2 >= num3:
    print ("Самое большое число: ", num2)
else:
    print ("Самое большое число: ", num3)