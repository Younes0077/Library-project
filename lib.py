# from ui_py.addBook_ui import AddBookUi
import sqlite3

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QMainWindow


from run_ui_py.run_remove_book_ui import MyRemoveBook
from run_ui_py.run_remove_person_ui import MyRemovePerson
from run_ui_py.run_deposits_ui import MyAddDeposits
from run_ui_py.run_addBook_ui import MyAddbook
from run_ui_py.run_registery_ui import MyRegisteryUi
from ui_py.main_ui import Ui_MainWindow


def remove_book():
    ui = MyRemoveBook()
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def remove_person():
    ui = MyRemovePerson()
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def add_deposits():
    ui = MyAddDeposits()
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def add_book():
    ui = MyAddbook()
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


def registery():
    ui = MyRegisteryUi()
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.exec()


class LibApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        print("hi")
        self.create_person_data_base(self)
        self.create_book_data_base(self)
        self.setupUi(self)
        self.grep_data_deposits()
        self.grep_data_person()
        self.grep_data_book()
        self.show()

        self.pushButton_add_person.clicked.connect(registery)
        self.pushButton_add_deposits.clicked.connect(add_deposits)
        self.pushButton_add_book.clicked.connect(add_book)
        self.pushButton_remove_person.clicked.connect(remove_person)
        self.pushButton_remove_book.clicked.connect(remove_book)

    @staticmethod
    def create_person_data_base(self):
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT exists Person(Name VarChar,LastName VarChar,NationalCode Varchar,PhoneNumber int,Age int,registeryDate date,Address text)")
        conn.commit()
        conn.close()

    @staticmethod
    def create_book_data_base(self):
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT exists book(Name Varchar,Author VarChar,ISBN int, Translator VarChar,Publication int,NumberOfPages int)")
        conn.commit()
        conn.close()

    def grep_data_person(self):
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Person")
        records = c.fetchall()
        counter = 0
        number_of_record = 0
        for rec in records:
            number_of_record = number_of_record + 1

        for rec in records:
            # print(counter)
            self.tableWidgetPerson.setRowCount(number_of_record)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetPerson.setVerticalHeaderItem(counter, item)

            for j in range(0, 7):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetPerson.setItem(counter, j, item)

            item = self.tableWidgetPerson.verticalHeaderItem(counter)
            # item.setText(self._translate("MainWindow", f"{counter+1}"))
            item.setText(f"{counter + 1}")

            item = self.tableWidgetPerson.item(counter, 0)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[0]}")
            item = self.tableWidgetPerson.item(counter, 1)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[1]}")
            item = self.tableWidgetPerson.item(counter, 2)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[2]}")
            item = self.tableWidgetPerson.item(counter, 3)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[3]}")
            item = self.tableWidgetPerson.item(counter, 4)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[4]}")
            item = self.tableWidgetPerson.item(counter, 5)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[5]}")
            item = self.tableWidgetPerson.item(counter, 6)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[6]}")

            counter = counter + 1
            # print(rec)

    def grep_data_book(self):
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM book")
        records = c.fetchall()
        counter = 0
        number_of_record = 0
        for rec in records:
            number_of_record = number_of_record + 1

        for rec in records:
            # print(counter)
            self.tableWidgetBooks.setRowCount(number_of_record)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetBooks.setVerticalHeaderItem(counter, item)

            for j in range(0, 8):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetBooks.setItem(counter, j, item)

            item = self.tableWidgetBooks.verticalHeaderItem(counter)
            # item.setText(self._translate("MainWindow", f"{counter+1}"))
            item.setText(f"{counter + 1}")

            item = self.tableWidgetBooks.item(counter, 0)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[0]}")
            item = self.tableWidgetBooks.item(counter, 1)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[1]}")
            item = self.tableWidgetBooks.item(counter, 2)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[2]}")
            item = self.tableWidgetBooks.item(counter, 3)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[3]}")
            item = self.tableWidgetBooks.item(counter, 4)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[4]}")
            item = self.tableWidgetBooks.item(counter, 5)
            # # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[5]}")


            counter = counter + 1
            # print(rec)

    def grep_data_deposits(self):
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM deposits")
        records = c.fetchall()
        counter = 0
        number_of_record = 0
        for rec in records:
            number_of_record = number_of_record + 1

        for rec in records:
            # print(counter)
            self.tableWidgetDeposits.setRowCount(number_of_record)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetDeposits.setVerticalHeaderItem(counter, item)

            for j in range(0, 5):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetDeposits.setItem(counter, j, item)

            item = self.tableWidgetDeposits.verticalHeaderItem(counter)
            # item.setText(self._translate("MainWindow", f"{counter+1}"))
            item.setText(f"{counter + 1}")

            item = self.tableWidgetDeposits.item(counter, 0)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[0]}")
            item = self.tableWidgetDeposits.item(counter, 1)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[1]}")
            item = self.tableWidgetDeposits.item(counter, 2)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[2]}")
            item = self.tableWidgetDeposits.item(counter, 3)
            # item.setText(self._translate("MainWindow", f"{rec[0]}"))
            item.setText(f"{rec[3]}")

            counter = counter + 1
