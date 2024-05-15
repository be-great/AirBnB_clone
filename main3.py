#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
status = True if "name" in my_model.__dict__.keys() else False
print("status :", status)
print(my_model.__dict__)
print(str(my_model.created_at))
