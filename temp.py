import json
from models.base_model import BaseModel


with open("file.json", "r") as f:
    objs = json.load(f)
    for k, v in objs.items():
       m = eval("BaseModel")(**v)
       print(m)