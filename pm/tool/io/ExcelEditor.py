import os.path as sys_path
from pm.tool.io.Reader import Reader
from pm.tool.io.Writer import Writer


class ExcelEditor(Reader, Writer):

    def connect(self, path):
        pass

    def is_exist(self, path):
        return sys_path.isfile(path)

    def write(self, path, data):
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(''.join(data))

    def read(self, path):
        with open(path, 'r', encoding='UTF-8') as file:
            date_row = [line for line in file]
        return date_row


if __name__ == '__main__':
    e = ExcelEditor()
    path_in = input('in:')
    data = e.read(path_in)
    path_out = input('out')
    e.write(path_out, data)
