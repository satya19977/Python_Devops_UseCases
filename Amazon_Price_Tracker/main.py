import smtplib

import lxml as lxml
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
TARGET_PRICE = 165
amazon_url = "https://www.amazon.com/North-Face-Junction-Insulated-Heather/dp/B097NJ6Y2T/ref=sr_1_18?keywords=north%2Bface%2Bjacket%2Bmen&qid=1666822811&qu=eyJxc2MiOiI4LjUxIiwicXNhIjoiOC4wNiIsInFzcCI6IjcuNDQifQ%3D%3D&sprefix=north%2Caps%2C124&sr=8-18&th=1"
headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
}
response = requests.get(url=amazon_url,headers=headers)
soup = BeautifulSoup(response.text, "lxml")
y = soup.find(class_="a-offscreen").get_text()
print(y)
stripped_y = y.strip("$")

if float(stripped_y) < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="rangarrr10@gmail.com", password="sstxuzdhokpehkgh")
        connection.sendmail(from_addr="rangarrr10@gmail.com", to_addrs="satyakrishna977@gmail.com", msg="Subject:Amazon Hoodie Price Down")