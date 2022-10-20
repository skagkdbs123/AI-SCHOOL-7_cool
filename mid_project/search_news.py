import urllib.request
import parser
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
keyword =input("키워드 : ")

def Naver_news(keyword):
    top_page_url = []
    enctext = urllib.parse.quote(keyword)
    url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query='+enctext
    soup = parser.pars(url)
    soup = soup.find('div', id='content')
    soup = soup.find('div', id='main_pack')
    soup = soup.find('section', class_='sc_new sp_nnews _prs_nws')
    for href in soup.find("ul", class_="list_news").find_all("li"):
        temp = href.find("a")["href"]
        top_page_url.append(temp)
    while '#' in top_page_url:
        top_page_url.remove('#')
    return top_page_url

print(Naver_news(keyword))
