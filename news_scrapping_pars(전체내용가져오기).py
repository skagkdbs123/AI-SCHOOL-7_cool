from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import re
import parser
import pandas as pd
#환율
# keyword =print(input())
top_page_url = []
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
soup = parser.pars(url)
pag = '&sid1=101&date=20221019'

category = soup.select('tr>td>div>ul>li') #경제뉴스의 전체카테고리 링크를 불러오기 위한 전처리
for temp1 in category: #soup를 i에 하나씩 담으면서 그것을 대상을 반복
    temp1 = temp1.find('a')['href']  #i에 담긴 데이터 중에 a와 href를 출력
    top_page_url.append("https://news.naver.com"+temp1+pag)

print(top_page_url)
#페이지의 갯수가 담긴걸 가지고 그 페이지의 수 만큼 반복문을 돌리게 만들어서 page_link에 모든 링크를 저장

temp4=[]
total_url=[]
for i in range(0,len(top_page_url)):
    page_change = top_page_url[i]
    pagee1 = 1
    print(i)
    while True:
        req = Request(
            url=page_change,
            headers={'User-Agent': 'Chrome/105.0.0.0 '}
        )
        html = urlopen(req).read()
        soup2 = bs(html, 'html.parser')
        temp2 = soup2.find('div', class_='paging')
        temp3 = temp2.get_text().find("다음")
        # print(temp5)
        temp2 = (page_change + '&page=' + str(pagee1))
        total_url.append(temp2)
        if pagee1 == 50:
            break
        else:
            pagee1 += 1

#모든 페이지를 다 읽어서 그 링크의 기사들을 싹 긁어온다.

article=[]

for url in total_url:

    html = urlopen(url).read()
    soup = bs(html, 'html.parser')
    soup = soup.find('div', class_='content')
    try:
        temp = ['type06_headline', 'type06']# 해당페이지 상위 10개뉴스,하위 10개뉴스를 번갈아가며 저장
        temp2 = []
        for tmp in temp:
            soup2 = soup.find('ul', class_=tmp)  # 해당페이지 상위 10개뉴스
            soup2 = soup2.select('dt>a')  # select로 dt의 하위태그인 a까지 담도록하여 리스트로 저장한다.
            for link in soup2:
                re.search('naver', link['href'])
                temp2.append(link['href'])
    except AttributeError:
        pass
    try:
        for b in temp2:
            req = Request(
                url=b,
                headers={'User-Agent': 'Chrome/105.0.0.0 '}
            )
            html = urlopen(req).read()
            soup = bs(html, 'html.parser')
            soup = soup.find('div', id='newsct_article').get_text()
            b.append(soup)
            article.append(soup)
        print(len(article))
    except AttributeError:  #알수없는 이유로 NoneType이 발견되었기 때문에 그 부분을 pass하기 위함
        pass

Series = pd.Series(article)
# ps1 = Series.duplicated(keep='first')
ps2=Series.to_csv("news1.csv", encoding='cp949')

# with open('list_to_csv.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(article)
# count = 0
# key = "달러"
# for u in range(len(article)):
#     temp3 = str(article[u]).count(key)
#     count+=temp3
#
# print(f"{key}의 개수 : " +f"{count}")



# print(article)
# article.to_csv("all_news.csv",index=False, encoding="cp949")
    # article_count=[]
    # cnt = article.count('환율')
    #
    # article_count.append(cnt)
    # print(article_count)
# for b in temp2:
#     req = Request(
#         url=b,
#         headers={'User-Agent': 'Chrome/105.0.0.0 '}
#     )
#     html = urlopen(req).read()
#     soup = bs(html, 'html.parser')
#     soup = soup.find('div', id='newsct_article').get_text()
#     article.append(soup)
# print(len(article))

# for b in range(len(temp2)):
#     req = Request(
#         url=b,
#         headers={'User-Agent': 'Chrome/105.0.0.0 '}
#     )
#     html = urlopen(req).read()
#     soup = bs(html, 'html.parser')
#     soup = soup.find('div', id='newsct_article').get_text()


# # urllib.request.urlretrieve(url,savename)
# print(soup)


#
# 참고자료:https://charimlab.tistory.com/12
#         https://crazyj.tistory.com/201
#         https://ponyozzang.tistory.com/335
#         https://www.fun-coding.org/crawl_basic4.html

