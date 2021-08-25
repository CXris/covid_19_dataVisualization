#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:13:07 2021

@author: chris
"""
import xlrd
import xlwt

file = "2021"
filename = file + "_matrix.xls"

old_book = xlrd.open_workbook(filename)
old_table = old_book.sheet_by_index(0)

new_book = xlwt.Workbook(encoding='utf-8')
new_table = new_book.add_sheet(file+"词频矩阵")

nrows = old_table.nrows
ncols = old_table.ncols

for i in range(ncols):
    init = old_table.cell_value(0, i)
    new_table.write(0, i, init)

for m in range(nrows-1):
    for n in range(ncols):
        value = old_table.cell_value(m+1, n)
        if value != 1:
            new_table.write(m+1, n, 0)
        else:
            new_table.write(m+1, n, 1)

new_book.save(file+"_matrix.xls")
