from abc import ABCMeta, abstractmethod
from pm.tool.io.Connecter import Connecter


class Reader(Connecter, metaclass=ABCMeta):
    pass

    @abstractmethod
    def read(self, path):
        pass
