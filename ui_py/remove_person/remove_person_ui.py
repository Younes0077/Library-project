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
        Dialog.resize(633, 213)
        Dialog.setStyleSheet("background-color:#8d99ae;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setStyleSheet("background-color:#2b2d42;\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setStyleSheet("background-color:#8d99ae;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_national_code = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_national_code.setFont(font)
        self.label_national_code.setStyleSheet("color:white")
        self.label_national_code.setObjectName("label_national_code")
        self.verticalLayout_3.addWidget(self.label_national_code)
        self.comboBox_natinal_code = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox_natinal_code.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.comboBox_natinal_code.setObjectName("comboBox_natinal_code")
        self.comboBox_natinal_code.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_natinal_code)
        self.label_alert = QtWidgets.QLabel(parent=self.frame)
        self.label_alert.setStyleSheet("")
        self.label_alert.setText("")
        self.label_alert.setObjectName("label_alert")
        self.verticalLayout_3.addWidget(self.label_alert)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget)
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
        self.label.setText(_translate("Dialog", "Remove person"))
        self.label_national_code.setText(_translate("Dialog", "National_code:"))
        self.comboBox_natinal_code.setItemText(0, _translate("Dialog", "926114816"))
        self.pushButton_done.setText(_translate("Dialog", "D O N E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
