import sys
from Communicator import Communicator

class Argument:
    """Class representing single argument within Command class str"""
    def __init__(self, arg : str, argType : str = None, descr : str = None,
    min : str = None, max : str = None, unit : str = None):
        self.arg    = arg
        self.argType= argType       # if argType != '' else None
        self.descr  = descr         # if descr != '' else None
        self.min    = float(min) if min else None
        self.max    = float(max) if max else None
        self.unit   = unit          # if unit  != '' else None

    def __str__(self) -> str:
        # if self.argType == "user_value" and (type(self.arg) != float or type(self.arg) != int):
            # sys.stderr.write("The value is not set!\n")
            # return None
        # else:
        return self.arg

    def setValue(self, value):
        """Sets the value of user modifiable argument"""
        if self.argType == "user_value":
            if self.min != None and float(value) < self.min:
                Communicator.eprint("Value is too low!")
                return
            if self.max != None and float(value) > self.max:
                Communicator.eprint("Value is too high!")
                return
            self.arg = value
        else:
            Communicator.eprint("Cannot set value for constant argument.")

    def getArgType(self):
        return self.argType
