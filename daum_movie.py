#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 다음 JTBC 뉴스 스크래핑 예제
# http://media.daum.net/cp/310?page=2&regDate=20180205&cateId=1002

# page = [0, 1, 2, 3, 4] # 페이지

rank_on = [] # 실시간예매순위
ranking_title = [] # 영화 이름

URL = 'http://movie.daum.net/boxoffice/weekly'

# 스크래핑해서 소스를 에 저장
source_code = requests.get( URL )

# 중간 결과 출력
# print(source_code.text)

plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')
# soup = BeautifulSoup(plain_text, 'html.parser')

