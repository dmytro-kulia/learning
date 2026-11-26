print ("Программа правильно склоняет твой возраст.")
age = int(input("Введите ваш возраст: "))
new_age = age + 1
if 11 <= new_age % 100 <= 14:
    word = "лет"
elif new_age % 10 == 1:
    word = "год"
elif 2 <= new_age % 10 <= 4:
    word = "года"
else:
    word = "лет"
print(f"В следующем году вам будет {new_age} {word}.")