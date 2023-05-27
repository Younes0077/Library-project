import sqlite3
from PyQt6.QtWidgets import QDialog
import sys
sys.path.append("..")
from ui_py.registery_ui import registeryUi


class MyRegisteryUi(registeryUi):
    def __init__(self):
        super().__init__()


    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.pushButton_done.clicked.connect(self.save_data)

    def save_data(self):
        condition = True
        name = self.lineEdit_name.text()
        if name == "":
            condition = False

        last_name = self.lineEdit_lastname.text()
        if last_name == "":
            condition = False

        national_code = self.lineEdit_NationalCode.text()
        if national_code == "":
            condition = False

        phone_number = self.lineEdit_phoneNumber.text()
        if phone_number == "":
            condition = False

        age = self.lineEdit_age.text()
        if age == "":
            condition = False

        registery_date = self.lineEdit_registeryDate.text()
        if registery_date == "":
            condition = False

        address = self.lineEdit_address.text()
        if address == "":
            condition = False

        if condition:
            conn = sqlite3.connect("./DataBase/libDatabase.db")
            c = conn.cursor()
#             c.execute(f""" INSERT INTO Person (Name, LastName, NationalCode,PhoneNumber,Age,registeryDate,Address)
# VALUES ('Cardinal', 'Stavanger', 115,937315,20,'salam','goodbye'); """)

            c.execute(f""" INSERT INTO Person (Name, LastName, NationalCode,PhoneNumber,Age,registeryDate,Address)
            VALUES ('{name}', '{last_name}', {national_code},{phone_number},{age},'{registery_date}','{address}'); """)

            conn.commit()
            conn.close()
            self.label_Alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                           "margin-left:3px")

            self.label_Alert.setText("data saved")

            self.lineEdit_address.clear()
            self.lineEdit_name.clear()
            self.lineEdit_lastname.clear()
            self.lineEdit_NationalCode.clear()
            self.lineEdit_registeryDate.clear()
            self.lineEdit_phoneNumber.clear()
            self.lineEdit_age.clear()

        else:
            self.label_Alert.setText("Please complete the form")



