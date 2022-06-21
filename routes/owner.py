from fastapi import APIRouter

import nodes.node

router = APIRouter()
from nodes.owner import owner
from pydantic import BaseModel
from datetime import datetime


class owner_model(BaseModel):
    name:str
    phone_number:str
    password:str


class available_reservation(BaseModel):
    start: datetime
    end: datetime
    worker_id: str

class AddAvailableTime(BaseModel):
    start: datetime
    end: datetime
    owner_id: str
    worker_id: str
@router.post("/owners")
def create_owner(owner_input: owner_model):
    if owner.create_owner(owner_input.name, owner_input.password, owner_input.phone_number):
        return {'message': "owner created successfully "}
    return {'message': "Phone Number already exists"}

@router.get('/owners')
def show_all_owners():
    return owner.get_owners()




# @router.post('/add_blocked_time')
# def add_blocked_time(input_data: AddAvailableTime):
#     owner_node = nodes.node.find_node_by_id(input_data.owner_id)
#     if not owner_node[0]:
#         return {"message": "id is unknown"}
#     if owner_node[1][0]['labels'] != ['owner']:
#         return {"message": "id dose not have access to this function"}
#     owner.add_available_time(input_data.start, input_data.end, input_data.worker_id)
# @router.post("/availableReservation")
# def open_available_reservation(data_input: available_reservation):
    # owner_node = nodes.node.find_node_by_id(data_input.owner_id)
    # print(owner_node)






