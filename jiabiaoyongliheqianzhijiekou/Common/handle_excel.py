
from openpyxl import load_workbook
import json


class HandleExcel:

    def __init__(self,file_path,sheet_name):
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:  
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        all_datas = []
        titles = self.__read_titles()
        for item in list(self.sh.rows)[1:]: 
            values = []
            for val in item: 
                values.append(val.value)
            res = dict(zip(titles, values))
            all_datas.append(res)
        return all_datas


    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    import os
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
    exc = HandleExcel(file_path,"login")
    cases = exc.read_all_datas()
    exc.close_file()
    for case in cases:
        print(case)
