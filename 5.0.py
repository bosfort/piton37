import colorama
from colorama import Fore, Back, Style

colorama.init()

# Інтроспекція
print("Назва бібліотеки:", colorama.__name__)
print("Файл бібліотеки:", colorama.__file__)

print("\nАтрибути та методи:")
print(dir(colorama))

# Приклади використання
print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Fore.BLUE + "Синій текст")

print(Back.YELLOW + "Текст на жовтому фоні")

print(Style.BRIGHT + "Жирний текст")

# Повернення стандартного стилю
print(Style.RESET_ALL + "Звичайний текст")