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
    customer_phone_number:str

@router.post('/reserve')
def make_reserve(input_data: reserve_class):
    if not node.find_node_by_id(input_data.worker_id)[0]:
        return {"message":"worker id is unknown"}

    if mysql.check_reserve_time(input_data.start_date,input_data.end_date,input_data.worker_id):
        return {"reservation already exist , check another time!"}
    mysql.make_reservation(input_data.start_date, input_data.end_date, input_data.customer_phone_number, input_data.worker_id)

@router.get('/reserve/{worker_id}')
def get_reserve_by_worker_id(worker_id):
    worker = node.find_node_by_id(worker_id)
    if not worker[0]:
        return {"message":"id is unknown"}
    if worker[1][0]['labels'] != ['worker']:
        return {"message":"id is unknown"}

    return mysql.get_reservation_by_by_worker_id(worker_id)



