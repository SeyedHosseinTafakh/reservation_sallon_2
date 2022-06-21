from fastapi import APIRouter
router = APIRouter()
from datetime import datetime
from pydantic import BaseModel
from services import mysql
from nodes import node
from nodes.worker import worker


class reserve_class(BaseModel):
    start_date: datetime
    end_date: datetime
    worker_id:str
    customer_phone_number:str #// TODO : make phone number validation

@router.post('/reserve')
def make_reserve(input_data: reserve_class):
    if not node.find_node_by_id(input_data.worker_id)[0]:
        return {"message":"worker id is unknown"}

    if mysql.check_reserve_time(input_data.start_date,input_data.end_date,input_data.worker_id)[0]:
        return {"reservation already exist , check another time!"}
    mysql.make_reservation(input_data.start_date, input_data.end_date, input_data.customer_phone_number, input_data.worker_id)







