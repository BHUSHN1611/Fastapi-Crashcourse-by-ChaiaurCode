from fastapi import FastAPI
from pydantic import BaseModel

from typing import List

app = FastAPI()

class Tea(BaseModel):
    id:int
    name :str
    origin:str

teas:List[Tea] = []

@app.get("/")
def read_root():
    return {"msg":"Welcome To Fastapi Tea"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/addteas")
def add_tea(tea:Tea):
    teas.append(tea)
    return {"mk"}