#!/bin/env python

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# ------------------------------------------------------------------------------
# Open UI
# ------------------------------------------------------------------------------
def openUI():
    '''
    Open UI.
    '''
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec_())

# ------------------------------------------------------------------------------
# UI
# ------------------------------------------------------------------------------
class UI(QMainWindow):

    def __init__( self, parent=None ):

        ## Init:
        super(UI, self).__init__( parent )

        # ----------------
        # Create Simple UI with QTreeWidget
        # ----------------
        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.setCentralWidget(self.centralwidget)

        # ----------------
        # Set TreeWidget Headers
        # ----------------
        HEADERS = ( "column 1", "column 3", "column 2" )
        self.treeWidget.setColumnCount( len(HEADERS) )
        self.treeWidget.setHeaderLabels( HEADERS )

        # ----------------
        # Add Custom QTreeWidgetItem
        # ----------------
        ## Add Items:
        for name in [ 'rock', 'paper', 'scissors' ]:
            item = CustomTreeItem( self.treeWidget, name )

        ## Set Columns Width to match content:
        for column in range( self.treeWidget.columnCount() ):
            self.treeWidget.resizeColumnToContents( column )

# ------------------------------------------------------------------------------
# Custom QTreeWidgetItem
# ------------------------------------------------------------------------------
class CustomTreeItem( QTreeWidgetItem ):
    '''
    Custom QTreeWidgetItem with Widgets
    '''

    def __init__( self, parent, name ):
        '''
        parent (QTreeWidget) : Item's QTreeWidget parent.
        name   (str)         : Item's name. just an example.
        '''

        ## Init super class ( QtGui.QTreeWidgetItem )
        super( CustomTreeItem, self ).__init__( parent )

        ## Column 0 - Text:
        self.setText( 0, name )

        ## Column 1 - SpinBox:
        self.spinBox = QSpinBox()
        self.spinBox.setValue( 0 )
        self.treeWidget().setItemWidget( self, 1, self.spinBox )

        ## Column 2 - Button:
        self.button = QPushButton()
        self.button.setText( "button %s" %name )
        self.treeWidget().setItemWidget( self, 2, self.button )

        ## Signals
        self.treeWidget().clicked.connect( self.buttonPressed )

    @property
    def name(self):
        '''
        Return name ( 1st column text )
        '''
        return self.text(0)

    @property
    def value(self):
        '''
        Return value ( 2nd column int)
        '''
        return self.spinBox.value()

    def buttonPressed(self):
        '''
        Triggered when Item's button pressed.
        an example of using the Item's own values.
        '''
#        print "This Item name:%s value:%i" %( self.name,
#                                              self.value )


# ------------------------------------------------------------------------------
# __name__
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    openUI()