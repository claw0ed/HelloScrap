#-*- coding: utf-8 -*-

# 파이썬에서 mysql을 사용하려면 Python 표준 DB API를 지원하는
# MySQL DB 모듈을 다운로드 한 후 설치해야 함 - PyMySQL
import pymysql

# mysql connection 생성
conn = pymysql.connect(host='192.168.220.128', port=3306,\
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
    # print(row['lastName'], row['email'], row['jobTitle']) # 인됨!

# cursor, connection 닫기
curs.close()
conn.close()

# 사전식 커서 사용
conn = pymysql.connect(host='192.168.220.128', port=3306,\
                       user='claw0ed', password='Abcdef_12',\
                       db='claw0ed', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from customers where state=%s and city=%s'
curs.execute(sql, ('NY', 'NYC'))

rows = curs.fetchall()

for row in rows:
    print(row['phone'], row['city'], row['state'])

# cursor, connection 닫기
curs.close()
conn.close()

# 간단한 CRUD 테스트
# delete from index_test
# insert into index_test values ('zzyzzy', '987654')
# select * from index_test
# update index_test set uid = 'zzyzigy' where uid = 'zzyzzy'
# select * from index_test

# delete from index_test
conn = pymysql.connect(host='192.168.220.128', port=3306,\
                       user='claw0ed', password='Abcdef_12',\
                       db='claw0ed', charset='utf8')

curs = conn.cursor()
sql = 'delete from index_test'
curs.execute(sql)
curs.close()
conn.commit() # insert, update, delete 시 필요!

# insert into index_test values ('zzyzzy', '987654')
curs = conn.cursor()

# sql = "insert into index_test values ('zzyzzy', '987654')"
sql = 'insert into index_test values (%s, %s)'

curs.execute(sql, ('zzyzzy', '987654'))
curs.close()
conn.commit()

conn.close()

# update index_test set uid = 'zzyzigy' where uid = 'zzyzzy'
conn = pymysql.connect(host='192.168.220.128', port=3306,\
                       user='claw0ed', password='Abcdef_12',\
                       db='claw0ed', charset='utf8')

curs = conn.cursor()

sql = 'update index_test set uid =%s where uid =%s'

curs.execute(sql, ('zzyzigy', 'zzyzzy'))
curs.close()
conn.commit()

conn.close()

# select * from index_test
conn = pymysql.connect(host='192.168.220.128', port=3306,\
                       user='claw0ed', password='Abcdef_12',\
                       db='claw0ed', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from index_test'

curs.execute(sql)
rows = curs.fetchall()

for row in rows:
    print(row['uid'], row['pwd'])

curs.close()

conn.close()
