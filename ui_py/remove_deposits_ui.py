# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class RemoveDepositsUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(642, 334)
        Dialog.setStyleSheet("background-color:#8d99ae;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(parent=Dialog)
        self.widget_3.setStyleSheet("background-color:#2b2d42;\n"
"border-radius:10px;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.widget_3)
        self.frame.setStyleSheet("background-color:#8d99ae;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_title = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:white")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_4.addWidget(self.label_title, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_national_code = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_national_code.setFont(font)
        self.label_national_code.setStyleSheet("color:white")
        self.label_national_code.setObjectName("label_national_code")
        self.verticalLayout_4.addWidget(self.label_national_code)
        self.comboBox_national_code = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox_national_code.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.comboBox_national_code.setObjectName("comboBox_national_code")
        self.verticalLayout_4.addWidget(self.comboBox_national_code)
        self.label_isbn = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_isbn.setFont(font)
        self.label_isbn.setStyleSheet("color:white")
        self.label_isbn.setObjectName("label_isbn")
        self.verticalLayout_4.addWidget(self.label_isbn)
        self.comboBox_isbn = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox_isbn.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.comboBox_isbn.setObjectName("comboBox_isbn")
        self.verticalLayout_4.addWidget(self.comboBox_isbn)
        self.label_time = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("color:white")
        self.label_time.setObjectName("label_time")
        self.verticalLayout_4.addWidget(self.label_time)
        self.lineEdit_time = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_time.setStyleSheet("background-color:rgb(255,255,255);\n"
"padding:3px;")
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.verticalLayout_4.addWidget(self.lineEdit_time)
        self.label_alert = QtWidgets.QLabel(parent=self.frame)
        self.label_alert.setStyleSheet("color:rgb(204, 16, 16);\n"
                                       "margin-left:3px")
        self.label_alert.setText("")
        self.label_alert.setObjectName("label_alert")
        self.verticalLayout_4.addWidget(self.label_alert)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget_3)
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
        self.label_title.setText(_translate("Dialog", "remove deposits"))
        self.label_national_code.setText(_translate("Dialog", "National_code:"))
        self.label_isbn.setText(_translate("Dialog", "ISBN of book:"))
        self.label_time.setText(_translate("Dialog", "time:"))
        self.pushButton_done.setText(_translate("Dialog", "D O N E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
