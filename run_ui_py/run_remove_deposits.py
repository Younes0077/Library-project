from ui_py.remove_deposits_ui import RemoveDepositsUi
import sqlite3


class MyRemoveDeposits(RemoveDepositsUi):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.grep_data_person()
        self.grep_data_isbn()
        # self.pushButton_done.clicked.connect(Save_data)

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
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        c.execute(f"DELETE * from")