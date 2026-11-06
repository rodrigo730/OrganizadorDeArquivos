from PySide6.QtWidgets import QApplication


from window import MyWindow, setting_style
import sys 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setting_style(app)
    janela = MyWindow()
    janela.show()
    janela.fixing_size()
    app.setWindowIcon(janela.icon)
    app.exec()
    
