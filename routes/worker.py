from fastapi import APIRouter
router = APIRouter()
from pydantic import BaseModel
from nodes.worker import worker



class worker_model(BaseModel):
    name:str
    phone_number:str
    password:str
    instagram_link:str

@router.post('/worker')
def create_worker(worker_input:worker_model):
    if worker.create_worker(name=worker_input.name, phone_number=worker_input.phone_number, password=worker_input.password,
                         instagram_link=worker_input.instagram_link):
        return {"message":"worker account created"}
    return {"message":"error phone number already exist in db"}

