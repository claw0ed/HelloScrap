#-*- coding: utf-8 -*-

# 파이썬에서 mysql을 사용하려면 Python 표준 DB API를 지원하는
# MySQL DB 모듈을 다운로드 한 후 설치해야 함 - PyMySQL
import pymysql

# mysql connection 생성
conn = pymysql.connect(host='192.168.220.128',\
                       user='claw0ed', password='Abcdef_12',\
                       db='claw0ed', charset='utf8')

# connection 에서 cursor 생성
curs = conn.cursor()

# sql 문 작성 후 실행
sql = 'select * from employees'
rows = curs.execute(sql)

# 필요하다면, 실행한 sql 로 부터 데이터 처리
rows = curs.fetchall()
for row in rows:
    print(row[0], row[1], row[2])

# connection 닫기
conn.close()