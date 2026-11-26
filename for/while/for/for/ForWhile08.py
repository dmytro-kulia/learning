password = "qwerty"
new_password = input("Введите пароль:" )
while new_password != password:
    print("Неверный пароль, попробуйте еще раз!")
    new_password = input("Введите пароль:" )
print("Доступ разрешён.")