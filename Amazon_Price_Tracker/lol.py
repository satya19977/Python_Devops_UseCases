import lxml as lxml
import requests
from bs4 import BeautifulSoup
import pandas as pd
count = 1
is_true = False
titles = []
review_content = []
headers = {
            "Accept-Language":"en-US,en;q=0.9",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        }
while is_true == False:
    if count ==10:
        is_true = True
        amazon_url = f"https://www.amazon.com/Hunger-Games-Trilogy-Catching-Mockingjay/product-reviews/0545670314/ref=cm_cr_dp_d_show_all_btm{count}?ie=UTF8&reviewerType=all_reviews"

        response = requests.get(url=amazon_url,headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        #soup = BeautifulSoup(response.text, "html.parser")


        reviews_title = soup.find_all('div',{'data-hook':'review'})
        for i in reviews_title:
            title = i.find('a',{'data-hook':'review-title'}).text.strip()
            titles.append(title)
            body = i.find('span',{'data-hook':'review-body'}).text.strip()
            review_content.append(body)
    else:
        amazon_url = f"https://www.amazon.com/Hunger-Games-Trilogy-Catching-Mockingjay/product-reviews/0545670314/ref=cm_cr_dp_d_show_all_btm{count}?ie=UTF8&reviewerType=all_reviews"
        response = requests.get(url=amazon_url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        # soup = BeautifulSoup(response.text, "html.parser")

        reviews_title = soup.find_all('div', {'data-hook': 'review'})
        for i in reviews_title:
            title = i.find('a', {'data-hook': 'review-title'}).text.strip()
            titles.append(title)
            body = i.find('span', {'data-hook': 'review-body'}).text.strip()
            review_content.append(body)

df1 = pd.DataFrame(titles)
df1.rename(columns={0:'title'},inplace=True)
df1['review_content'] = pd.DataFrame(review_content)
print(df1)
