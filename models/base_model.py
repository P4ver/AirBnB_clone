#!/usr/bin/python3
"""BaseModel class creat and manage model inst,"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents BaseModel that will creat and manage model inst.
    """
    def __init__(self, *ag_p, **krgs):
        """
        Initialization:
        Args:
            *ag_p: will not use it,
            **krgs: kp and vp of attributes.
        """
        if krgs:
            for kp, vp in krgs.items():
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
        """Return str repr,"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"

    def save(self):
        """updated_at will be updated with the crnt dtime,"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return 'dict' of BaseModel,"""
        dct_o = self.__dict__.copy()
        dct_o["created_at"] = self.created_at.isoformat()
        dct_o["updated_at"] = self.updated_at.isoformat()
        dct_o['__class__'] = self.__class__.__name__
        return dct_o
