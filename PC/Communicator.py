import sys                                                                  
from PySide2.QtCore import QObject, Slot, Signal

class Communicator(QObject):
    @Signal
    @staticmethod
    def eprint(msg : str):
        printErrSignal.emit(msg)
        # sys.stderr.write(msg + "\n")
    printErrSignal = Signal(str)

