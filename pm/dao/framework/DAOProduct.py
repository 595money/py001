from abc import ABCMeta, abstractmethod
import pyodbc

class DAOProduct(metaclass=ABCMeta):
    pass
    @staticmethod
    def connect():
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-88J84HR;'
                              'Database=pm;'
                              'Trusted_Connection=yes;')
        return conn

    @abstractmethod
    def insert(self, conn):
        pass

    @abstractmethod
    def select(self, conn):
        pass

    @abstractmethod
    def update(self, conn):
        pass

    @abstractmethod
    def delete(self, conn):
        pass
