import pandas as pd

# csvファイルを読み込む
df = pd.read_csv("test.csv")

# 条件に合うデータを抽出
data_s = df[df["国語"] >= 80]

print("国語が80点以上 \n" ,data_s)

data_c = df[df["数学"] < 80 ]

print("数学が80点以下\n", data_c)