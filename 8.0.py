def check_age(age):
    try:
        assert age >= 18
        print("Ви можете використовувати цей сервіс")
    except AssertionError:
        print("Вам має бути 18 років або більше")


age = int(input("Введіть ваш вік: "))
check_age(age)