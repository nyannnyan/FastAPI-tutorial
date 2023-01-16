from typing import List, Union
from enum import Enum

from fastapi import FastAPI, Query
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

@app.get("/items/")
async def read_items(
  q: Union[str, None] = Query(default=None, 
  title="Query string", 
  description="Query string for the items",
  min_length=3,
  deprecated=True)):
  result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    result.update({"q": q})
  return result