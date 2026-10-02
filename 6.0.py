try:
    number = input("Введіть число: ")
    number = int(number)
    print("Ціле число:", number)

except ValueError:
    print("Помилка: введені дані не можна перетворити на число!")