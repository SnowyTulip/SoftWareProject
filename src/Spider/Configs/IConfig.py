from abc import abstractmethod


class IConfig:
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_headers(self):
        pass

    @abstractmethod
    def get_base_url(self):
        pass

    @abstractmethod
    def get_pagination_str(self):
        pass