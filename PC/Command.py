from ast import arg
from tokenize import String

class Argument:
    def __init__(self, arg : String, argType : String = '', descr : String = '',
    min : String = '', max : String = '', unit : String = ''):
        self.arg    = arg
        self.argType= argType       if argType != '' else None
        self.descr  = descr         if descr != '' else None
        self.min    = float(min)    if min   != '' else None
        self.max    = float(max)    if max   != '' else None
        self.unit   = unit          if unit  != '' else None

    def __str__(self) -> str:
        if self.argType == "user_value" and (type(self.arg) != float or type(self.arg) != int):
            print("The value is not set!")
            return None
        else:
            return self.arg

    def setValue(self, value):
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

class Command:
    def __init__(self, name : String):
        self.name = name
        self.request = []
        self.response = []

    def fillRequest(self, arg : Argument):
        self.request.append(arg)

    def fillResponse(self, arg : Argument):
        self.response.append(arg)

    # TODO: correctness check
    def prepareRequest(self):
        request = ""
        for arg in self.request:
            if arg.argType == "user_value" and (type(self.arg) != float or type(self.arg) != int):
                print("The value is not set!\nClearing request...")
                return None
            request += str(arg)
        return request


class CommandRead(Command):
    def __init__(self):
        pass

class CommandSet(Command):
    def __init__(self):
        pass



if __name__ == "__main__":
    arg1 = Argument("T", '', "-2.3", "32.1")
