import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        button = QPushButton("Click me!")
        button.clicked.connect(self.fade)
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
    def fade(self):
        self.setWindowOpacity(0.5)
        QTimer.singleShot(300, self.unfade)

    def unfade(self):
        self.setWindowOpacity(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())