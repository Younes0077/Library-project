# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 536)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 536))
        Dialog.setStyleSheet("background-color:#8d99ae;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setStyleSheet("background-color:#2b2d42;\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.widget)
        self.frame_2.setStyleSheet("background-color:#8d99ae;\n"
"border-radius:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("padding-left:5px;\n"
"color:white")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_2.addWidget(self.lineEdit_name)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("padding-left:5px;\n"
"color:white")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_lastname = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_lastname.setFont(font)
        self.lineEdit_lastname.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.verticalLayout_2.addWidget(self.lineEdit_lastname)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("padding-left:5px;\n"
"color:white")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.lineEdit_NationalCode = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_NationalCode.setFont(font)
        self.lineEdit_NationalCode.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_NationalCode.setObjectName("lineEdit_NationalCode")
        self.verticalLayout_2.addWidget(self.lineEdit_NationalCode)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("padding-left:5px;\n"
"color:white")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lineEdit_phoneNumber = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_phoneNumber.setFont(font)
        self.lineEdit_phoneNumber.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_phoneNumber.setObjectName("lineEdit_phoneNumber")
        self.verticalLayout_2.addWidget(self.lineEdit_phoneNumber)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("padding-left:5px;\n"
"color:white")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_age = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_age.setFont(font)
        self.lineEdit_age.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.verticalLayout_2.addWidget(self.lineEdit_age)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("padding-left:5px;\n"
"color:white")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.lineEdit_registeryDate = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_registeryDate.setFont(font)
        self.lineEdit_registeryDate.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_registeryDate.setText("")
        self.lineEdit_registeryDate.setObjectName("lineEdit_registeryDate")
        self.verticalLayout_2.addWidget(self.lineEdit_registeryDate)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("padding-left:5px;\n"
"color:white")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit_address = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_address.setFont(font)
        self.lineEdit_address.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.verticalLayout_2.addWidget(self.lineEdit_address)
        self.label_Alert = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_Alert.setFont(font)
        self.label_Alert.setStyleSheet("color:rgb(204, 16, 16);\n"
"margin-left:3px")
        self.label_Alert.setText("")
        self.label_Alert.setObjectName("label_Alert")
        self.verticalLayout_2.addWidget(self.label_Alert)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.pushButton_done = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_done.setFont(font)
        self.pushButton_done.setStyleSheet("background-color:#2b2d42;\n"
"border-radius:6px;\n"
"color:white\n"
"")
        self.pushButton_done.setObjectName("pushButton_done")
        self.verticalLayout.addWidget(self.pushButton_done)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "name:"))
        self.label_2.setText(_translate("Dialog", "last name:"))
        self.label_8.setText(_translate("Dialog", "NationalCode"))
        self.label_5.setText(_translate("Dialog", "phone number:"))
        self.label_3.setText(_translate("Dialog", "age :"))
        self.label_6.setText(_translate("Dialog", "registery date:"))
        self.label_4.setText(_translate("Dialog", "address:"))
        self.pushButton_done.setText(_translate("Dialog", "D O N E !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
