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