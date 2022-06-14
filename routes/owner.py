from fastapi import APIRouter
router = APIRouter()
from nodes.owner import owner
from pydantic import BaseModel


class owner_model(BaseModel):
    name:str
    phone_number:str
    password:str



@router.post("/owner")
def create_owner(owner_input: owner_model):
    if owner.create_owner(owner_input.name, owner_input.password, owner_input.phone_number):
        return {'message':"owner created successfully "}
    return {'message':"Phone Number already exists"}