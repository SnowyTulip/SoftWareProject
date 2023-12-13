from abc import ABCMeta, abstractmethod
from Configs import IConfig

class ISpider:
    @abstractmethod
    def read_url(self):
        pass

    @abstractmethod
    def add_config(self,IConfig):
        pass