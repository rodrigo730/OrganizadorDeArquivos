import sys

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class PreferencesForm(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Preferências")

        self.theme_combo = QComboBox()
        self.theme_combo.addItem("Claro", "light")
        self.theme_combo.addItem("Escuro", "dark")
        self.theme_combo.addItem("Sistema", "system")

        self.category_combo = QComboBox()
        self.category_combo.addItem("Selecione...", None)
        self.category_combo.addItem("Interfaces gráficas", "gui")
        self.category_combo.addItem("Fundamentos", "basics")

        self.summary = QLabel()
        self.save_button = QPushButton("Salvar")
        self.save_button.setEnabled(False)

        form = QFormLayout()
        form.addRow("Tema", self.theme_combo)
        form.addRow("Categoria", self.category_combo)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.summary)
        layout.addWidget(self.save_button)

        self.category_combo.currentIndexChanged.connect(self.update_state)
        self.theme_combo.currentIndexChanged.connect(self.update_state)
        self.save_button.clicked.connect(self.save)
        self.update_state()

    def update_state(self, _index: int = -1) -> None:
        category_id = self.category_combo.currentData()
        theme_id = self.theme_combo.currentData()
        ready = category_id is not None
        self.save_button.setEnabled(ready)
        self.summary.setText(
            f"Tema: {theme_id} | Categoria: {category_id or 'não definida'}"
        )

    def save(self) -> None:
        category_id = self.category_combo.currentData()
        self.summary.setText(f"Preferências salvas para {category_id}.")


app = QApplication(sys.argv)
window = PreferencesForm()
window.show()
sys.exit(app.exec())