import sys
from classes.window import Window
from PySide6 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())