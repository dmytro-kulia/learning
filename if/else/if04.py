print ("Придумайте пароль и напишите его ниже!")
password = "secret"
word = input("Введите пароль: ")
if password == word:
    print ("Доступ разрещён.")
else:
    print ("Неверный пароль.")