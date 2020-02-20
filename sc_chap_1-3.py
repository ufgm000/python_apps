import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)    # Webページを取得する

response.encoding = response.apparent_encoding # 文字化けしないようにする

filename = "chap1-3.txt"
with open(filename, mode="w") as f:     # ファイルを書込みモードで開く
    f.write(response.text)              # インターネットから取得したデータを書込む
