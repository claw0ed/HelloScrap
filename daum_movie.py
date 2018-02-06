#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 다음 영화 순위 스크래핑 예제
# http://ticket2.movie.daum.net/Movie/MovieRankList.aspx

# page = [0, 1, 2, 3, 4] # 페이지

movie_rank = []   # 순위
movie_title = []  # 제목
movie_grade = []  # 평점
movie_opdate = [] # 개봉일

URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'

# 스크래핑해서 소스를 에 저장
source_code = requests.get(URL)

# 중간 결과 출력
# print(source_code.text)

plain_text = source_code.text
# soup = BeautifulSoup(plain_text, 'lxml')
soup = BeautifulSoup(plain_text, 'html.parser')

# print(soup)

# 순위 추출
for i in range (1, 21):
    findkey = 'span["class=ico_ranking ico_top'+ str(i) +'"]'
    for title in soup.select(findkey):
        # print(" ".join(title.text.strip().split()))
        movie_rank.append(" ".join(title.text.strip().split()))

# 제목 추출
findkey = "a['class=link_g']"
for title in soup.select(findkey):
    # print(title.text.strip())
    movie_title.append(title.text.strip())

# 평점 추출
findkey = "em['class=emph_grade']"
for title in soup.select(findkey):
    # print(title.text.strip() + "/10")
    movie_grade.append(title.text.strip() + "/10")

# 개봉일 추출
findkey = "dl['class=list_state']"
for title in soup.select(findkey):
    # print(title.select('dd')[0].text)
    movie_opdate.append(title.select('dd')[0].text)

# 모든 내용 출력
for i in range(0, 20):
    print(movie_rank[i])
    print(movie_title[i])
    print(movie_grade[i])
    print("%s\n" % (movie_opdate[i]))
