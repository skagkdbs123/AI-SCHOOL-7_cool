import os
import sys
import urllib.request
client_id = "eii21SeKqnLtCvAX08FH"                  # 발급받은 ID 값 입력
client_secret = "l3LEH4LvMp"              # 발급받은 KEY 값 입력
encText = urllib.parse.quote("창업")     # 원하는 키워드 입력
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    # news blogs cafearticle 로 변환가능

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)