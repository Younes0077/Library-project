import sqlite3

from ui_py.remove_person_ui import RemovePersonUi
from PyQt6.QtGui import QDoubleValidator



class MyRemovePerson(RemovePersonUi):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.grep_data_person()
        self.pushButton_done.clicked.connect(self.delete_data_person)
        self.comboBox_natinal_code.setValidator(QDoubleValidator(0.99, 99.99, 2))

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
        self.comboBox_natinal_code.setEditable(True)
        # adding list of items to combo box
        self.comboBox_natinal_code.addItems(code_list)


    def delete_data_person(self):
        condition = True
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        code = self.comboBox_natinal_code.currentText()
        if code == "":
            condition = False
        else:
            code = int(self.comboBox_natinal_code.currentText())
        print(code)
        # find national code

        c.execute(f"SELECT * FROM Person")
        records = c.fetchall()
        condition_code = True
        for rec in records:
            print(rec[2])
            print(code)
            if rec[2] == code:
                condition_code = True
                print("code found")
                break
            else:
                condition_code = False

        if condition:
            if condition_code:
                c.execute(f"DELETE FROM Person WHERE NationalCode = {code}")
                conn.commit()
                conn.close()
                self.label_alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                           "margin-left:3px")
                self.label_alert.setText("person removed")

                self.comboBox_natinal_code.clear()
            else:
                self.label_alert.setText("national code are not valid")
        else:
            self.label_alert.setText("Please complete the form")



