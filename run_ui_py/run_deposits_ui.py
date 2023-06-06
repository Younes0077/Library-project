import sqlite3
from datetime import date
from ui_py.add_deposits_ui import DepositsUI
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QDoubleValidator


class MyAddDeposits(DepositsUI):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.grep_data_person()
        self.grep_data_isbn()
        self.time()
        self.comboBox_isbn.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.comboBox_code.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.pushButton_done.clicked.connect(self.save_data)

    def time(self):
        today = date.today()
        year = str(today.year)
        month = str(today.month)
        day = str(today.day)
        self.lineEdit_DateDeliveryToPerson.setText(f"{year}/{month}/{day}")
        # print(self.comboBox_isbn.currentText())

    def grep_data_person(self):
        code_list = []
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        # find national code
        c = conn.cursor()
        c.execute(f"SELECT * FROM Person")
        records = c.fetchall()
        for rec in records:
            code_list.append(str(rec[2]))
        # making it editable
        self.comboBox_code.setEditable(True)
        # adding list of items to combo box
        self.comboBox_code.addItems(code_list)

    def grep_data_isbn(self):
        isbn_list = []
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        # find national code
        c = conn.cursor()
        c.execute(f"SELECT * FROM book")
        records = c.fetchall()
        print(records)
        for rec in records:
            isbn_list.append(str(rec[2]))
        # making it editable
        self.comboBox_isbn.setEditable(True)
        # adding list of items to combo box
        self.comboBox_isbn.addItems(isbn_list)


    def save_data(self):
        condition = True;

        code = self.comboBox_code.currentText()
        if code == "":
            condition = False
        else:
            code = int(self.comboBox_code.currentText())

        isbn = self.comboBox_isbn.currentText()
        if isbn == "":
            condition = False
        else:
            isbn = int(self.comboBox_isbn.currentText())

        ScheduledTime = self.lineEdit_DateDeliveryFromPerson_Scheduled.text()
        if ScheduledTime == "":
            condition = False
        DateDeliveryToPerson = self.lineEdit_DateDeliveryToPerson.text()
        if DateDeliveryToPerson == "":
            condition = False

        if condition:
            condition_code = False
            conn = sqlite3.connect("./DataBase/libDatabase.db")
            # find national code
            c = conn.cursor()
            c.execute(f"SELECT * FROM Person")
            records = c.fetchall()
            if not records:
                self.label_Alert.setText("isbn or national code are not valid")
            for rec in records:
                print(rec[2])
                print(code)
                if rec[2] == code:
                    condition_code = True
                    print("code found")
                    break
                else:
                    condition_code = False
                    self.label_Alert.setText("isbn or national code are not valid")

            # find isbn code
            condition_isbn = False
            c.execute(f"SELECT * FROM book")
            records = c.fetchall()
            if not records:
                self.label_Alert.setText("isbn or national code are not valid")
            for rec in records:
                if rec[2] == isbn:
                    condition_isbn = True
                    print("isbn found")
                    break
                else:
                    condition_isbn = False
                    self.label_Alert.setText("isbn or national code are not valid")

            # search for book and code in deposits
            condition_match = False
            if condition and condition_code and condition_isbn:
                c.execute(f"SELECT * FROM deposits")
                records = c.fetchall()
                for rec in records:
                    if rec[0] == code and rec[1] == isbn:
                        condition_match = False
                        self.label_Alert.setText("This book has already been loaned to this person")
                        break
                    else:
                        condition_match = True

            print(condition_code)
            print(condition_isbn)
            print(condition_match)

            if condition and condition_code and condition_isbn and condition_match:
                conn = sqlite3.connect("./DataBase/libDatabase.db")
                c = conn.cursor()
                c.execute(f"""INSERT INTO deposits(code,ISBN,DateDeliveryToPerson,ScheduledTime)VALUES({code},{isbn},'{DateDeliveryToPerson}','{ScheduledTime}')""")
                conn.commit()
                conn.close()
                self.comboBox_code.clear()
                self.comboBox_isbn.clear()
                self.lineEdit_DateDeliveryToPerson.clear()
                self.lineEdit_DateDeliveryFromPerson_Scheduled.clear()

                self.label_Alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                               "margin-left:3px")
                self.label_Alert.setText("data saved")

        else:
            self.label_Alert.setText("Please complete the form")
