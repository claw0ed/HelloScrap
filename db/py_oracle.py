#-*- coding: utf-8 -*-
import cx_Oracle
import os # cx_Oracle 에서 한글처리를 위해 추가

# 파이썬에서 oracle 를 사용하려면 먼저,
# Oracle Instant Client 와 부속 파일을 설치해야 함
# 1. oracle.com 에서 Oracle Instant Client 윈도우 X64 다운로드
#    instant client basic, instant client sqlplus
#    C:\Java 아래에 압축해제
# 2. Visual Studio 2013 Redistributable(재배포패키지) x64 다운로드
# 3. 환경변수 설정
#    ORACLE_HOME, TNS_ADMIN, LD_LIBRARY, PATH
# 4. cx_Oracle 모듈 설치

# os.environ['NLS_LANG'] = '.AL32UTF8' # 오라클 환경변수로 인코딩 설정
os.putenv('NLS_LANG', '.AL32UTF8') # 오라클 환경변수로 인코딩 설정

# Oracle connection 생성 (아이디/비번@디비아이피:포트/오라클SID)
conn = cx_Oracle.connect('hr/hr@192.168.220.128:1521/xe')
print(conn.version)

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
