from ast import arg
import Argument
import sys

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

    def prepareRequest(self) -> str:
        """Returns ready-to-send request"""
        if self.badRequest == True:
            return None
        request = ""
        for arg in self.request:
            request += str(arg)
        return request

    def parseChamberResponse(self, resp : str):
        """Encodes string of chamber response"""
        i = 0
        result = {}
        try:
            for arg in self.response:
                temp_str = ""
                if i >= len(resp): break
                for _ in arg.arg:
                    temp_str += resp[i]
                    i += 1
                if arg.descr != None:
                    result[arg.descr] = temp_str
            return result
        except Exception:
            raise


    def setValue(self, value : float) -> None:
        """Sets value of argument with range check if needed"""
        try:
            for arg in self.request:
                if arg.argType == "user_value":
                    if arg.min != None and float(value) < arg.min:
                        self.badRequest = True
                        return
                    if arg.max != None and float(value) > arg.max:
                        self.badRequest = True
                        return
                    if float(value) < 300.:
                        arg.arg = '%.2f' % float(value)
                    else:
                        arg.arg = '%.1f' % float(value)
            self.badRequest = False
        except Exception:
            raise

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description
    
    def isUserModifiable(self) -> bool:
        return self.userModifiable

    def getUserModifiableArguments(self):
        return [r for r in self.request if r.getArgType() == "user_value"]


if __name__ == "__main__":
    arg1 = Argument("T", '', "-2.3", "32.1")
