from PySide6.QtWidgets import  (QMainWindow, 
                                QWidget, 
                                QGridLayout, 
                                QLabel, 
                                QLineEdit,
                                QPushButton,
                                QMessageBox,
                                QComboBox,
                                QVBoxLayout
                                )
from PySide6.QtCore import QTimer
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
            background: {PRIMARY_COLOR};
            
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


class window_extension(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        self.fixing_size()
        self.setWindowTitle("Adicionar Extensão")

    def fixing_size(self):
            self.setFixedSize(300, 200)
            self.adjustSize()
    def adding_widgets(self, *args):
        for x in range(len(args)):
            self._layout.addWidget(args[x])

class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget| None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #Creating widget and layouts
        self.central_widget_ = QWidget()
        self._layout_label = QGridLayout()
        
        #Creating buttons main window
        organizar = QPushButton('Digite o Caminho')
        self.input__ = MyInput('Digite o Caminho')
        self.icon = QIcon(str(FILE_ICON_PATH))
        self.adding_extension = QPushButton('Extensões')
        self.botao1 = QPushButton('Organizar')

        #Creating buttons window adding new extensions
        self.mycombobox = MyComboBox()
        self.mycombobox.setVisible(False)
        self._window_new_extensions = window_extension()
        self.label_category = MyLabel('PASTAS')
        self.label_new_extension = MyLabel('NOVAS EXTENSÕES')
        self.input_new_extensions_folder = MyInput(
                                            'Adicione aqui o nome da pastas'
                                            )
        self.input_new_extensions = MyInput(
                                            'Adicione aqui as extensões'
                                            )
        self.button_new_extensions = QPushButton('Adicionar')
        
        self.contador = 0
        self.botao1.setProperty('cssClass', 'special')
        self.adding_extension.setProperty('cssClass', 'special')
        organizar.setProperty('cssClass', 'special')
        
        self.adding_extension.setCheckable(True)
        self.button_new_extensions.setCheckable(True)
        
        self.botao1.clicked.connect(
                                        lambda: 
                                        self.moving_files(self.input__.text())
                                                )
        self.adding_extension.clicked.connect(
                                        lambda: 
                                        self._creating_new_extensions_()
                                                )
        self.button_new_extensions.clicked.connect(
                                        lambda: 
                                        self.new_extensions_action()
                                                )
        self.appending_new_extensions()
        self.adding_wid((organizar,0,0, 1,1),
                        (self.input__, 1, 0, 1, 3),
                        (self.botao1,2,0,1,2),
                        (self.adding_extension, 0,1,1,1)
                        )

        self.setCentralWidget(self.central_widget_)
        self.central_widget_.setLayout(self._layout_label)
        self.setWindowTitle('Gerenciador de arquivos')

    def adding_wid(self, 
                   *args
                ):
        for x in args:
            self._layout_label.addWidget(*x)

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
        contador_teste = 0
        for i in organizador_extensao.Pasta_extensao:
                        self.mycombobox.addItem(i.name)
                        contador_teste +=1
        self.contador = contador_teste
        
    def _creating_new_extensions_(self):
        self.mycombobox.clear()
        self.appending_new_extensions()
        self.mycombobox.setVisible(True)
        self._window_new_extensions.adding_widgets(self.label_category, 
                                            self.mycombobox,
                                            self.label_new_extension,
                                            self.input_new_extensions_folder,
                                            self.input_new_extensions,
                                            self.button_new_extensions
                                                )
        self.changing_visible_window()
        
    def new_extensions_action(self):
        folder = self.input_new_extensions_folder.text()
        extension = self.input_new_extensions.text()
        organizador_extensao.creating_extension(folder, extension)
        self.appending_new_extensions()
        self.changing_visible_window()

    def changing_visible_window(self) :
        if self._window_new_extensions.isVisible():
            self.myclear()
            self._window_new_extensions.close()  
            return False
        else:
            self._window_new_extensions.show()
            return True
        
    def myclear(self):
        self.input_new_extensions_folder.clear()
        self.input_new_extensions.clear()

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
    def __init__(self,placeholder=None,*args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.styling_widgets(self, 
                                'lightgray; color: black'
                                )
            self.setPlaceholderText(f'{placeholder}')
            
    def styling_widgets(self, a_widget: QWidget, msg: str):
                    a_widget.setStyleSheet(msg)
class MyComboBox(QComboBox):
    def __init__(self,*args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.styling_widgets(self,
                                        'margin-left: 40px;'
                                        )
        
    def styling_widgets(self, a_widget: QWidget, msg: str):
                a_widget.setStyleSheet(msg)