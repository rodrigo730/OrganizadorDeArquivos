import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QCheckBox, QLabel,
    QSlider, QComboBox, QLineEdit
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt


def create_dark_palette():
    """Create a dark color palette for the Fusion style."""
    palette = QPalette()

    # Base colors
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(35, 35, 35))

    # Disabled state
    palette.setColor(
        QPalette.ColorGroup.Disabled,
        QPalette.ColorRole.WindowText,
        QColor(127, 127, 127),
    )
    palette.setColor(
        QPalette.ColorGroup.Disabled,
        QPalette.ColorRole.Text,
        QColor(127, 127, 127),
    )
    palette.setColor(
        QPalette.ColorGroup.Disabled,
        QPalette.ColorRole.ButtonText,
        QColor(127, 127, 127),
    )
    palette.setColor(
        QPalette.ColorGroup.Disabled,
        QPalette.ColorRole.HighlightedText,
        QColor(127, 127, 127),
    )

    return palette


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dark Fusion Theme")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Dark Fusion palette example"))
        layout.addWidget(QLineEdit("Editable text"))
        layout.addWidget(QPushButton("Enabled Button"))

        disabled_btn = QPushButton("Disabled Button")
        disabled_btn.setEnabled(False)
        layout.addWidget(disabled_btn)

        layout.addWidget(QCheckBox("A checkbox option"))
        layout.addWidget(QSlider(Qt.Orientation.Horizontal))

        combo = QComboBox()
        combo.addItems(["First", "Second", "Third"])
        layout.addWidget(combo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
app.setStyle("Fusion")
app.setPalette(create_dark_palette())

window = MainWindow()
window.show()
sys.exit(app.exec())