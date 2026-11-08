
from PySide6.QtWidgets import  (QMainWindow, 
                                QWidget, 
                                QGridLayout, 
                                QLabel, 
                                QLineEdit,
                                QPushButton,
                                QMessageBox
                                )
from PySide6.QtCore import QTimer
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
        self.input__ = MyInput()
        self.icon = QIcon(str(FILE_ICON_PATH))
        self.botao1 = QPushButton('Organizar')
        self.botao1.setProperty('cssClass', 'special')
        self.botao1.setChecked(True)
        self.botao1.clicked.connect(lambda: self.make_action(self.input__.text()))
        self.make_action_status = mover_arquivos.mover_arquivos
        self.adding_wid(label,1,1)
        self.adding_wid(self.input__,1,2)
        self.adding_wid(self.botao1,2,2)
        

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

    def make_mensage_box(self):
        return QMessageBox(self)

    def _show_error(self, text: str):
        _box_mensage = self.make_mensage_box()
        _box_mensage.setText(text)
        _box_mensage.setIcon(_box_mensage.Icon.Information)
        QTimer.singleShot(3000, _box_mensage.accept)
        _box_mensage.exec()
        
    
    def make_action(self, value):
        
        if not value:
            self._show_error("Status: \nCaminho não encontrado")
            return
        else:
            if mover_arquivos.mover_arquivos(value):
                self._show_error('Status: \nArquivos Movidos')
                self.make_action_status = True
            elif self.make_action_status:
                self._show_error('Status: \nArquivos já Movidos')
            if not self.botao1.isChecked():
                self.input__.clear()
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
            self.setPlaceholderText('Digite o caminho')
            
    def styling_widgets(self, a_widget: QWidget, msg: str):
                    a_widget.setStyleSheet(msg)

    