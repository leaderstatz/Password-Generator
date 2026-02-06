import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QSpinBox, QCheckBox, QLineEdit, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon

from classes.generate import Generate

class Window(QMainWindow):
    def __init__(self):
        """
        this function creates the GUI
        
        params:
        self
        """
        super().__init__()

        self.setWindowTitle("Password Generator.exe")
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon("assets/lock.png"))

        self.setWindowFlags(
            Qt.WindowType.CustomizeWindowHint |
            Qt.WindowType.WindowCloseButtonHint |
            Qt.WindowType.WindowMinimizeButtonHint |
            Qt.WindowType.WindowSystemMenuHint |
            Qt.WindowType.WindowTitleHint
        )

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        central_widget.setLayout(layout)

        self.length_box = QSpinBox()
        self.length_box.setRange(4, 64)
        self.length_box.setValue(12)

        self.label = QLabel("How long do u want ur pass to be?")

        self.label.setStyleSheet("font-size: 18px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.label)
        layout.addWidget(self.length_box)

        options = [
            "Uppercase",
            "Lowercase",
            "Numbers",
            "Symbols"
        ]

        # efficient method

        self.cached_options = {}

        for option in options: # <- this loop stores the options with their instances in the cache table
            self.cached_options[option] = QCheckBox(option)
        
        if self.cached_options["Uppercase"] and self.cached_options["Lowercase"]:
            self.cached_options["Uppercase"].setChecked(True)
            self.cached_options["Lowercase"].setChecked(True)
        else:
            print("the uppercase and lowercase check boxes are not found in the class")

        for option, instance in self.cached_options.items():
            layout.addWidget(instance)

        self.btn = QPushButton("Generate")
        self.btn.clicked.connect(lambda: Generate(self))

        layout.addWidget(self.btn)

        self.result = QLineEdit()
        self.result.setReadOnly(True)
        layout.addWidget(self.result)