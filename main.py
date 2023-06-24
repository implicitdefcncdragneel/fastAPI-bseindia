import requests
from fastapi import FastAPI,Depends
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from models import Deals
from schema import DealsCreate

app = FastAPI()

# @app.get("/")
# def data_test(db: Session = Depends(db_session)):
#     url = '''https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'''

#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
#     }
#     res = requests.get(url, headers=headers)
#     c = res.content
#     soup = BeautifulSoup(c, "html.parser")

#     table = soup.find('table', id='ContentPlaceHolder1_gvbulk_deals')
#     data = []

#     rows = table.find_all('tr', class_='tdcolumn')

#     for row in rows:
#         cols = row.find_all('td')
#         row_data = [col.text.strip() for col in cols]
#         data.append(row_data)

#     for row in data:
#         deal = DealsCreate(
#             deal_date=row[0],
#             security_code=row[1],
#             security_name=row[2],
#             client_name=row[3],
#             deal_type=row[4],
#             quantity=row[5],
#             price=row[6],
#         )
#         db_deal = Deals(**deal.dict())
#         db.add(db_deal)
#         db.commit()

#     return {"data": data}

# @app.get("/deals")
# def list_deals(db: Session = Depends(db_session)):
#     deals = db.query(Deals).all()
#     return {"deals": deals}
