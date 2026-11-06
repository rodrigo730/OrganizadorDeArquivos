
from PySide6.QtWidgets import  (QMainWindow, 
                                QWidget, 
                                QGridLayout, 
                                QLabel, 
                                QLineEdit,
                                QPushButton
                                )
from paths_files import FILE_ICON_PATH
from PySide6.QtGui import QIcon
import qdarkstyle
import mover_arquivos
PRIMARY_COLOR = '#385187'
DARKER_PRIMARY_COLOR = '#2d416c'
DARKEST_PRIMARY_COLOR = '#243456'

qss = f"""
        QPushButton[cssClass="special"]{{
            color: #fff;
            background: {PRIMARY_COLOR}
        }}
        QPushButton[cssClass="special"]:hover{{
                    color: #fff;
                    background: {DARKER_PRIMARY_COLOR}
        }}
        QPushButton[cssClass="special"]:pressed{{
                    color: #fff;
                    background: {DARKEST_PRIMARY_COLOR}
        }}
"""
def setting_style(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    app.setStyleSheet(app.styleSheet() + qss)
    
class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget| None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.central_widget_ = QWidget()
        self._layout_label = QGridLayout()
        self._layout_botoes = QGridLayout()

        label = MyLabel('Digite o Caminho')
        input__ = MyInput()
        self.icon = QIcon(str(FILE_ICON_PATH))
        botao1 = QPushButton('Organizar')
        botao1.setProperty('cssClass', 'special')
        botao1.clicked.connect(lambda: self.make_action(input__.text()))
        
        self.adding_wid(label,1,1)
        self.adding_wid(input__,1,2)
        self.adding_wid(botao1,2,2)

        self.setCentralWidget(self.central_widget_)
        self.central_widget_.setLayout(self._layout_label)
        self.central_widget_.setLayout(self._layout_botoes)
        self._layout_label.addChildLayout(self._layout_botoes)
        
        self.setWindowTitle('Gerenciador de arquivos')

    def adding_wid(self, a_widget: QWidget, col: int, row: int):
        self._layout_label.addWidget(a_widget,col, row)

    def styling_widgets(self, a_widget: QWidget, msg: str):
        a_widget.setStyleSheet(msg)
        
    def fixing_size(self):
        self.setFixedSize(350, 100)
        self.adjustSize()
    def make_action(self, value):
        mover_arquivos.mover_arquivos(value)
class MyLabel(QLabel):
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.styling_widgets(self,
                            'color: white;'
                            'background-color: #385187;'
                            'border-style: solid;'
                            'border-width: 0px;'
                            'border-radius: 4px;'
                            )

    def styling_widgets(self, a_widget: QWidget, msg: str):
                a_widget.setStyleSheet(msg)

class MyInput(QLineEdit):
    def __init__(self,*args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.styling_widgets(self, 
                                'lightgray; color: black'
                                )
            self.setPlaceholderText('Digite aqui')
            
    def styling_widgets(self, a_widget: QWidget, msg: str):
                    a_widget.setStyleSheet(msg)