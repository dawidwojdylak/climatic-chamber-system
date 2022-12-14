import sys

class Argument:
    """Class representing single argument within Command class"""
    def __init__(self, arg : str, argType : str = None, descr : str = None,
    min : str = None, max : str = None, unit : str = None):
        self.arg    = arg
        self.argType= argType
        self.descr  = descr
        self.min    = float(min) if min else None
        self.max    = float(max) if max else None
        self.unit   = unit

    def __str__(self) -> str:
        return self.arg

    def setValue(self, value):
        """Sets the value of user modifiable argument"""
        if self.argType == "user_value":
            if self.min != None and float(value) < self.min:
                return
            if self.max != None and float(value) > self.max:
                return
            self.arg = value

    def getArgType(self):
        return self.argType
