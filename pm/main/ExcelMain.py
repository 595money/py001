from pm.main.FileExecuter import FileExecuter
from pm.tool.io.ExcelEditor import ExcelEditor


class ExcelMain(FileExecuter):
    def __init__(self):
        self.excel_editor = ExcelEditor()
        self.status = 'input'

    def execute(self):

        while self.status != 'output':
            # 1.取得使用者輸入之檔案讀取路徑
            self.status = 'input'
            input_path = self.interaction(self.status)

            # 2.2. 路徑錯誤回到流程 1，路徑正確進入流程 3
            self.status = self.excel_editor.is_exist(input_path) and 'output' or 'wrong'
            if self.status == 'wrong':
                self.interaction(self.status)
        else:
            # 3.取得使用者輸入之檔案產出路徑
            output_path = self.interaction(self.status)

        # 4.讀取資源
        data = self.excel_editor.read(input_path)

        # 5.寫入檔案
        self.excel_editor.write(output_path, data)

        # 6.結束程式
        self.status = 'quit'
        self.interaction(self.status)

    def interaction(self, status):
        if status == 'input':
            return input('請輸入來源路徑: ')

        if status == 'output':
            return input('請輸入輸出路徑: ')

        if status == 'wrong':
            print('路徑錯誤，查無檔案')

        if status == 'quit':
            print('離開')


main = ExcelMain()
main.execute()
