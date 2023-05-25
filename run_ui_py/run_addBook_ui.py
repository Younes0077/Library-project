import sqlite3

from ui_py.addBook_ui import AddBookUi


class MyAddbook(AddBookUi):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        print("HERE")
        super().setupUi(Dialog)
        self.pushButton_done.clicked.connect(self.save_data)

    def save_data(self):

        condition = True;

        print("14")
        name = self.lineEdit_name.text()
        if name == "":
            condition = False
        author = self.lineEdit_Author.text()
        if author == "":
            condition = False
        isbn = self.lineEdit__ISBN.text()
        if isbn == "":
            condition = False
        translator = self.lineEdit_Translator.text()
        if translator == "":
            condition = False
        publication = self.lineEdit_Publicatipn.text()
        if publication == "":
            condition = False
        number_of_pages = self.lineEdit_NumberOfPages.text()
        if number_of_pages == "":
            condition = False

        if condition:
            conn = sqlite3.connect("./DataBase/libDatabase.db")
            print(conn)
            c = conn.cursor()
            if conn:
                print("connection ok")

            print(condition)

            c.execute(f"INSERT INTO book(Name, Author, ISBN, Translator, Publication, NumberOfPages)VALUES ('{name}', '{author}', '{isbn}', '{translator}','{publication}','{number_of_pages}');")

            conn.commit()
            conn.close()

            self.lineEdit_name.clear()
            self.lineEdit__ISBN.clear()
            self.lineEdit_Author.clear()
            self.lineEdit_Translator.clear()
            self.lineEdit_Publicatipn.clear()
            self.lineEdit_NumberOfPages.clear()

            self.label_Alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                           "margin-left:3px")
            self.label_Alert.setText("data saved")

        else:
            self.label_Alert.setText("Please complete the form")



