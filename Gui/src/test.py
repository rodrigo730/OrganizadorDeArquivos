# Source - https://stackoverflow.com/a/76512736
# Posted by JordiBujons
# Retrieved 2026-11-22, License - CC BY-SA 4.0

import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QStandardItem

class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox,self).__init__(parent)
        self.setEditable(True)
        #self.lineEdit().setReadOnly(True)
        self.closeOnLineEditClick = False
        self.lineEdit().installEventFilter(self)
        self.model().dataChanged.connect(self.updateLineEditField)
    
    def eventFilter(self, widget, event: QEvent) -> bool:
        if widget == self.lineEdit():
            if event.type() == QEvent.Type.MouseButtonPress:
                if self.closeOnLineEditClick:
                    print("hide")
                    self.hidePopup()
                else:
                    print("show")
                    self.showPopup()
                    self.closeOnLineEditClick = True
                return True
        return super().eventFilter(widget, event)

    def addItems(self, items, itemList=None):
        itemList = [] if itemList is None else itemList
        for indx, text in enumerate(items):
            try:
                data = itemList[indx]
            except(IndexError):
                data = None
            self.addItem(text,data)
            

    def addItem(self,text,userData=None):
        item = QStandardItem()
        item.setText(text)
        if not userData is None:
            item.setData(userData)
        
        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        self.model().appendRow(item)
    
    def updateLineEditField(self):
        text_container = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                text_container.append(self.model().item(i).text())

        text_string=', '.join(text_container)
        self.lineEdit().setText(text_string)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200,800
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 10px;
            }
        ''')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        combobox = CheckableComboBox()
        combobox.addItems(colors)
        self.layout.addWidget(combobox)

    def closeEvent(self, event):
        event.accept()

if __name__ == '__main__':
    colors=["Blue", "Yellow", "Green", "Red"]
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing window...")
