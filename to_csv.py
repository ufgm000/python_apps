# command Line 
# pip install pandas
# pip install xlrd
import pandas as pd
import sys

excel = pd.read_excel('book2.xlsx')

# 入力引数を受け取る
#args = sys.argv

print(excel)


print(excel.drop(excel.index[[0,1]]))

print(excel.drop(excel.columns[[0]], axis=1))

print('\n\n')

# index   → 行操作
# columns → 列操作
excel = excel.drop(index = excel.index[[1]] , columns = excel.columns[[0]])

print(excel)

excel.to_csv('to_files.csv')

#空白の行がどうなるか試す