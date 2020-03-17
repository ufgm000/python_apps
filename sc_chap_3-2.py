import pandas as pd 

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 1列のデータを表示
print("国語の列データ\n",df["国語"])

# 複数の列のデータを表示
print("国語と数学の列データ\n",df[["国語","数学","社会"]])

# 行データ取得
print("C子のデータ\n",df.loc[2])

# 複数の行のデータを表示
print("C子とDのデータ\n",df.loc[[2,3]])

# 指定した行の指定した列のデータを表示
print("Cの国語のデータ\n",df.loc[2]["国語"])
