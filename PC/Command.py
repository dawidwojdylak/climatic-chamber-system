from ast import arg
from tokenize import String
import Argument
import sys
import Communicator

class Command:
    """Class containing Climatic Chamber commands as Argument objects sequences"""
    def __init__(self, name : str, cmdType = False):
        self.name = name
        self.request = []
        self.response = []
        self.description = ""
        self.userModifiable = cmdType
        self.badRequest = False

    def fillRequest(self, arg : Argument) -> None:
        """Appends Arguments to request command"""
        self.request.append(arg)

    def fillResponse(self, arg : Argument) -> None:
        """Append Arguments """
        self.response.append(arg)

    def fillDescription(self, descr : str) -> None:
        """Fills the argument description"""
        self.description = descr

    def setCommandType(self, cmdType : str) -> None:
        """Sets type of the command. It can be read-command or set-command"""
        self.userModifiable = True if cmdType == "user_value" else False

    # TODO: correctness check
    def prepareRequest(self) -> String:
        """Returns ready-to-send request"""
        if self.badRequest == True:
            Communicator.eprint("Bad request")
            return None
        request = ""
        for arg in self.request:
            # if arg.argType == "user_value" and (type(arg.arg) != float or type(arg.arg) != int):
                # sys.stderr.write("The value is not set!\nClearing request...")
                # return None
            request += str(arg)
        return request

    # def encodeResponse(self, response : String):
        # for arg in self.response:
            

    # TODO: check how many arguments are to be changed
    def setValue(self, value) -> None:
        """Sets value of argument with range check if needed"""
        try:
            for arg in self.request:
                if arg.argType == "user_value":
                    if arg.min != None and float(value) < arg.min:
                        Communicator.eprint("The value is too low. Min = " + str(arg.min))
                        self.badRequest = True
                        return
                    if arg.max != None and float(value) > arg.max:
                        Communicator.eprint("The value is too high. Max = " + str(arg.max))
                        self.badRequest = True
                        return
                    arg.arg = str(value)
            self.badRequest = False
        except Exception as e:
            print(e)

    # def __str__(self) -> str:
        # return self.prepareRequest()

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description
    
    def isUserModifiable(self) -> bool:
        return self.userModifiable

    def getUserModifiableArguments(self):
        return [r for r in self.request if r.getArgType() == "user_value"]


class CommandRead(Command):
    def __init__(self):
        pass

class CommandSet(Command):
    def __init__(self):
        pass



if __name__ == "__main__":
    arg1 = Argument("T", '', "-2.3", "32.1")
