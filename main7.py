points = int(input("Введіть кількість балів: "))

if points <= 49:
    print("незадовільно")
elif points <= 69:
    print("задовільно")
elif points <= 89:
    print("добре")
elif points <= 100:
    print("відмінно")
else:
    print("Некоректна кількість балів")