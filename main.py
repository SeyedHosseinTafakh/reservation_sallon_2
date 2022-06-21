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

