import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "C:\mca_4th_sem\MoHFW _ Home.html"

soup = BeautifulSoup(open(url,mode='r',encoding='utf-8'),"html.parser")

table = soup.find_all('table')[0]

headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

rows = []
for tr in table.tbody.find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    rows.append(row)

#for row in rows:
 #   print(row)
df = pd.DataFrame(rows)
df.to_csv('Assignment1b.csv')
