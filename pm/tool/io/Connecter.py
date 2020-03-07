from abc import ABCMeta, abstractmethod


class Connecter(metaclass=ABCMeta):

    @abstractmethod
    def connect(self, path):
        pass

    @abstractmethod
    def is_exist(self, path):
        pass


if __name__ == '__main__':
    c = Connecter()
