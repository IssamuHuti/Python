import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox, QInputDialog
)


class Conversor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Moedas (com API)")
        self.setFixedSize(350, 200)

        self.label_valor = QLabel("Valor:")
        self.input_valor = QLineEdit()

        self.combo_origem = QComboBox()
        self.combo_destino = QComboBox()
        moedas = ["USD", "BRL", "EUR", "JPY", "GBP"]
        self.combo_origem.addItems(moedas)
        self.combo_destino.addItems(moedas)

        self.botao_converter = QPushButton("Converter")
        self.botao_converter.clicked.connect(self.converter)

        layout_valor = QHBoxLayout()
        layout_valor.addWidget(self.label_valor)
        layout_valor.addWidget(self.input_valor)

        layout_moedas = QHBoxLayout()
        layout_moedas.addWidget(self.combo_origem)
        layout_moedas.addWidget(QLabel("→"))
        layout_moedas.addWidget(self.combo_destino)

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_valor)
        layout_principal.addLayout(layout_moedas)
        layout_principal.addWidget(self.botao_converter)

        self.setLayout(layout_principal)

    def converter(self):
        try:
            valor = float(self.input_valor.text())
        except ValueError:
            QMessageBox.warning(self, "Erro", "Digite um valor válido.")
            return

        de = self.combo_origem.currentText()
        para = self.combo_destino.currentText()

        if de == para:
            QMessageBox.information(self, "Resultado", f"{valor:.2f} {de} = {valor:.2f} {para}")
            return

        taxa = self.pegar_taxa_api(de, para)

        if taxa is None:
            taxa, ok = QInputDialog.getDouble( # QInputDialog.getDouble() = Entrada manual da taxa se API falhar
                self, "Taxa Manual",
                f"Digite a taxa de conversão de {de} para {para}:",
                decimals=6
            )
            if not ok:
                QMessageBox.warning(self, "Cancelado", "Conversão cancelada.")
                return

        resultado = valor * float(taxa)
        QMessageBox.information(self, "Resultado", f"{valor:.2f} {de} = {resultado:.2f} {para}")

    def pegar_taxa_api(self, de, para):
        try:
            url = f"https://economia.awesomeapi.com.br/last/{de}-{para}"
            resposta = requests.get(url) # requests.get() = Requisição à API externa
            if resposta.status_code == 200:
                dados = resposta.json()
                return dados[f"{de}{para}"]["bid"]
        except Exception as erro:
            print("Erro ao consultar API:", erro)
        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Conversor()
    janela.show()
    app.exec()
