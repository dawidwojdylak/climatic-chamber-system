# from XmlProtocolParser import *
# from SshProtocolSender import */
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import UIControler

# TODO:
# - class diagram (look for desing patterns)
# - unit tests
# - when reading value read also description of argument
# - setting time value
# - prepare wrong argument handling
# - response handling

def setUp():
    UIControler.setUpWindow()

if __name__ == "__main__":
    setUp()    
