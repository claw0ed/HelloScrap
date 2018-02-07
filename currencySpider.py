#-*- coding: utf-8 -*-

import scrapy # 스크랩파이 설치
import codecs
import sys

# 리눅스상에서 파이썬2 를 이용해서 utf-8 로 파일에 내용을 기록하려면 시스템 기본 인코딩을 utf-8 로 설정해야 함
reload(sys)
sys.setdefaultencoding('utf8')

# scrapy 에서 spider 는 크롤링/스크래핑을 담당하는 핵심부분
# 크롤링/스크래핑 절차에 대한 정의를 하는 부분
class CurrencySpider(scrapy.Spider):
    name = 'currencySpider' # 스파이더 프로그램의 이름 정의
    start_urls = ['http://finance.naver.com/marketindex/?tabSel=exchange']
    # 스파이더가 스크래핑할 위치를 URL 로 정의

    def parse(self, response):
        # start_urls 에 정의된 URL 을 스파이더가 스크래핑하고
        # 내용이 다운로드된 후 호출되는 메서드
        # parse() 는 실제 추출할 데이터를 작업한 후
        # 결과를 return 하는 역할 담당

        blinds = response.css('span.blind::text').extract()
        # css 선택자를 이용햐서 클래스가 span.blind 인
        # 모든 항목을 추출해서 blinds 변수에 저장

        values = response.css('span.value::text').extract()
        # css 선택자를 이용해서 클래스가 span.value 인
        # 모든 항목을 추출해서 values 변수에 저장

        with codecs.open('currency.csv', 'w', 'utf-8') as f:
            # 처리결과를 파일에 저장하기 위해
            # movierank.csv 라는 이름으로 쓰기 모드 open
            for i in range(0, 20):
                blind = blinds[i].replace('/r/n', '') # /r/n -> whitespace 눈에 보이지 않는 스페이스
                blind = ''.join(blind.split()) # 빈칸으로 분리후 다시 합침
                print(blind)
                value = values[i].replace('/r/n', '') # -> whitespace 눈에 보이지 않는 스페이스
                value = value.strip().encode('utf-8') # utf-8 로 변환후 출력
                print(value)
                f.write('%s,%s\n' % (blind, value)) # 순위와 제목을 파일에 기록
        f.close()
