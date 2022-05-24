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
    pure_title = title.get_text().replace(u'\xae', '')
    pure_title = pure_title.replace(u'\u2122', '')
    title_list.append(pure_title)

for price in prices:
    price_list.append(price.get_text())

for i in range(len(title_list)):
    print(i,",",title_list[i])

for i in range(len(price_list)):
    print(i,",",price_list[i])

cur_print_price=[]
for i in range(len(price_list)):
    dollar_index = price_list[i].find("Current Price:")
    cur_print_price.append(price_list[i][dollar_index+14:dollar_index+20])
    if ":" in cur_print_price[i]:
        cur_print_price[i] = "-"

reg_print_price=[]
for i in range(len(price_list)):
    dollar_index = price_list[i].find("Regular Price:")
    reg_print_price.append(price_list[i][dollar_index+14:dollar_index+20])

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
    pure_title = title.get_text().replace(u'\xae', '')
    pure_title = pure_title.replace(u'\u2122', '')
    title_list_2.append(pure_title)

for price in prices_2:
    price_list_2.append(price.get_text())

for i in range(len(title_list_2)):
    print(i,",",title_list_2[i])

for i in range(len(price_list_2)):
    print(i,",",price_list_2[i])

cur_print_price_2=[]
for i in range(len(price_list_2)):
    dollar_index = price_list_2[i].find("Current Price:")
    cur_print_price_2.append(price_list_2[i][dollar_index+14:dollar_index+20])
    if ":" in cur_print_price_2[i]:
        cur_print_price_2[i] = "-"

reg_print_price_2=[]
for i in range(len(price_list_2)):
    dollar_index = price_list_2[i].find("Regular Price:")
    reg_print_price_2.append(price_list_2[i][dollar_index+14:dollar_index+20])

dataframe = pd.DataFrame({'America-Game Name':title_list, 'Regular Price-A':reg_print_price, 'Current Price-A':cur_print_price,'Canada-Game Name':title_list_2, 'Regular Price-C':reg_print_price_2, 'Current Price-C':cur_print_price_2})

dataframe.to_csv("result.csv", index = False, sep = ',')
