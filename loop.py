# 3 2 1 GO!と表示するプログラム
for i in range(3,0,-1):
    print(i)
    if i==1:
        print("Go")

# 1 - 100までの数字の中から偶数の値を持つ値だけのListを作成してください。

result = []

for i in range(101):
    if i%2==0:
        result.append(i)

print(result)
