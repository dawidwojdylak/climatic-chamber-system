from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, Signal, Slot

class Ui_Login(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setObjectName("Login")
        self.resize(300, 150)
        self.setWindowTitle("Login")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_Login = QtWidgets.QLineEdit(self)
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Login)
        self.lineEdit_Password = QtWidgets.QLineEdit(self)
        self.lineEdit_Password.setText("")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Password)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.onAccept) # type: ignore
        self.buttonBox.rejected.connect(self.onCancel) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)
        self.login = None
        self.pwd = None

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("self", "Login"))
        self.label_2.setText(_translate("self", "Password"))

    def onAccept(self):
        self.login = self.lineEdit_Login.text()
        self.pwd = self.lineEdit_Password.text()
        self.accepted.emit()
        self.close()

    def onCancel(self):
        self.login = None
        self.pwd = None
        self.rejected.emit()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())
