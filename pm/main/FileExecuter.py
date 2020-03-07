from abc import ABCMeta, abstractmethod


class FileExecuter(metaclass=ABCMeta):
    pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def interaction(self, status):
        pass
