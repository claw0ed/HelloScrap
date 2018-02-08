#-*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

# 포탈사이트에 로그인한 후 자신이 받은 메일 수 확인
URL = 'http://www.naver.com'

# 웹 브라우저 자동화를 위해 드라이버 초기화
driver = webdriver.Firefox(
    executable_path = r'C:\Program Files\Mozilla Firefox\geckodriver.exe'
)

# 브라우저를 지정한 URL 로 이동 시킴
driver.get(URL)

# 로그인창에 아이디/비번 입력 후 로그인 버튼 클릭
# html 요소 중 id 가 id 인 요소를 찾음
userid = driver.find_element_by_id('id')
# @id=id 인 요소에 아이디를 입력
userid.send_keys('claw0ed')

# html 요소 중 id 가 pw 인 요소를 찾음
passwd = driver.find_element_by_id('pw')
# @id=pw 인 요소에 비밀번호를 입력
passwd.send_keys('password')

# 로그인 버튼을 찾아서 클릭
loginbtn = driver.find_element_by_xpath('//input[@title="로그인"]')

loginbtn.submit()

# 처리속도가 빨라서 로그인 완료 페이지가 뜨기전에
# 메일 확인 페이지로 이동하려고 함 - 메일페이지가 제대로 안뜸
# 따라서, 로그인 완료페이지가 뜨는걸 확인하기 위해
# (서버로부터 넘어오는 응답데이터를 다 받을때까지)
# 일정 시간동안 브라우저를 잠시 대기시킴
# driver.implicitly_wait(3)

time.sleep(3) # 파이썬 처리를 지연

# 메일 페이지로 이동
MailURL = 'http://mail.naver.com/?n=1518058905359&v=f'
driver.get(MailURL)

source_code = driver.page_source
soup = BeautifulSoup(source_code, 'html.parser')

# 안 읽은 메일 (span[class=cnt])
findkey = 'span["class=cnt"]'
for title in soup.select(findkey):
    print(title.text)

# 로그아웃 버튼 클릭 - 로그아웃 처리
# time.sleep(3)
# mouse = webdriver.ActionChains(driver)
# logoutbtn = driver.find_element_by_xpath("//span[@id='gnb_name1']")
# mouse.move_to_element(logoutbtn).click().perform()
#
# time.sleep(3)
# logoutbtn = driver.find_element_by_id("gnb_logout_button")
# mouse.move_to_element(logoutbtn).click().perform()
time.sleep(3)

clickbtn = driver.find_element_by_xpath('//*[@id="gnb_name1"]')
mouse = webdriver.ActionChains(driver)
mouse.move_to_element(clickbtn).click().perform()

time.sleep(3)

logoutbtn = driver.find_element_by_xpath('//*[@id="gnb_logout_button"]')
mouse = webdriver.ActionChains(driver)
mouse.move_to_element(logoutbtn).click().perform()

time.sleep(3)

driver.get('https://www.naver.com')

# time.sleep(3)
# driver.get('https://nid.naver.com/nidlogin.logout?returl=http://www.naver.com') # 요것만 써도 자동 로그인

# # 테스트를 위해 띄운 브라우져 닫기
# driver.close()
