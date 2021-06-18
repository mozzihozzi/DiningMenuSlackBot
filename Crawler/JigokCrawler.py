from . import Crawler
import re, requests
from bs4 import BeautifulSoup


class JigokCrawler(Crawler.Crawler):
    def __init__(self):
        self.menu = {}

    def crawling(self, request):
        bs = BeautifulSoup(request.content, "lxml")
        divs = bs.select("div.column > div.content")

        # 각각의 메뉴를 추출한 div 내용 저장
        breakfast = divs[0]
        sandwich = divs[1]
        lunch = divs[2]
        dinner = divs[3]

        # div 내용에서 한글만 추출
        return {
            'breakfast': re.compile('[가-힣]+').findall(str(breakfast)),
            'sandwitch': re.compile('[가-힣]+').findall(str(sandwich)),
            'lunch': re.compile('[가-힣]+').findall(str(lunch)),
            'dinner': re.compile('[가-힣]+').findall(str(dinner))
        }

    def findDay(self):
        pass

    def findMenu(self):
        pass

    def parsingSentence(self, sentence):
        pass
