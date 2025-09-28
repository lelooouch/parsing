from requests import Session # сохраняем файды куки
from bs4 import BeautifulSoup
from time import sleep

work = Session()
work.get("https://quotes.toscrape.com/")
response = work.get("https://quotes.toscrape.com/login")
soup = BeautifulSoup(response.text, "lxml")

token = soup.find("form").find("input").get("value")



