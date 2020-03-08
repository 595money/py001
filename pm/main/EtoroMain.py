from pm.main.FileExecuter import FileExecuter
from pm.tool.io.ExcelEditor import ExcelEditor
from pm.dao.implement.DAOFactory import DAOFactory
from pm.dao.framework.DAOProduct import DAOProduct
from pm.etoro.bean import Fund
from pm.etoro.bean import Portfolio

class EtoroMain(FileExecuter):
    conn = None
    db_fund = None
    db_portfolio = None
    csv_fund = None
    csv_portfolio = None
    def __init__(self):
        self.file_editor = ExcelEditor()
        self.conn = DAOProduct.connect()
        self.status = 'input'

    def welcome(self):
        print('''\
        請輸入功能選項:
        1) Insert Fund、Portfolio 資料表
        2) Insert Fund 資料表
        3) Insert Portfolio 資料表
        4) Update Portfolio 資料表平倉記錄
        q) 離開程式
        ''')

    def process(self, cmd):
        conn = DAOProduct.connect()
        if cmd.casefold() == 'q':
            return
        if cmd.casefold() in '1':
            self.insert_fund()
            self.insert_portfolio()
        if cmd.casefold() in '2':
            self.insert_fund()
        if cmd.casefold() in '3':
            self.insert_portfolio()
        if cmd.casefold() in '4':
            self.update_portfolio()

    def interaction(self, status):
        msg = status.strip()
        if msg == '1':
            # insert fund table and portfolio table
            pass
        if msg == '2':
            # insert fund table
            pass
        if msg == '3':
            # insert portfolio table
            pass
        if msg == '4':
            # update portfolio table
            pass
        if msg.casefold() == 'q':
            print('***** 離開程式 *****')
            # quit
            pass
        self.status = msg

    def insert_fund(self):
        # 1. insert Fund table
        fund = DAOFactory().create_product('fund')

        # 1_1. search all data from Fund table
        funds_set = fund.select(self.conn) # TODO

        # 1_2. read etoro Fund csv file
        self.file_editor.is_exist('TODO') # TODO
        self.file_editor.read('TODO')  # TODO 讀取etoro匯出的資料
        self.file_editor.write('TODO')  # TODO 進行搬檔(1)，將讀取完的資料寫到complete資料夾
        self.file_editor.delete('TODO')  # TODO  進行搬檔(2)，移除資料來源檔
        # 1_3. convert csv file to FundBean set

        # 1_4. Set operation

        # 1_5. insert Fund table done
        # self.fund.insert(conn)
        pass

    def insert_portfolio(self):
        # 2. insert Portfolio
        portfolio = DAOFactory().create_product('portfolio')

        # 2_1. search all data from Portfolio table
        funds_set = portfolio.select(self.conn) # TODO

        # 2_2. read etoro Portfolio csv file
        self.file_editor.is_exist('TODO') # TODO
        self.file_editor.read('TODO')  # TODO 讀取etoro匯出的資料
        self.file_editor.write('TODO')  # TODO 進行搬檔(1)，將讀取完的資料寫到complete資料夾
        self.file_editor.delete('TODO')  # TODO  進行搬檔(2)，移除資料來源檔
        # 2_3. convert csv file to PortfolioBean set

        # 2_4. Set operation

        # 2_5. insert Portfolio table done
        pass
    def update_portfolio(self):
        # 2. insert Portfolio
        portfolio = DAOFactory().create_product('portfolio')

        # 2_1. search all data from Portfolio table
        funds_set = portfolio.select(self.conn)

        # 2_2. read etoro Portfolio csv file

        # 2_3. convert csv file to PortfolioBean set

        # 2_4. Set operation

        # 2_5. insert Portfolio table done
        pass
    def execute(self):
        self.welcome()
        self.interaction(input('請輸入:'))
        self.process(self.status)


print(1, '\n')
e = EtoroMain()
e.execute()
