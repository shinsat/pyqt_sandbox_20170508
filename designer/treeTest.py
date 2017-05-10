from PyQt5.QtWidgets import *
from PyQt5.uic import *
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

#    ui = loadUi('QPushButton.ui')
    ui = QTreeWidget()
    ui.headerItem().setText(0, 'ヘッド')
    ui.headerItem().setText(1, '日付')

    ui.setWordWrap(True)


    for _ in range(3):
        item_displayed = QTreeWidgetItem()

#        label = QLabel('タイトル')
#        label.setWordWrap(True)
#        item_displayed.setText(0, 'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ')
        item_displayed.setText(0, 'タイトル')

        ui.addTopLevelItem(item_displayed)
#        ui.setItemWidget(item_displayed, 0, label)
        item_displayed.setText(1, '1111 - 東芝\n1234 - 日立')
        ui.addTopLevelItem(item_displayed)

        #ui.resizeColumnToContents(0)


        sub = QTreeWidgetItem(item_displayed)
#        sub.setText(0, 'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ')
        label = QLabel('ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ')
        label.setWordWrap(True)
        ui.addTopLevelItem(sub)
        ui.setItemWidget(sub, 0, label)

    ui.show()

    sys.exit(app.exec_())