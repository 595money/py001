from pm.dao.framework.DAOProduct import DAOProduct
import pyodbc


class FundDAOImpl(DAOProduct):
    __single = None

    def __new__(cls):
        if not FundDAOImpl.__single:
            FundDAOImpl.__single = object.__new__(cls)
        return FundDAOImpl.__single

    def insert(self, conn):
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO [TROLL].[FUNDS]
                       ([DEPOSIT_DATE]
                       ,[EXCHANGE_RATE]
                       ,[TOTAL_PAY_NTD]
                       ,[TOTAL_PAY_USD])
                 VALUES
                       (?
                       ,?
                       ,?
                       ,?)
            ''', 'test', '0', '0', '0')
        conn.commit()

    def select(self, conn):
        cursor = conn.cursor()
        cursor.execute('''\
        SELECT * 
          FROM TROLL.FUNDS
        ''')
        for row in cursor:
            print(row)
        pass

    def update(self, conn):
        pass

    def delete(self, conn):
        pass

    def test(self):
        print('FundDAOImplFundDAOImpl')


f = FundDAOImpl()
f.connect()
