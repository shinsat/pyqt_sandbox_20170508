import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi


class Main(QWidget):
    def __init__(self):
        super().__init__()

        ui = loadUi('myUI.ui', self)

        ui.treeWidget.headerItem().setText(0, '認定')
        ui.treeWidget.headerItem().setText(1, '企業名')
        ui.treeWidget.headerItem().setText(2, '企業コード')
        ui.treeWidget.headerItem().setText(3, '')

        item = []

        for i in range(5):
            item.append(QTreeWidgetItem())

            item[-1].setText(1, '東芝')
            item[-1].setText(2, '6504')
            ui.treeWidget.addTopLevelItem(item[-1])

            cb = QCheckBox()
            ui.treeWidget.setItemWidget(item[-1], 0, cb)

            if i == 4:
                pb = QPushButton('新規')
            else:
                pb = QPushButton('編集')

            #pb.clicked.connect(lambda checked:self.bingo(item[-1].cb.isChecked()))
            ui.treeWidget.setItemWidget(item[-1], 3, pb)


    def bingo(self, checked):
        #print('clicked')
        print(checked)
'''
        model = QStringListModel()
        myList = []
        myList += ui.listWidget.addItem('1111')
        pb = QPushButton('Button')
        myList += pb
#        ui.listWidget.addItem('2222')
#        ui.listWidget.addItem('3333')

        ui.label.setText('TEST!')
        ui.pushButton1.setText('Back')
        ui.pushButton2.setText('Next')
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()


    window.show()

    sys.exit(app.exec_())