secret = 42
attempts = 0
number = int(input("Введите число:" ))
attempts = attempts + 1
while number != secret:
    if number < secret:
        print ("Больше")
    else:
        print ("Меньше")
    number = int(input("Введите следующую число:" ))
    attempts = attempts + 1
print ("Вы угадали число и вы использовали:", attempts, "попыток.")