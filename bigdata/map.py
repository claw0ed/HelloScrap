# -*- coding: utf-8 -*-

import sys
import codecs

# 파이썬으로 작성해보는 맵리듀스 구현 예제
# 워드 카운트 - 파일에 작성된 단어 빈도를 계산후 출력

sys.stdin = codecs.open('words.txt', 'r', 'utf-8')
# words.txt 의 내용을 표준 입력으로 받음

for line in sys.stdin: # 표준입력으로부터 한줄씩 꺼낸후
    cline =line.strip() # 앞뒤 공백 제거
    words = cline.split() # 빈칸을 기준으로 각 단어를 분리한 후 리스트에 저장

    for word in words: # 리스트에 저장된 단어들로부터 하나씩 꺼내
        print('%s\t%s' % (word, 1)) # 단어와 출현빈도를 같이 출력
        pass