import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url) # получаем ответ от сайта
# print(response.text) - сырой текст html страницы
soup = BeautifulSoup(response.text, "lxml") # lxml - анализатор html кода
data = soup.find("div", class_="quote")
name = data.find("span", class_="text")
print(name.text)
