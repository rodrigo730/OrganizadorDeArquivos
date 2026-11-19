from PySide6.QtWidgets import  (QMainWindow, 
                                QWidget, 
                                QGridLayout, 
                                QLabel, 
                                QLineEdit,
                                QPushButton,
                                QMessageBox,
                                QComboBox
                                )
from PySide6.QtCore import QTimer
from qtpy.QtCore import QSize
from paths_files import FILE_ICON_PATH
from PySide6.QtGui import QIcon
import qdarkstyle
import mover_arquivos, organizador_extensao

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
        #Creating widget and layouts
        self.central_widget_ = QWidget()
        self._layout_label = QGridLayout()

        #Creating buttons 
        organizar = QPushButton('Digite o Caminho')
        self.input__ = MyInput()
        self.icon = QIcon(str(FILE_ICON_PATH))
        self.adding_extension = QPushButton('Extensões')
        self.botao1 = QPushButton('Organizar')
        self.mycombobox = MyComboBox()
        self.mycombobox.setVisible(False)
        
        self.contador = 0
        self.botao1.setProperty('cssClass', 'special')
        self.adding_extension.setProperty('cssClass', 'special')
        organizar.setProperty('cssClass', 'special')
        self.botao1.setChecked(True)

        self.botao1.clicked.connect(lambda: self.moving_files(self.input__.text()))
        self.adding_extension.clicked.connect(lambda: self.appending_new_extensions())
        self.adding_extension.setChecked(True)
        self.adding_wid(organizar,0,0, 1,1)
        self.adding_wid(self.input__, 1, 0, 1, 3)
        self.adding_wid(self.botao1,2,0,1,2)
        self.adding_wid(self.adding_extension, 0,1,1,1)
        self.adding_wid(self.mycombobox,0,3,1,3)

        self.setCentralWidget(self.central_widget_)
        self.central_widget_.setLayout(self._layout_label)
        self.setWindowTitle('Gerenciador de arquivos')

    def adding_wid(self, 
                a_widget: QWidget, 
                row: int,
                col: int, 
                rowspan: int, 
                colsspan:int, 
                ):
        self._layout_label.addWidget(a_widget,row, col,rowspan, colsspan)

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
        QTimer.singleShot(2500, _box_mensage.accept)
        _box_mensage.exec()
        
    def moving_files(self, value):
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

    def appending_new_extensions(self):
        self.mycombobox.setVisible(True)
        if self.contador == len(organizador_extensao.Pasta_extensao):
            return
        for i in organizador_extensao.Pasta_extensao:
            self.mycombobox.addItem(i.name)
            self.contador +=1
        
        print(self.contador)


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
class MyComboBox(QComboBox):
     def __init__(self,*args, **kwargs) -> None:
          super().__init__(*args, **kwargs)
    