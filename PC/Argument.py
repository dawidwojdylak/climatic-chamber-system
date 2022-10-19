from tokenize import String

class Argument:
    """Class representing single argument within Command class string"""
    def __init__(self, arg : String, argType : String = None, descr : String = None,
    min : String = None, max : String = None, unit : String = None):
        self.arg    = arg
        self.argType= argType       # if argType != '' else None
        self.descr  = descr         # if descr != '' else None
        self.min    = float(min) if min else None
        self.max    = float(max) if max else None
        self.unit   = unit          # if unit  != '' else None

    def __str__(self) -> str:
        # if self.argType == "user_value" and (type(self.arg) != float or type(self.arg) != int):
            # print("The value is not set!")
            # return None
        # else:
        return self.arg

    def setValue(self, value):
        """Sets the value of user modifiable argument"""
        if self.argType == "user_value":
            if self.min != None and float(value) < self.min:
                print("Value is too low!")
                return
            if self.max != None and float(value) > self.max:
                print("Value is too high!")
                return
            self.arg = value
        else:
            print("Cannot set value for constant argument.")
