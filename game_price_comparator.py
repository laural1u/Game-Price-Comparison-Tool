import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
url = 'https://www.nintendo.com/store/games/'

headers = { }
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html)

titles = soup.find_all(class_= "BasicTilestyles__Title-sc-sh8sf3-11 ka-dMDt")
prices = soup.find_all(class_= "Pricestyles__PriceWrapper-sc-afjfk5-8 eieoUb")
title_list=[]
price_list=[]

for title in titles:
    title_list.append(title.get_text())

for price in prices:
    price_list.append(price.get_text())

for i in range(len(title_list)):
    print(i,",",title_list[i])

for i in range(len(price_list)):
    print(i,",",price_list[i])

url_2 = 'https://www.nintendo.com/en-ca/store/games/'
headers_2 = { }
response_2 = requests.get(url_2, headers=headers_2)
html_2 = response_2.text
soup_2 = BeautifulSoup(html_2)

titles_2= soup_2.find_all(class_= "BasicTilestyles__Title-sc-sh8sf3-11 ka-dMDt")
prices_2 = soup_2.find_all(class_= "Pricestyles__PriceWrapper-sc-afjfk5-8 eieoUb")
title_list_2=[]
price_list_2=[]

for title in titles_2:
    title_list_2.append(title.get_text())

for price in prices_2:
    price_list_2.append(price.get_text())

for i in range(len(title_list_2)):
    print(i,",",title_list_2[i])

for i in range(len(price_list_2)):
    print(i,",",price_list_2[i])
