import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *ag_p, **krgs):
        if krgs:
            for  kp, vp in krgs.items():
                if kp == "__class__":
                    continue
                if kp in ["created_at", "updated_at"]:
                    setattr(self, kp, datetime.now())
                else:
                    setattr(self, kp, vp)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
