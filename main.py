
import sys
from PyQt6.QtWidgets import QApplication, QStyleFactory
from lib import LibApp

app = QApplication(sys.argv)

lib = LibApp()

sys.exit(app.exec())
