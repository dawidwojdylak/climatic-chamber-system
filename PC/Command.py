from ast import arg
from tokenize import String
import Argument

class Command:
    """Class containing Climatic Chamber commands as Argument objects sequences"""
    def __init__(self, name : String):
        self.name = name
        self.request = []
        self.response = []
        self.description = ""

    def fillRequest(self, arg : Argument) -> None:
        """Appends Arguments to request command"""
        self.request.append(arg)

    def fillResponse(self, arg : Argument) -> None:
        """Append Arguments """
        self.response.append(arg)

    def fillDescription(self, descr : String) -> None:
        """Fills the argument description"""
        self.description = descr

    # TODO: correctness check
    def prepareRequest(self) -> String:
        """Returns ready-to-send request"""
        request = ""
        for arg in self.request:
            # if arg.argType == "user_value" and (type(arg.arg) != float or type(arg.arg) != int):
                # print("The value is not set!\nClearing request...")
                # return None
            request += str(arg)
        return request

    # def encodeResponse(self, response : String):
        # for arg in self.response:
            

    # TODO: check how many arguments are to be changed
    def setValue(self, value) -> None:
        """Sets value of argument with range check if needed"""
        for arg in self.request:
            if arg.argType == "user_value":
                if arg.min != None and float(value) < arg.min:
                    print("The value is too low. Min = " + str(arg.min))
                    return
                if arg.max != None and float(value) > arg.max:
                    print("The value is too high. Max = " + str(arg.max))
                    return
                arg.arg = str(value)

    def __str__(self) -> str:
        return self.prepareRequest()
    


class CommandRead(Command):
    def __init__(self):
        pass

class CommandSet(Command):
    def __init__(self):
        pass



if __name__ == "__main__":
    arg1 = Argument("T", '', "-2.3", "32.1")
