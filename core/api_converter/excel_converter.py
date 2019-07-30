# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     excel_converter
   Description :   read Excel then, convert to apis
                   also run the excel files
   Author :        patrick
   date：          2019/7/29
-------------------------------------------------
   Change Activity:
                   2019/7/29:
-------------------------------------------------
"""
import xlrd

from core.api_converter.api_model import BaseApiConverter

__author__ = 'patrick'

# book = xlrd.open_workbook("ontoservice_api.xlsx")
# fields = ["ONT服务", "优先级", "接口用途", "URL	mthod", "request_sample", "response_sample"]
# print(book)
#
# sh = book.sheet_by_index(0)
# print(sh.ncols, sh.nrows)
#
# for rx in range(1, sh.nrows):
#     print(rx)
#     print(type(sh.row(rx)[0]))
#     print(type(sh.row(rx)))
#
#     print(sh.cell(rx, 1).value)


class ExcelApiConverter(BaseApiConverter):
    headers = {
        "ContentType": "application/json",
        "Accept": "application/json"
    }

    def parse(self, target_file):
        book = xlrd.open_workbook(target_file)
        sh = book.sheet_by_index(0)
        for rx in range(1, sh.nrows):
            api_def = {'name': sh.cell(rx, 2).value, 'req_url': sh.cell(rx, 3).value, "headers": self.headers,
                       'req_body': sh.cell(rx, 5).value, 'method': sh.cell(rx, 4).value}
            self.api_context_data.append(api_def)
        return self.api_context_data


if __name__ == '__main__':
    ExcelApiConverter().generate_api_testcode("ontoservice_api.xlsx")
