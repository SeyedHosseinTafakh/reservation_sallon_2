from fastapi import APIRouter
router = APIRouter()
from pydantic import BaseModel
from nodes.saloon import saloon

class saloon_model(BaseModel):
    name:str
    phone_number:str
    address:str
    location:str
    owner_id:str

@router.post('/saloon')
def create_saloon(saloon_input:saloon_model):
    if saloon.create_saloon(name=saloon_input.name,
                         phone_number=saloon_input.phone_number,
                         address=saloon_input.address,
                         location=saloon_input.location,
                         owner_id=saloon_input.owner_id):
        return {"message":"saloon created"}
    return {"message":"error: unknown owner_id"}



