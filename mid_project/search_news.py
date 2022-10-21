import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import re
import time
import threading
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
# keyword =input("키워드 : ")
keyword = '달러'
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

    for href in soup.find("ul", class_="list_news").find_all("div",attrs = {"class":re.compile("api_save_group _keep_wrap")}):
        temp = href.find("a")["data-url"]
        top_page_url.append(temp)
        
    return top_page_url

naver = Naver_news(keyword)
num=1
for i in naver:
    with st.expander(f'{keyword}'+' 검색결과'+f'{num}'):
        components.iframe(f"{i}",width=800, height=1200, scrolling=True)
    num+=1
