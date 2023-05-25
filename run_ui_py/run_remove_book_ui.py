from ui_py.remove_book_ui import RemovePersonUi


class MyRemoveBook(RemovePersonUi):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        self.pushButton_done.clicked.connect(self.delete_data_book)

    def delete_data_book(self):
        pass
