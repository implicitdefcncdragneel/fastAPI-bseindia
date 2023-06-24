from pydantic import BaseModel

class DealsCreate(BaseModel):
    deal_date: str
    security_code: str
    security_name: str
    client_name: str
    deal_type: str
    quantity: str
    price: str

    class Config:
        orm_mode = True