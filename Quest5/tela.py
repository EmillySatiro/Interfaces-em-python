import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
    QLineEdit,
    QStackedWidget,
    QLabel,
    QComboBox,
)

# Importando as classes do arquivo carrinho.py
from back import Item, CarrinhoDeCompras, GerenciadorCupons

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.carrinho = CarrinhoDeCompras()
        self.gerenciador_cupons = GerenciadorCupons()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sistema de Compras")
        self.setGeometry(100, 100, 400, 400)

        # Definindo o estilo da janela
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                color: #333;
            }
            QPushButton {
                background-color: #003366;
                color: white;
                border: none;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005599;
            }
            QLineEdit {
                border: 2px solid #003366;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QLabel {
                font-size: 16px;
            }
            QComboBox {
                border: 2px solid #003366;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
        """)

        self.layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()

        # Página inicial
        self.pagina_inicial = QWidget()
        self.layout_inicial = QVBoxLayout()
        self.botao_adicionar_carrinho = QPushButton("Adicionar ao Carrinho", self)
        self.botao_cadastrar_cupons = QPushButton("Cadastrar Cupons", self)
        self.botao_ver_carrinho = QPushButton("Ver Carrinho", self)
        self.botao_sair = QPushButton("Sair", self)

        self.botao_adicionar_carrinho.clicked.connect(self.mostrar_adicionar_ao_carrinho)
        self.botao_cadastrar_cupons.clicked.connect(self.mostrar_cadastrar_cupons)
        self.botao_ver_carrinho.clicked.connect(self.mostrar_carrinho)
        self.botao_sair.clicked.connect(self.fechar_aplicacao)

        self.layout_inicial.addWidget(self.botao_adicionar_carrinho)
        self.layout_inicial.addWidget(self.botao_cadastrar_cupons)
        self.layout_inicial.addWidget(self.botao_ver_carrinho)
        self.layout_inicial.addWidget(self.botao_sair)

        self.pagina_inicial.setLayout(self.layout_inicial)
        self.stacked_widget.addWidget(self.pagina_inicial)

        # Página de adicionar ao carrinho
        self.pagina_adicionar_ao_carrinho = QWidget()
        self.layout_adicionar_ao_carrinho = QVBoxLayout()
        self.item_carrinho_nome = QLineEdit(self)
        self.item_carrinho_preco = QLineEdit(self)
        self.item_carrinho_quantidade = QLineEdit(self)
        self.item_carrinho_nome.setPlaceholderText("Nome do item")
        self.item_carrinho_preco.setPlaceholderText("Preço do item (R$)")
        self.item_carrinho_quantidade.setPlaceholderText("Quantidade")

        self.botao_adicionar_item = QPushButton("Adicionar Item ao Carrinho", self)
        self.botao_adicionar_item.clicked.connect(self.adicionar_item_ao_carrinho)

        self.label_total = QLabel("Total do Carrinho: R$0.00", self)
        self.botao_voltar_carrinho = QPushButton("Voltar", self)
        self.botao_voltar_carrinho.clicked.connect(self.voltar_para_inicial)

        self.layout_adicionar_ao_carrinho.addWidget(self.item_carrinho_nome)
        self.layout_adicionar_ao_carrinho.addWidget(self.item_carrinho_preco)
        self.layout_adicionar_ao_carrinho.addWidget(self.item_carrinho_quantidade)
        self.layout_adicionar_ao_carrinho.addWidget(self.botao_adicionar_item)
        self.layout_adicionar_ao_carrinho.addWidget(self.label_total)
        self.layout_adicionar_ao_carrinho.addWidget(self.botao_voltar_carrinho)

        self.pagina_adicionar_ao_carrinho.setLayout(self.layout_adicionar_ao_carrinho)
        self.stacked_widget.addWidget(self.pagina_adicionar_ao_carrinho)

        # Página de cadastrar cupons
        self.pagina_cadastrar_cupons = QWidget()
        self.layout_cadastrar_cupons = QVBoxLayout()
        self.cupom_codigo = QLineEdit(self)
        self.cupom_desconto = QLineEdit(self)
        self.cupom_codigo.setPlaceholderText("Código do cupom")
        self.cupom_desconto.setPlaceholderText("Valor do desconto (%)")

        self.botao_salvar_cupom = QPushButton("Salvar Cupom", self)
        self.botao_salvar_cupom.clicked.connect(self.salvar_cupom)

        self.botao_voltar_cupons = QPushButton("Voltar", self)
        self.botao_voltar_cupons.clicked.connect(self.voltar_para_inicial)

        self.layout_cadastrar_cupons.addWidget(self.cupom_codigo)
        self.layout_cadastrar_cupons.addWidget(self.cupom_desconto)
        self.layout_cadastrar_cupons.addWidget(self.botao_salvar_cupom)
        self.layout_cadastrar_cupons.addWidget(self.botao_voltar_cupons)

        self.pagina_cadastrar_cupons.setLayout(self.layout_cadastrar_cupons)
        self.stacked_widget.addWidget(self.pagina_cadastrar_cupons)

        # Página de carrinho com desconto
        self.pagina_carrinho = QWidget()
        self.layout_carrinho = QVBoxLayout()

        self.botao_aplicar_desconto_automatico = QPushButton("Aplicar Cupom", self)
        self.botao_aplicar_desconto_automatico.clicked.connect(self.aplicar_desconto_automatico)

        self.combo_cupons = QComboBox(self)
        self.combo_cupons.addItem("Selecionar Cupom")
        self.carregar_cupons()  # Carregar cupons disponíveis

        self.label_total_com_desconto = QLabel("Total com Desconto: R$0.00", self)
        self.botao_finalizar_compra = QPushButton("Finalizar Compra", self)
        self.botao_finalizar_compra.clicked.connect(self.finalizar_compra)
        self.botao_voltar_carrinho_page = QPushButton("Voltar", self)
        self.botao_voltar_carrinho_page.clicked.connect(self.voltar_para_inicial)

        self.layout_carrinho.addWidget(self.combo_cupons)
        self.layout_carrinho.addWidget(self.botao_aplicar_desconto_automatico)
        self.layout_carrinho.addWidget(self.label_total_com_desconto)
        self.layout_carrinho.addWidget(self.botao_finalizar_compra)
        self.layout_carrinho.addWidget(self.botao_voltar_carrinho_page)

        self.pagina_carrinho.setLayout(self.layout_carrinho)
        self.stacked_widget.addWidget(self.pagina_carrinho)

        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

    def mostrar_adicionar_ao_carrinho(self):
        self.stacked_widget.setCurrentIndex(1)  # 1 é o índice da página de adicionar ao carrinho
        self.label_total.setText("Total do Carrinho: R$0.00")  # Resetando o total ao mudar de página
        self.item_carrinho_nome.clear()  # Limpando os campos de entrada
        self.item_carrinho_preco.clear()
        self.item_carrinho_quantidade.clear()

    def mostrar_cadastrar_cupons(self):
        self.stacked_widget.setCurrentIndex(2)  # 2 é o índice da página de cadastrar cupons

    def mostrar_carrinho(self):
        self.stacked_widget.setCurrentIndex(3)  # 3 é o índice da página do carrinho
        self.atualizar_total_carrinho()  # Atualiza o total ao mostrar a página do carrinho

    def voltar_para_inicial(self):
        self.stacked_widget.setCurrentIndex(0)  # 0 é o índice da página inicial

    def fechar_aplicacao(self):
        QApplication.quit()

    def adicionar_item_ao_carrinho(self):
        nome = self.item_carrinho_nome.text()
        try:
            preco = float(self.item_carrinho_preco.text().replace(',', '.'))  # Suporte para vírgula decimal
            quantidade = int(self.item_carrinho_quantidade.text())
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")

            item = Item(nome, preco, quantidade)  
            self.carrinho.adicionar_item(item)

            total = self.calcular_total_carrinho()
            self.label_total.setText(f"Total do Carrinho: R${total:.2f}")

            self.item_carrinho_nome.clear()
            self.item_carrinho_preco.clear()
            self.item_carrinho_quantidade.clear()

            QMessageBox.information(self, "Sucesso", "Item adicionado ao carrinho.")
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))

    def calcular_total_carrinho(self):
        total = sum(item.preco * item.quantidade for item in self.carrinho.itens)
        return total

    def carregar_cupons(self):
        self.combo_cupons.clear()
        self.combo_cupons.addItem("Selecionar Cupom")
        for cupom in self.gerenciador_cupons.cupons:
            self.combo_cupons.addItem(cupom.codigo)

    def salvar_cupom(self):
        codigo = self.cupom_codigo.text()
        try:
            desconto = float(self.cupom_desconto.text().replace(',', '.'))  # Suporte para vírgula decimal
            if desconto < 0 or desconto > 100:
                raise ValueError("O desconto deve ser entre 0 e 100.")

            self.gerenciador_cupons.adicionar_cupom(codigo, desconto)
            self.cupom_codigo.clear()
            self.cupom_desconto.clear()
            QMessageBox.information(self, "Sucesso", "Cupom salvo com sucesso.")
            self.carregar_cupons()  # Recarregar cupons disponíveis após salvar um novo
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))

    def aplicar_desconto_automatico(self):
        total = self.calcular_total_carrinho()
        cupom_selecionado = self.combo_cupons.currentText()

        if cupom_selecionado != "Selecionar Cupom":
            desconto = self.gerenciador_cupons.obter_desconto(cupom_selecionado)
            total *= (1 - desconto / 100)

        self.label_total_com_desconto.setText(f"Total com Desconto: R${total:.2f}")

    def atualizar_total_carrinho(self):
        total = self.calcular_total_carrinho()
        self.label_total_com_desconto.setText(f"Total com Desconto: R${total:.2f}")  # Atualiza o total com desconto ao mostrar a página

    def finalizar_compra(self):
        total = self.label_total_com_desconto.text().split("R$")[1]
        QMessageBox.information(self, "Compra Finalizada", f"Total da compra: R${total}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
