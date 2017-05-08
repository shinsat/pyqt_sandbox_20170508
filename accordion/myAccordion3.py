import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class myAccordionItem(QWidget):
    def __init__(self):
        super().__init__()


        pushButton = QPushButton("Hide")
        pushButton.setCheckable(True)

        ClearBtn = QPushButton("Clear")
        ClearBtn.setCheckable(True)
        #pushButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.textArea = QTextBrowser()
#        self.textArea.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#        self.textArea.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
#        self.textArea.setMaximumHeight(50)
#        self.textArea.setMinimumHeight(20)
        self.textArea.setText("こんにちわ")

        pushButton.clicked.connect(lambda checked: self.buttonClicked(checked, self.textArea))
        ClearBtn.clicked.connect(lambda checked: self.clearClicked(checked, self.textArea))

        h = QHBoxLayout()
        h.addWidget(pushButton)
        h.addWidget(self.textArea)
        h.addWidget(ClearBtn)

#        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setLayout(h)
        self.show()
#        v.setAlignment(self, Qt.AlignTop)


#        v.addLayout(h)

    def buttonClicked(self, checked, textArea):
        if checked:
            print("checked")
            textArea.hide()
            self.update()
#            self.layout().activate()
            self.parent().resize(self.sizeHint())

        else:
            print("notChecked")
            textArea.show()
            #self.update()
           # self.parent().sizeHint()
            self.parent().resize(self.sizeHint())

    def clearClicked(self, checked, textArea):
        if checked:
            print("checked")
            #textArea.hide()

        else:
            print("notChecked")
            #textArea.show()


#    def resizeEvent(self, newSize):
#        print("Resize me")
#        pass


class myAccordionSample(QWidget):
    def __init__(self, parent=None):
        super(myAccordionSample, self).__init__(parent)

        v = QVBoxLayout()
        
        for _ in range(3):
            ui = myAccordionItem()
            v.addWidget(ui)

#        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.setLayout(v)
        self.setGeometry(50, 50, 600, 400)
        self.show()

    def resizeEvent(self, newSize):
        print("Full resize!")
#        self.layout().activate()
        self.resize(self.sizeHint())
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.setGeometry(50, 50, 600, 600)

    ui = myAccordionSample(w)

    w.show()

#    ui = myAccordionItem()

    sys.exit(app.exec_())
