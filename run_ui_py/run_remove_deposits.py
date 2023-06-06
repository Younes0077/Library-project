from ui_py.remove_deposits_ui import RemoveDepositsUi
import sqlite3
from PyQt6.QtGui import QDoubleValidator


class MyRemoveDeposits(RemoveDepositsUi):
    def __init__(self):
        super().__init__()


    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.grep_data_person()
        self.grep_data_isbn()
        self.comboBox_isbn.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.comboBox_national_code.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.pushButton_done.clicked.connect(self.remove_data_deposits)

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
        self.comboBox_national_code.setEditable(True)
        # adding list of items to combo box
        self.comboBox_national_code.addItems(code_list)



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

    def remove_data_deposits(self):
        condition = True;

        code = self.comboBox_national_code.currentText()
        if code == "":
            condition = False
        else:
            code = int(self.comboBox_national_code.currentText())

        isbn = self.comboBox_isbn.currentText()
        if isbn == "":
            condition = False
        else:
            isbn = int(self.comboBox_isbn.currentText())

        time = self.lineEdit_time.text()
        if time == "":
            condition = False

        if condition:
            condition_code = False
            conn = sqlite3.connect("./DataBase/libDatabase.db")
            # find national code
            c = conn.cursor()
            c.execute(f"SELECT * FROM Person")
            records = c.fetchall()
            if not records:
                self.label_alert.setText("isbn or national code are not valid")
            for rec in records:
                print(rec[2])
                print(code)
                if rec[2] == code:
                    condition_code = True
                    print("code found")
                    break
                else:
                    condition_code = False
                    self.label_alert.setText("isbn or national code are not valid")

            # find isbn code
            condition_isbn = False
            c.execute(f"SELECT * FROM book")
            records = c.fetchall()
            if not records:
                self.label_alert.setText("isbn or national code are not valid")
            for rec in records:
                if rec[2] == isbn:
                    condition_isbn = True
                    print("isbn found")
                    break
                else:
                    condition_isbn = False
                    self.label_alert.setText("isbn or national code are not valid")

            # search for book and code in deposits
            condition_match = False
            if condition and condition_code and condition_isbn:
                c.execute(f"SELECT * FROM deposits")
                records = c.fetchall()
                for rec in records:
                    if rec[0] == code and rec[1] == isbn:
                        condition_match = True
                        break
                    else:
                        condition_match = False
                        self.label_alert.setText("This book Not loaned ")

            print(condition_code)
            print(condition_isbn)
            # print(condition_match)

            if condition and condition_code and condition_isbn and condition_match:
                conn = sqlite3.connect("./DataBase/libDatabase.db")
                c = conn.cursor()
                # code = int(self.comboBox_national_code.currentText())
                # isbn = int(self.comboBox_isbn.currentText())
                # time = self.lineEdit_time.text()
                c.execute(f"UPDATE deposits SET DateDeliveryFromPerson = '{time}' WHERE code = {code} AND ISBN = {isbn}")
                conn.commit()
                conn.close()
                self.label_alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                               "margin-left:3px")
                self.label_alert.setText("deposits removed")
                self.comboBox_isbn.clear()
                self.comboBox_national_code.clear()
                self.lineEdit_time.clear()

        else:
            self.label_alert.setText("Please complete the form")
