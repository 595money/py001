from pm.dao.framework.DAOProduct import DAOProduct
import pyodbc


class EtoroDAOImpl(DAOProduct):
    __single = None

    def __new__(cls):
        if not EtoroDAOImpl.__single:
            EtoroDAOImpl.__single = object.__new__(cls)
        return EtoroDAOImpl.__single

    def insert(self, conn):
        pass

    def select(self, conn):
        pass

    def update(self, conn):
        pass

    def delete(self, conn):
        pass

    def test(self):
        print('yyyy')
