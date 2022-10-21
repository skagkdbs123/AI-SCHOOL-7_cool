import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import time
import threading
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
# keyword =input("키워드 : ")
keyword = '비자'
def Naver_news(keyword):
    top_page_url = []
    enctext = urllib.parse.quote(keyword)
    url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query='+enctext
    headers = {'User-Agent': 'Chrome/105.0.0.0 '}
    response = requests.get(url, headers=headers)
    soup = bs(response.text, "html.parser")

    soup = soup.find('div', id='content')
    soup = soup.find('div', id='main_pack')
    soup = soup.find('section', class_='sc_new sp_nnews _prs_nws')

    for href in soup.find("ul", class_="list_news").find_all("li"):
        temp = href.find("a")["href"]
        top_page_url.append(temp)
    while '#' in top_page_url:
        top_page_url.remove('#')
    return top_page_url

naver = Naver_news(keyword)
num=1
st.sidebar.write("hoog")
for i in naver:
#     components.iframe(f"{i}"+"/embed",width=800, height=300, scrolling=False)
    with st.expander(f'{keyword}'+' 검색결과'+f'{num}'):
        github_gist(f"{i}"+"/embed",width=1200, height=900)
    num+=1
print(Naver_news(keyword))
