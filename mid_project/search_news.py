import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import re
import streamlit as st
import streamlit.components.v1 as components

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.pexels.com/photos/321464/pexels-photo-321464.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

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

keyword = st.text_input('검색할 키워드를 입력하세요')

try:
    
    if type(keyword) == str:
        with st.spinner('Wait for it...'):
            naver_link = Naver_news(keyword)
            naver_main = Naver_title(keyword)
            num=1
            i = naver_link
            k = naver_main #여기엔 숫자대신 제목이 들어갈 예정
            link_dict = { name:value for name, value in zip(k,i)}

            selected = st.selectbox('check one',options = [t for t in k])

            selected_link = link_dict[selected]
            components.iframe(selected_link, width=700, height=1200, scrolling=True)
        st.success('Done!')
except AttributeError:
    pass
