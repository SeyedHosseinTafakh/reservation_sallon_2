from fastapi import APIRouter
router = APIRouter()
from pydantic import BaseModel
from nodes.worker import worker
from nodes import node
from edges import edge
from nodes.saloon import saloon

class worker_model(BaseModel):
    name:str
    phone_number:str
    password:str
    instagram_link:str
    saloon_id:str


class connect_worker_to_saloon(BaseModel):
    worker_id:str
    saloon_id:str


class disconnect_worker_to_saloon(BaseModel):
    worker_id:str
    saloon_id:str


@router.post('/worker')
def create_worker(worker_input:worker_model):
    saloon = node.find_node_by_id(worker_input.saloon_id)
    if not saloon[0]:
        return {'message': "saloon id is unkown"}
    if saloon[1][0]['labels'] != ['saloon']:
        return {'message': "saloon id is unkown"}
    worker_id = worker.create_worker(name=worker_input.name,
                                     phone_number=worker_input.phone_number,
                                     password=worker_input.password,
                                     instagram_link=worker_input.instagram_link)
    if not worker_id:
        return {"message":"phone number already exist in db"}
    edge.connect_nodes(first_node_id=worker_input.saloon_id,second_node_id=worker_id)
    return {"message":"worker created"}


# @router.post('/connect_worker_to_saloon')
# def connect_worker_to_saloon(nodes_input:connect_worker_to_saloon):
#     first_node = node.find_node_by_id(nodes_input.worker_id)
#     second_node = node.find_node_by_id(nodes_input.saloon_id)
#     if not first_node[0]:
#         return {"error":"worker id is unknown"}
#     if not second_node[0]:
#         return {"error":"saloon id is unknown"}
#     connection = edge.check_connection(nodes_input.worker_id,nodes_input.saloon_id)
#     if connection[0]:
#         return {"error":"already existing connection"}
#     edge.connect_nodes(first_node[1][0]['n']['id'],second_node[1][0]['n']['id'])
#
#     return {"message":"worker connected to saloon"}


# @router.post('/disconnect_worker_from_saloon')
# def disconnect_worker_to_saloon(nodes_input:disconnect_worker_to_saloon):
#     first_node = node.find_node_by_id(nodes_input.worker_id)
#     second_node = node.find_node_by_id(nodes_input.saloon_id)
#     if not first_node[0]:
#         return {"error": "worker id is unknown"}
#     if not second_node[0]:
#         return {"error": "saloon id is unknown"}
#     connection = edge.check_connection(nodes_input.worker_id, nodes_input.saloon_id)
#     if not connection:
#         return {"error": "no existing connection"}
#     edge.delete_connection(first_node[1][0]['n']['id'],second_node[1][0]['n']['id'])
#     return {"message":"worker connected deleted to saloon"}


@router.get('/workers/{saloon_id}')
def get_workers(saloon_id):
    return saloon.get_saloon_workers(saloon_id)

