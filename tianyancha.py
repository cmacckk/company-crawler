#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosin
:date: 03/28/2019
"""
from tianyancha import crawler
from util import log
import urllib3
import logging
import pandas as pd
urllib3.disable_warnings()


log.set_file("./logs/tianyancha.log")

# excel列名
COLUMNS = ['公司名称', '统一社会信用代码', '公司地址']

# excel表名
OUTPUT_XLSX = './天眼查导出表.xlsx'

# 工作表名
SHEET_NAME = '天眼查'


if __name__ == '__main__':
    result = []
    with open('./keys.txt', 'r', encoding='utf-8') as f:
        keys = f.read().strip().split('\n')
        for key in keys:
            companies = crawler.start(key)
            for company in companies:
                result.append([company.name, company.credit_code, company.company_address])
    df = pd.DataFrame(result, columns = COLUMNS)
    # 导出为Excel时不带有索引
    df.to_excel(OUTPUT_XLSX, SHEET_NAME, index=False)
    logging.info(f"excel文件已导出到[ {OUTPUT_XLSX} ], 工作表名为 [ {SHEET_NAME} ]")



