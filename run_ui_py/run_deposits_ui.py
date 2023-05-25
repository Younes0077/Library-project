import sqlite3
from ui_py.deposits_ui import DepositsUI


class MyAddDeposits(DepositsUI):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.pushButton_done.clicked.connect(self.save_data)

    def save_data(self):
        condition = True;

        code = self.lineEdit_NationalCode.text()
        if code == "":
            condition = False
        isbn = self.lineEdit_ISBN.text()
        if isbn == "":
            condition = False
        DateDeliveryFromPerson = self.lineEdit_DateDeliveryFromPerson.text()
        if DateDeliveryFromPerson == "":
            condition = False
        DateDeliveryToPerson = self.lineEdit_DateDeliveryToPerson.text()
        if DateDeliveryToPerson == "":
            condition = False

        if condition:
            conn = sqlite3.connect("./DataBase/libDatabase.db")
            c = conn.cursor()
            # c.execute(f"SELECT * FROM Person WHERE code = {code}")
            # records = c.fetchall()
            # for rec in records:
            #     print(rec)
            c.executescript(f"""INSERT INTO deposits(code,ISBN,DateDeliveryToPerson,DateDeliveryFromPerson)VALUES({code},{isbn},'{DateDeliveryToPerson}','{DateDeliveryToPerson}')""")
            conn.commit()
            conn.close()

            self.lineEdit_NationalCode.clear()
            self.lineEdit_ISBN.clear()
            self.lineEdit_DateDeliveryToPerson.clear()
            self.lineEdit_DateDeliveryFromPerson.clear()

            self.label_Alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                           "margin-left:3px")
            self.label_Alert.setText("data saved")

        else:
            self.label_Alert.setText("Please complete the form")