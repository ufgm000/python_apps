import requests
from bs4 import BeautifulSoup
import csv

load_url = "https://www.aeoncinema.com/cinema2/kakamigahara/monthly/index.html"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

#table
table = soup.find_all("table", {"class":"detail_monthly_movie"})[0]
rows = table.find_all("tr")

print(rows)
#for element in table.find_all:
#    print(element.dev)

with open("cinema.csv","x", encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for cell in row.find_all(['td','th']):
            csvRow.append(cell.get_Text())
        writer.writerow(csvRow)
