from abc import ABCMeta, abstractmethod

class ISpider:
    @abstractmethod
    def read_url(self):
        pass

    @abstractmethod
    def add_config(self,IConfig):
        pass