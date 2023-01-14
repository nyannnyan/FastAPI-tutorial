from typing import Union
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  description: Union[str, None] = None
  price: float
  tax: Union[float, None] = None

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message": "Deep Learning FTW!"}

  if model_name.value == "lenet":
    return {"model_name": model_name, "message": "LeCNN all the images"}

  return {"model_name": model_name, "message": "Have some residuals"}

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
  result = {"item_id": item_id, **item.dict()}
  if q:
    result.update({"q": q})
  return result