import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

print("Назви книг:")
for book in books:
    title = book.find("h3").find("a")["title"]
    print(title)

print("Ціни книг:")
for book in books:
    price = book.find("p", class_="price_color").text
    print(price)

print("інформація:")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find(
        "p", class_="instock availability"
    ).text.strip()

    print("Назва:", title)
    print("Ціна:", price)
    print("Наявність:", availability)
