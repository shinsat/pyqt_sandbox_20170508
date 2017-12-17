import sys, os, pprint, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class my_thread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self)
        self.parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        import time
        ct = 0
        while True:
            ct += 1
            #self.parent.addItem()
            #self.parent.data_in.emit()
            time.sleep(1)
        #    print(ct)
            #self.parent.get_data_row(1, val=str(ct))
            self.parent.update_data.emit(1, str(ct))



class App(QWidget):
    update_data = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()

        self.update_data.connect(self.get_data_row)

        self.ticker = my_thread(parent=self)
        self.ticker.start()

        self.vbox = QVBoxLayout()
        self.view = QTreeView()
        self.view.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['col1', 'col2', 'col3'])
        self.view.setModel(self.model)
        self.view.setUniformRowHeights(True)

        self.vbox.addWidget(self.view)
        self.setLayout(self.vbox)

        for i in range(3):
            self.parent1 = QStandardItem('Family {}. Some long status text for sp'.format(i))
            self.parent2 = QStandardItem('colum 2 field')
            self.parent3 = QStandardItem('colum 3 field')
            for j in range(3):
                child1 = QStandardItem('Child {}'.format(i*3+j))
                child2 = QStandardItem('row: {}, col: {}'.format(i, j+1))
                child3 = QStandardItem('row: {}, col: {}'.format(i, j+2))
                self.parent1.appendRow([child1, child2, child3])
            #self.model.appendRow(self.parent1)
            self.model.appendRow([self.parent1, self.parent2, self.parent3,])
            # span container columns
            #self.view.setFirstColumnSpanned(i, self.view.rootIndex(), True)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # expand third container
        index = self.model.indexFromItem(self.parent1)
        self.view.expand(index)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # select last row
        selmod = self.view.selectionModel()
        index2 = self.model.indexFromItem(child3)
        selmod.select(index2, QItemSelectionModel.Select|QItemSelectionModel.Rows)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #view.show()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @pyqtSlot(int, str)
    def get_data_row(self, row, val=None):
        #row_wgt = self.view.indexWidget(self.model.createIndex(1,1))
        row_wgt = self.view.model().itemFromIndex(self.view.model().index(row, 2))
        row_wgt2 = self.view.model().data(self.model.index(row, 0), Qt.DisplayRole)
      #  print(row_wgt.text())
        row_wgt.setData(val, Qt.EditRole)
        self.view.dataChanged(self.model.index(row, 0), self.model.index(row,0))
        new_data = QStandardItem('inserted row')
        #self.view.model().insertRow(row, new_data)
#        aaa = self.view.model().itemFromIndex(self.model.index(0, 0))
        #bbb = self.model.indexFromItem(self.parent1)
        #r = bbb.row()
        #c = bbb.column()
#        self.model.appendRow(row_wgt)
#        self.view.dataChanged(self.model.index(3,0), self.model.index(3, 0))
#        self.view.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wgt = App()
    wgt.show()

    #wgt.get_data_row(2, val='llll')

    sys.exit(app.exec_())
