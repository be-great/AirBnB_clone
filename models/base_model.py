
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            # Iterate through kwargs
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        )

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict