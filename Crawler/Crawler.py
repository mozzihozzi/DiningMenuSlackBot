from abc import ABCMeta, abstractmethod


class Crawler(metaclass=ABCMeta):
    @abstractmethod
    def crawling(self, request):
        pass

    @abstractmethod
    def findDay(self):
        pass

    @abstractmethod
    def findMenu(self):
        pass

    @abstractmethod
    def parsingSentence(self, sentence):
        pass

    def startCrawling(self, request, sentence):
        self.parsingSentence(sentence)
        return self.crawling(request)



