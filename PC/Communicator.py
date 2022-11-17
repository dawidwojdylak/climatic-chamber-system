import sys                                                                  
from PySide2.QtCore import QObject, Slot, Signal

class Communicator(QObject):
    printErrSignal = Signal(str)
    
    def __init__(self):
        super(Communicator, self).__init__()

    # @Signal
    @staticmethod
    def eprint(msg : str):
        Communicator.printErrSignal.emit(msg)
        # sys.stderr.write(msg + "\n")

    # def eprint(self, msg : str):
    #     self.printErrSignal.emit(msg)
    #     # sys.stderr.write(msg + "\n")

