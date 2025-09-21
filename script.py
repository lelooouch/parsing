import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url) # получаем ответ от сайта
# print(response.text) - сырой текст html страницы
soup = BeautifulSoup(response.text, "lxml") # lxml - анализатор html кода
data = soup.find_all("div", class_="quote")

for i in data:
    quote_1 = i.find("span", class_="text").text
    author_1 = i.find("small", class_="author").text.replace('\n', '')
    url_author = "https://quotes.toscrape.com" + i.find("a").get("href")
    print(quote_1 + "\n" + author_1 + "\n" + url_author + "\n")


