import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import re
import time
import threading
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.pexels.com/photos/342945/pexels-photo-342945.jpeg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# set_bg_hack_url()

keyword = st.text_input('검색할 키워드를 입력하세요')

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

def Naver_title(keyword):
    
    real_title=[]
    enctext = urllib.parse.quote(keyword)
    url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query='+enctext
    headers = {'User-Agent': 'Chrome/105.0.0.0 '}
    response = requests.get(url, headers=headers)
    soup = bs(response.text, "html.parser")
    items = soup.select('.news_tit')
    for item in items:
        real_title.append(item.text)
        
    return real_title
# def show_page(i):
#     components.iframe(f"{i}",width=800, height=1200, scrolling=True)
# number_list=[1,2,3,4,5,6,7,8,9,10]

# dic = { name:value for name, value in zip(number_list,i)}

naver_link = Naver_news(keyword)
naver_main = Naver_title(keyword)
num=1
for i in naver:
    with st.expander(f'{keyword}'+' 검색결과'+f'{num}'):
        components.iframe(f"{i}",width=800, height=1200, scrolling=True)
    num+=1
