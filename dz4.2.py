import random


class Cipher:
    def __init__(self, number):
        self.__result = self.__calculate(number)

    def __calculate(self, number):
        operation = random.choice(["+", "*", "-"])

        if operation == "+":
            return number + random.randint(1, 10)
        elif operation == "*":
            return number * random.randint(2, 5)
        else:
            return number - random.randint(1, 10)

    def __str__(self):
        return str(self.__result)


number = int(input("Введіть число: "))

cipher = Cipher(number)

print("Результат:", cipher)