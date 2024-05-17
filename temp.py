#!/usr/bin/python3
import json
from models import storage
with open("file.json", "r") as f:
    content = json.load(f)
    print(content)

print("+++++++++++++++++++++++++++++++0")
print(storage.all())
