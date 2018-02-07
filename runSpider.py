#-*- coding: utf-8 -*-

from scrapy import cmdline

# scrapy 를 윈도우 상에서 구동하려면
# pycharm 환경에서 cmdline.execute() 메서드를 이용하면 된다

# 먼저, pycharm 환경에서 scrapy 가 설치되어 있어야 함@!
# 단, 우가 설치해야 하는 패키지는 pypiwin32 다!

cmdline.execute("scrapy runspider movieSpider.py".split())
