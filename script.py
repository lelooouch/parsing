import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0 (.NET CLR 89.0)"}

def array():
    for j in range(1, 4):
        sleep(3)
        url = f"https://quotes.toscrape.com/page/{j}/"

        response = requests.get(url, headers=headers) # получаем ответ от сайта
        soup = BeautifulSoup(response.text, "lxml") # lxml - анализатор html кода
        data = soup.find_all("div", class_="quote")

        for i in data:
            quote = i.find("span", class_="text").text

            by = i.find("small", class_="author").text

            tags = i.find("div", class_="tags").find_all("a", class_="tag")
            tag = ''
            for u in tags:
                tag += u.text + ' '

            about_author = "https://quotes.toscrape.com" + i.find("a").get("href")
            response = requests.get(about_author, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            data = soup.find("div", class_="author-details")
            desc = data.find("div", class_="author-description").text

            yield quote, by, tag, desc



















