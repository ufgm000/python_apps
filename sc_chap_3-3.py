import pandas as pd

# csvファイルを読み込む
df = pd.read_csv("test.csv")

#
# 書き込み処理は行っていないので、csvファイルには影響なし
#

# 1列目のデータを追加
df["美術"] = [68,73,82,77]

print("列データ追加\n",df)

# 1行のデータを追加
df.loc[4] = ["E",90,92,94,96,92,100]

print('行データ追加\n',df)