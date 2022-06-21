from typing import Union

from fastapi import FastAPI

from routes import owner
from routes import saloon
from routes import worker
from routes import reserve
app = FastAPI()
app.include_router(saloon.router)
app.include_router(owner.router)
app.include_router(worker.router)
app.include_router(reserve.router)
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


