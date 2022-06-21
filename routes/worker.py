from fastapi import APIRouter
router = APIRouter()
from pydantic import BaseModel
from nodes.worker import worker
from nodes import node
from edges import edge


class worker_model(BaseModel):
    name:str
    phone_number:str
    password:str
    instagram_link:str


class connect_worker_to_saloon(BaseModel):
    worker_id:str
    saloon_id:str


class disconnect_worker_to_saloon(BaseModel):
    worker_id:str
    saloon_id:str


@router.post('/worker')
def create_worker(worker_input:worker_model):
    if worker.create_worker(name=worker_input.name, phone_number=worker_input.phone_number, password=worker_input.password,
                         instagram_link=worker_input.instagram_link):
        return {"message":"worker account created"}
    return {"message":"error phone number already exist in db"}


@router.post('/connect_worker_to_saloon')
def connect_worker_to_saloon(nodes_input:connect_worker_to_saloon):
    first_node = node.find_node_by_id(nodes_input.worker_id)
    second_node = node.find_node_by_id(nodes_input.saloon_id)
    if not first_node[0]:
        return {"error":"worker id is unknown"}
    if not second_node[0]:
        return {"error":"saloon id is unknown"}
    connection = edge.check_connection(nodes_input.worker_id,nodes_input.saloon_id)
    if connection[0]:
        return {"error":"already existing connection"}
    edge.connect_nodes(first_node[1][0]['n']['id'],second_node[1][0]['n']['id'])

    return {"message":"worker connected to saloon"}


@router.post('/disconnect_worker_to_saloon')
def disconnect_worker_to_saloon(nodes_input:disconnect_worker_to_saloon):
    first_node = node.find_node_by_id(nodes_input.worker_id)
    second_node = node.find_node_by_id(nodes_input.saloon_id)
    if not first_node[0]:
        return {"error": "worker id is unknown"}
    if not second_node[0]:
        return {"error": "saloon id is unknown"}
    connection = edge.check_connection(nodes_input.worker_id, nodes_input.saloon_id)
    if not connection:
        return {"error": "no existing connection"}
    edge.delete_connection(first_node[1][0]['n']['id'],second_node[1][0]['n']['id'])
    return {"message":"worker connected deleted to saloon"}
