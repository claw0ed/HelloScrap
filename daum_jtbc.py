import requests
from bs4 import BeautifulSoup

# 다음 JTBC 뉴스 스크래핑 예제
# http://media.daum.net/cp/310?page=2&regDate=20180205&cateId=1002

press = [310] # 언론사
date = [20180205] # 년월일
page = [1, 2, 3] # 페이지

news_title = [] # 뉴스제목
news_desc = [] # 뉴스 간략소개

URL = 'http://media.daum.net/cp/' + str(press[0]) + '?page=' + str(page[0]) + '&regDate=' + str(date[0])

# 스크래핑해서 소스를 에 저장
source_code = requests.get( URL )

# 중간 결과 출력
# print(source_code.text)

plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')
# soup = BeautifulSoup(plain_text, 'html.parser')

# 기사 제목 추출
cnt = 1
for title in soup.select("a['class=link_txt']"):
    if (cnt > 15): break
    # print(title.text.strip())
    news_title.append(title.text.strip())
    cnt += 1

# 기사 간단소개 추출
cnt = 1
for title in soup.select("span['class=link_txt']"):
    if (cnt > 15): break
    # print(title.text.strip())
    news_desc.append(title.text.strip())
    cnt += 1

cnt = 0
for title in soup.select("a['class=link_txt']"):
    if (cnt > 14): break
    print(news_title[cnt])
    print(news_desc[cnt])
    cnt += 1

for i in range(0, 15):
    print(news_title[i])
    print("%s\n" % news_desc[i])

