from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy.exc import SQLAlchemyError
from models import Deals
from schema import DealsCreate,DealUpdate

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://admin:admin@bsedb:5432/bsedeals")

@app.get("/")
def list_deals():
    """
    Get a list of all deals.

    Returns:
        dict: A dictionary containing a list of deals.
    """

    deals = db.session.query(Deals).all()
    return {"message": deals}

@app.post("/")
def create_deal(deal: DealsCreate):
    """
    Create a new deal.

    Args:
        deal: The deal data to create.

    Returns:
        dict: A dictionary containing a message indicating success.
    """

    try:
        new_deal = Deals(
            deal_date=deal.deal_date,
            security_code=deal.security_code,
            security_name=deal.security_name,
            client_name=deal.client_name,
            deal_type=deal.deal_type,
            quantity=deal.quantity,
            price=deal.price
        )
        db.session.add(new_deal)
        db.session.commit()
        return {"message": "Deal created successfully"}
    except SQLAlchemyError as e:
        db.session.rollback()
        raise HTTPException(status_code=400, detail="Could not create deal")


@app.patch("/")
def update_deal(deal: DealUpdate):
    """
    Update an existing deal.

    Args:
        deal: The deal data to update.

    Returns:
        dict: A dictionary containing a message indicating success.
    """

    try:
        existing_deal = db.session.query(Deals).get(deal.id)
        if existing_deal:
            existing_deal.deal_date = deal.deal_date
            existing_deal.security_code = deal.security_code
            existing_deal.security_name = deal.security_name
            existing_deal.client_name = deal.client_name
            existing_deal.deal_type = deal.deal_type
            existing_deal.quantity = deal.quantity
            existing_deal.price = deal.price
            db.session.commit()
            return {"message": "Deal updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Deal not found")
    except SQLAlchemyError as e:
        db.session.rollback()
        raise HTTPException(status_code=400, detail="Could not update deal")

@app.delete("/")
def delete_deal(deal_id: int):
    """
    Delete a deal.

    Args:
        deal_id: The ID of the deal to delete.

    Returns:
        dict: A dictionary containing a message indicating success.
    """
    
    try:
        deal = db.session.query(Deals).get(deal_id)
        if deal:
            db.session.delete(deal)
            db.session.commit()
            return {"message": "Deal deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Deal not found")
    except SQLAlchemyError as e:
        db.session.rollback()
        raise HTTPException(status_code=400, detail="Could not delete deal")