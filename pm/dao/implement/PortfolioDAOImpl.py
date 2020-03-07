from pm.dao.framework.DAOProduct import DAOProduct
import pyodbc


class PortfolioDAOImpl(DAOProduct):
    __single = None

    def __new__(cls):
        if not PortfolioDAOImpl.__single:
            PortfolioDAOImpl.__single = object.__new__(cls)
        return PortfolioDAOImpl.__single

    def insert(self, conn):
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO [TROLL].[PORTFOLIO]
                       ([TICKER_SYMBOL]
                       ,[OPEN_DATE]
                       ,[CLOSE_DATE]
                       ,[TOTAL_PAY_USD]
                       ,[OPEN]
                       ,[CLOSE]
                       ,[UNITS])
                 VALUES
                       (?
                       ,?
                       ,?
                       ,?
                       ,?
                       ,?
                       ,?)
            ''')
        conn.commit()

    def select(self, conn):
        cursor = conn.cursor()
        cursor.execute('''\
        SELECT * 
          FROM TROLL.PORTFOLIO
        ''')
        for row in cursor:
            print(row)
        pass

    def update(self, conn):
        pass

    def delete(self, conn):
        pass

    def test(self):
        print('PortfolioDAOImplPortfolioDAOImplPortfolioDAOImpl')
