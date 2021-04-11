import sys, os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from view.widget.main_window_view import MainWindowView
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindowView()
    main_window.show()
    sys.exit(app.exec_())
