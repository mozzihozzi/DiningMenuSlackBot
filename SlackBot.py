from Singleton import Singleton
from Crawler import JigokCrawler
from slacker import Slacker


class SlackBot(metaclass=Singleton):
    def __init__(self):
        self._crawlers = []
        self.__token = "xoxb-1937514063156-2175465725633-UV7FjkEVzAB6R6nSJnq9ToOl"
        self._slackBot = Slacker(self.__token)
    