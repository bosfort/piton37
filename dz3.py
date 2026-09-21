class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print(f"Товари в магазині {self.name}:")
        for product in self.products:
            print("-", product)


class Human:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def buy(self, shop, product):
        if product in shop.products:
            print(f"{self.name} купив {product} у магазині {shop.name}")
        else:
            print(f"У магазині немає товару {product}")


shop = Shop("АТБ")

shop.add_product("Хліб")
shop.add_product("Молоко")
shop.add_product("Сік")

person = Human("Олег", 500)

shop.show_products()

person.buy(shop, "Молоко")
person.buy(shop, "Шоколад")