
import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE Animals (name TEXT, type TEXT);")

cur.execute("INSERT INTO Animals (name, type) VALUES ('Лев', 'Ссавець');")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Крокодил', 'Плазун');")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Орел', 'Птах');")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Морська черепаха', 'Плазун');")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Мавпа', 'Ссавець');")

connection.commit()

cur.execute("UPDATE Animals SET name='Сокіл' WHERE name='Орел';")
connection.commit()

cur.execute("SELECT rowid, name, type FROM Animals WHERE type='Ссавець';")
res = cur.fetchall()
print(res)

cur.execute("SELECT rowid, name, type FROM Animals;")
res = cur.fetchall()
print(res)

connection.close()


connection = sqlite3.connect("FruitBasket.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE Fruits (name TEXT, color TEXT);")

cur.execute("INSERT INTO Fruits (name, color) VALUES ('Яблуко', 'Червоне');")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Банан', 'Жовтий');")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Апельсин', 'Помаранчевий');")

connection.commit()

cur.execute("UPDATE Fruits SET color='Зелене' WHERE name='Яблуко';")
connection.commit()

cur.execute("SELECT rowid, name, color FROM Fruits WHERE color='Жовтий';")
res = cur.fetchall()
print(res)

cur.execute("SELECT rowid, name, color FROM Fruits;")
res = cur.fetchall()
print(res)

connection.close()
