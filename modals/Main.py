import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class modal2(QDialog):
    def __init__(self):
        super().__init__()

        ui = loadUi('close_me2.ui', self)
        ui.pushButton.clicked.connect(self.btn_clicked)
        ui.pushButton_2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        print('clicked!')
        #self.close()
        self.done(8)

    def btn2_clicked(self):
        print('clicked2!')

        my_modal = modal2()
        my_modal.show()

        if my_modal.exec_() == 8:
            self.done(8)


class modal1(QDialog):
    def __init__(self):
        super().__init__()

        ui = loadUi('close_me2.ui', self)
        ui.pushButton.clicked.connect(self.btn_clicked)
        ui.pushButton_2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        print('clicked!')
        #self.close()
        self.done(8)

    def btn2_clicked(self):
        print('clicked2!')

        my_modal = modal2()
        my_modal.show()

        if my_modal.exec_() == 8:
            self.done(8)


class Main(QDialog):
    def __init__(self):
        super().__init__()

        ui = loadUi('close_me.ui', self)
        ui.pushButton.clicked.connect(self.btn_clicked)
        ui.pushButton_2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        print('clicked!')
        self.close()

    def btn2_clicked(self):
        print('clicked2!')

        my_modal = modal2()
        my_modal.show()

        #if my_modal.exec_() == 8:
        #    self.close()
        my_modal.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())