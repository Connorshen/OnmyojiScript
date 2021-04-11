from PyQt5.QtWidgets import QMainWindow

from view.design.main_window import Ui_MainWindow


class MainWindowView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
