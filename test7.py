import streamlit as st
import streamlit.components.v1 as components
i = ['https://www.yna.co.kr/view/AKR20221021118000004?input=1195m', 'https://www.seoul.co.kr/news/newsView.php?id=20221021500083&wlog_tag3=naver', 'https://www.yna.co.kr/view/AKR20221021119900064?input=1195m', 'http://www.newsis.com/view/?id=NISX20221020_0002055098&cID=10806&pID=10800', 'http://www.segye.com/content/html/2022/10/20/20221020520458.html?OutUrl=naver', 'https://www.donga.com/news/article/all/20221020/116056433/1', 'https://biz.chosun.com/topics/topics_social/2022/10/20/BASCOOQGSNCSNE35ABIRDCYMBQ/?utm_source=naver&utm_medium=original&utm_campaign=biz', 'https://imnews.imbc.com/news/2022/society/article/6418847_35673.html', 'http://mbn.mk.co.kr/pages/news/newsView.php?category=mbn00009&news_seq_no=4867206', 'https://news.imaeil.com/page/view/2022102110571162043']
option = st.selectbox(
    'How would you like to be contacted?',i)
