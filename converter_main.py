import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
from pathlib import Path
import ctypes
# Importando a classe gerada pelo pyuic5
from converter_ui import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(r"converterSources\srcs\ico\troca.ico"))

        self.placeholder_text = "Escolha a PASTA dos arquivos a serem convertidos"
        self.ui.text_for_directory.setPlaceholderText(self.placeholder_text)

        self.ui.select_button.clicked.connect(self.search_for_dir)
        self.ui.convert_button.clicked.connect(self.convert)

    def search_for_dir(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Pasta")

        if directory:
            self.ui.text_for_directory.setText(directory)

    def convert(self):
        directory = self.ui.text_for_directory.toPlainText()

        if directory == self.placeholder_text:
            ctypes.windll.user32.MessageBoxW(
                0, "Por gentileza, selecione um diretorio", "Informação", 0x40 | 0x1)
            return

        counter = 0
        files = Path(directory).glob('*')
        for file in files:
            if Path(file).suffix == '.ret':
                counter += 1
                file.rename(file.with_suffix('.txt'))
        self.ui.label_for_counter.setText(f"Arquivos renomeados: {counter}")
        ctypes.windll.user32.MessageBoxW(
            0, f"Arquivos renomeados!\nQuantidade: {counter}", "Sucesso", 0x40)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()  # Mostra a janela principal
    sys.exit(app.exec_())  # Inicia o loop da aplicação
