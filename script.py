import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0 (.NET CLR 89.0)"}

for j in range(5):

    sleep(3)
    if j == 0:
        url = "https://quotes.toscrape.com/"
    else:
        url = f"https://quotes.toscrape.com/page/{j}/"

    response = requests.get(url, headers=headers) # получаем ответ от сайта
    # print(response.text) - сырой текст html страницы
    soup = BeautifulSoup(response.text, "lxml") # lxml - анализатор html кода
    data = soup.find_all("div", class_="quote")

    for i in data:
        quote_1 = i.find("span", class_="text").text
        author_1 = i.find("small", class_="author").text.replace('\n', '')
        url_author = "https://quotes.toscrape.com" + i.find("a").get("href")
        print(quote_1 + "\n" + author_1 + "\n" + url_author + "\n")


