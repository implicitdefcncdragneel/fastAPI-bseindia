from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Deals(Base):

    __tablename__ = 'deals'

    id = Column(Integer, primary_key=True)
    deal_date = Column(String(30))
    security_code = Column(String(30))
    security_name = Column(String(100))
    client_name = Column(String(255))
    deal_type = Column(String(5))
    quantity = Column(String(255))
    price = Column(Float)

    def __init__(self, deal_date, security_code, security_name, client_name, deal_type, quantity, price):
        self.deal_date = deal_date
        self.security_code = security_code
        self.security_name = security_name
        self.client_name = client_name
        self.deal_type = deal_type
        self.quantity = quantity
        self.price = price