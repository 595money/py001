from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    pass

    @abstractmethod
    def create_product(self, product_name):
        pass
