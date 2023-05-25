import sqlite3

from ui_py.remove_person_ui import RemovePersonUi


class MyRemovePerson(RemovePersonUi):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.pushButton_done.clicked.connect(self.delete_data_person)

    def delete_data_person(self):
        condition = True
        conn = sqlite3.connect("./DataBase/libDatabase.db")
        c = conn.cursor()
        national = self.lineEdit_national_code.text()
        if national == "":
            condition = False
        print(national)

        if condition:
            c.execute(f"DELETE FROM Person WHERE NationalCode = {national}")
            conn.commit()
            conn.close()
            self.label_alert.setStyleSheet("color:rgb(40, 77, 0);\n"
                                       "margin-left:3px")
            self.label_alert.setText("person removed")

            self.lineEdit_national_code.clear()
        else:
            self.label_alert.setText("Please complete the form")



