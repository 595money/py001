from abc import ABCMeta, abstractmethod
from pm.tool.io.Connecter import Connecter


class Writer(Connecter, metaclass=ABCMeta):
    pass


    @abstractmethod
    def write(self, path, data):
        pass
