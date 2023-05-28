from ui_py.remove_book_ui import RemoveBookUi
import sqlite3


class MyRemoveBook(RemoveBookUi):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.grep_data_isbn()
        self.pushButton_done.clicked.connect(self.delete_data_book)

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
        print(isbn)

        if condition:
            c.execute(f"DELETE FROM book WHERE ISBN = {isbn}")
            conn.commit()
            conn.close()
            self.label_alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                       "margin-left:3px")
            self.label_alert.setText("book removed")

            self.comboBox_isbn.clear()
        else:
            self.label_alert.setText("Please complete the form")


