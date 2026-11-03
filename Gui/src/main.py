from PySide6.QtWidgets import QApplication, QLabel, QLineEdit,QPushButton
from PySide6.QtGui import QIcon
from path_file_icon import FILE_PATH
from window import MyWindow
import sys 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MyWindow()
    label = QLabel('Digite o Caminho')
    input__ = QLineEdit()
    icon = QIcon(str(FILE_PATH))
    botao1 = QPushButton('Organizar')
    janela.styling_widgets(label,
                        'color: white; background-color: #385187; '
                        'border-style: solid;'
                        'border-width: 0px;'
                        'border-radius: 4px;')
    janela.styling_widgets(input__, f'background-color: lightgray')
    janela.styling_widgets(botao1, 'background-color: #385187; color: white')
    janela.adding_wid(label,1,1)
    janela.adding_wid(input__,1,2)
    janela.adding_wid(botao1,2,2)
    janela.show()
    janela.fixing_size()
    app.setWindowIcon(icon)
    app.exec()
    
