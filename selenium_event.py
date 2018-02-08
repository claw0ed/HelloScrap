#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 탐색할 URL 정의
URL = 'https://kr.investing.com/currencies/'

# 웹 브라우저 자동화를 위해 드라이버 초기화
driver = webdriver.Firefox(
    executable_path = r'C:\Program Files\Mozilla Firefox\geckodriver.exe'
)
# 웹브라우저를 자동화할 수 있도록 특수하게 컴파일된 브라우저인
# geckodriver.exe 를 다운로드 후 지정한 위치에 저장
# https://github.com/mozilla/geckodriver/releases

# 브라우저를 지정한 URL 로 이동 시킴
driver.get(URL)

# 웹 페이지 오른쪽 '암호화폐' 탭의 xpath 정의
# //*[@id="QBS_7"]
# /html/body/div[5]/aside/div[2]/div[1]/ul/li[4]/a
alink = driver.find_element_by_xpath('//li[@id="QBS_7"]/a')

# 마우스, 단축키 이벤트 처리를 위해 ActionChains 초기화
mouse = webdriver.ActionChains(driver)

# 해당 링크를 마우스클릭으로 처리하기 위해 move_to_element 사용
# 즉, 마우스를 링크로 이동한 다음 클릭
mouse.move_to_element(alink).click().perform()

# 클릭후 보여지는 페이지 내용을 source_code 에 저장
source_code = driver.page_source # firefox 로 가져온 소스를 source_code 변수에 저장
# print(source_code)

# 웹 페이지를 parsing 하기 위해 bs4 로 초기화
# soup = BeautifulSoup(source_code, 'lxml')      #  xml 파서(분석기)
soup = BeautifulSoup(source_code, 'html.parser') # html 파서(분석기)

btccode = ['-btc-usd','-btc-krw','-eth-usd','-bch-krw','-iot-usd','-bch-usd','-etc-krw','-xrp-usd']
btccurcode = [945629,940808,997650,1031396,1031068,1031333,1011047,1010782] # 종목번호

# 암호화폐 종류 (data-btccode="-btc-usd")
for i in range(0, len(btccode)):
    findkey = 'a["data-gae='+str(btccode[i])+'"]'
    for title in soup.select(findkey):
        print(title.text)

    # 암호화폐 환율 (id="sb_last_945629")
    findkey = 'td["id=sb_last_'+str(btccurcode[i])+'"]'
    for title in soup.select(findkey):
        print(title.text.strip())
