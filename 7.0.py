import random
import string

def random_letters():
    while True:
        yield random.choice(string.ascii_letters)

generator = random_letters()

for i in range(10):
    print(next(generator))