from PySide6.QtWidgets import  QMainWindow, QWidget, QGridLayout


class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget| None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.central_widget_ = QWidget()
        self.setCentralWidget(self.central_widget_)
        self._layout_label = QGridLayout()
        self._layout_botoes = QGridLayout()
        self.central_widget_.setLayout(self._layout_label)
        self.central_widget_.setLayout(self._layout_botoes)
        self._layout_label.addChildLayout(self._layout_botoes)
        self.setWindowTitle('Gerenciador de arquivos')
        self.setStyleSheet('background-color: #212121')
    def adding_wid(self, a_widget: QWidget, col: int, row: int):
        self._layout_label.addWidget(a_widget,col, row)
    def styling_widgets(self, a_widget: QWidget, msg: str):
        a_widget.setStyleSheet(msg)
    def fixing_size(self):
        self.setFixedSize(350, 100)
        self.adjustSize()