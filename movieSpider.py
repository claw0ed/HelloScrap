#-*- coding: utf-8 -*-

import scrapy
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class MovieSpider(scrapy.Spider):
    name = 'movieSpider'
    start_urls = ['http://ticket2.movie.daum.net/Movie/MovieRankList.aspx']

    def parse(self, response):
        ranks = response.css('.ico_ranking::text').extract()
        titles = response.css('.link_g::text').extract()

        with codecs.open('movierank.csv', 'w', 'utf-8') as f:
            for i in range(0, 20):
                rank = ranks[i].replace('/r/n', '')
                rank = ''.join(rank.split())
                print(rank)
                title = titles[i].replace('/r/n', '')
                title = title.strip().encode('utf-8')
                print(title)
                f.write('%s,%s\n' % (rank, title))
        f.close()
