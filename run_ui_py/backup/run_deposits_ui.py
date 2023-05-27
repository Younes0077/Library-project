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
        else:
            code = int(self.lineEdit_NationalCode.text())

        isbn = self.lineEdit_ISBN.text()
        if isbn == "":
            condition = False
        else:
            isbn = int(self.lineEdit_ISBN.text())

        DateDeliveryFromPerson = self.lineEdit_DateDeliveryFromPerson.text()
        if DateDeliveryFromPerson == "":
            condition = False
        DateDeliveryToPerson = self.lineEdit_DateDeliveryToPerson.text()
        if DateDeliveryToPerson == "":
            condition = False

        if condition:
            print("1")
            condition = False
            conn = sqlite3.connect("./DataBase/libDatabase.db")
            # find national code
            c = conn.cursor()
            c.execute(f"SELECT * FROM Person")
            records = c.fetchall()
            for rec in records:
                print(rec[2])
                print(code)
                if rec[2] == code:
                    condition = True
                    print("code found")
                    break
                else:
                    condition = False
                    self.label_Alert.setText("isbn or national code are not valid")

            # find isbn code

            c.execute(f"SELECT * FROM book")
            records = c.fetchall()
            for rec in records:
                if rec[2] == isbn:
                    condition = True
                else:
                    condition = False
                    self.label_Alert.setText("isbn or national code are not valid")

            # search for book and code in deposits
            c.execute(f"SELECT * FROM deposits")
            records = c.fetchall()
            for rec in records:
                if rec[0] == code and rec[1] == isbn:
                    condition = False
                    self.label_Alert.setText("This book has already been loaned to this person")
                else:
                    condition = True

            if condition:
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
