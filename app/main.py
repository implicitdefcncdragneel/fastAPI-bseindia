import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def data_test():
    url = '''https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'''

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
    }
    res = requests.get(url, headers=headers)
    c = res.content
    soup = BeautifulSoup(c, "html.parser")

    table = soup.find('table', id='ContentPlaceHolder1_gvbulk_deals')
    data = []

    rows = table.find_all('tr', class_='tdcolumn')

    for row in rows:
        cols = row.find_all('td')
        row_data = [col.text.strip() for col in cols]
        data.append(row_data)

    for row in data:
        print(row)
    