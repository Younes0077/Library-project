from ui_py.remove_book_ui import RemoveBookUi
import sqlite3

from PyQt6.QtGui import QDoubleValidator

class MyRemoveBook(RemoveBookUi):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.grep_data_isbn()
        self.pushButton_done.clicked.connect(self.delete_data_book)
        self.comboBox_isbn.setValidator(QDoubleValidator(0.99, 99.99, 2))

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

    def delete_data_book(self):
        condition = True
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        isbn = self.comboBox_isbn.currentText()
        if isbn == "":
            condition = False
        else:
            isbn = int(self.comboBox_isbn.currentText())

        condition_isbn = False
        c.execute(f"SELECT * FROM book")
        records = c.fetchall()
        for rec in records:
            if rec[2] == isbn:
                condition_isbn = True
                print("isbn found")
                break
            else:
                condition_isbn = False

        if condition:
            if condition_isbn:
                c.execute(f"DELETE FROM book WHERE ISBN = {isbn}")
                conn.commit()
                conn.close()
                self.label_alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                           "margin-left:3px")
                self.label_alert.setText("book removed")

                self.comboBox_isbn.clear()
            else:
                self.label_alert.setText("isbn are not valid")
        else:
            self.label_alert.setText("Please complete the form")


