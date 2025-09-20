import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url) # получаем ответ от сайта
# print(response.text) - сырой текст html страницы
soup = BeautifulSoup(response.text, "lxml") # lxml - анализатор html кода
data = soup.find("div", class_="quote")
quote_1 = data.find("span", class_="text").text.replace('\n', '')
author_1 = data.find("small", class_="author").text.replace('\n', '')
print(quote_1, author_1)
