from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import re
import parser
import urllib.request
import pandas as pd
#환율
keyword =print(input())
top_page_url = []
encText = urllib.parse.quote(keyword)
url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query='+encText
soup = parser.pars(url)
soup = soup.find('div',id='content')
soup = soup.find('div',id='main_pack')
soup = soup.find('section',class_='sc_new sp_nnews _prs_nws')
# category = soup.select('div>div>ul>li>div>div>a')
for href in soup.find("ul",class_="list_news").find_all("li"):
    temp = href.find("a")["href"]
    top_page_url.append(temp)
while '#' in top_page_url:
    top_page_url.remove('#')
print(top_page_url)
# soup = soup.find()
# print((str(category[0]).split('"')))
# for i in range(0,len(category)):
#     temp1 = (str(category[i]).split('"'))
#     matching = [s for s in temp1 if "news" in s]
#     top_page_url.append(matching)

# print(category)

# print(matching)