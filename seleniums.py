#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# selenium 설치
# firefox 용 webdriver 다운로드

movie_rank = []   # 순위
movie_title = []  # 제목

# URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'
URL = 'http://movie.daum.net/main/new#slide-1-0'

# firefox 를 띄어 브라우저에 나타난 소스를 스크래핑함
driver = webdriver.Firefox(
    executable_path = r'C:\Program Files\Mozilla Firefox\geckodriver.exe'
)
# 웹브라우저를 자동화할 수 있도록 특수하게 컴파일된 브라우저인
# geckodriver.exe 를 다운로드 후 지정한 위치에 저장
# https://github.com/mozilla/geckodriver/releases
driver.get(URL)

# 스크래핑해서 소스를 에 저장
source_code = driver.page_source # firefox 로 가져온 소스를 source_code 변수에 저장

# print(source_code)

# plain_text = source_code.text

# soup = BeautifulSoup(plain_text, 'html.parser') # html 파서(분석기)
soup = BeautifulSoup(source_code, 'lxml')         #  xml 파서(분석기)

# print(soup)

# 순위 추출
for i in range (1, 21):
    findkey = 'em["class=num_rank rank_'+ str(i).zfill(2) +'"]'
    for title in soup.select(findkey):
        print(" ".join(title.text.strip().split()))
        # movie_rank.append(" ".join(title.text.strip().split()))

    # 제목 추출
    findkey = 'a["class=link_txt #top #ranking #title @' + str(i) +'"]'
    for title in soup.select(findkey):
        print(title.text.strip())
        # movie_title.append(title.text.strip())
