import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QMessageBox, QComboBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from back import BibliotecaBicicletas  

class TelaInicial(QWidget):
    """
    TelaInicial é uma classe que representa a tela inicial do sistema de aluguel de bicicletas.
    Atributos:
        biblioteca (Biblioteca): Instância da biblioteca que gerencia os dados do sistema.
        label_titulo (QLabel): Rótulo que exibe o título da aplicação.
        botao_cadastrar (QPushButton): Botão para abrir a tela de cadastro de bicicletas.
        botao_alugar (QPushButton): Botão para abrir a tela de aluguel de bicicletas.
        botao_devolver (QPushButton): Botão para abrir a tela de devolução de bicicletas.
        botao_sair (QPushButton): Botão para sair da aplicação.
    Métodos:
        __init__(biblioteca):
            Inicializa a tela inicial com os componentes e layout necessários.
        criar_botao(texto, funcao):
            Cria e retorna um botão configurado com o texto e função de clique fornecidos.
        abrir_tela_cadastro():
            Abre a tela de cadastro de bicicletas e fecha a tela atual.
        abrir_tela_aluguel():
            Abre a tela de aluguel de bicicletas e fecha a tela atual.
        abrir_tela_devolucao():
            Abre a tela de devolução de bicicletas e fecha a tela atual.
        sair_aplicacao():
            Exibe uma mensagem de confirmação para sair da aplicação e, se confirmado, encerra a aplicação.
    """
    def __init__(self, biblioteca):
        super().__init__()
        self.biblioteca = biblioteca
        self.setWindowTitle("Sistema de Aluguel de Bicicletas")
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet("background-color:#007C92;")

        layout_principal = QVBoxLayout()
        layout_principal.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.label_titulo = QLabel("Sistema de Aluguel de Bicicletas")
        self.label_titulo.setFont(QFont("Arial", 16, QFont.Bold))
        self.label_titulo.setStyleSheet("color: #000080;")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(self.label_titulo)

        self.botao_cadastrar = self.criar_botao("Cadastrar Bicicleta", self.abrir_tela_cadastro)
        self.botao_alugar = self.criar_botao("Alugar Bicicleta", self.abrir_tela_aluguel)
        self.botao_devolver = self.criar_botao("Devolver Bicicleta", self.abrir_tela_devolucao)

        layout_principal.addWidget(self.botao_cadastrar)
        layout_principal.addWidget(self.botao_alugar)
        layout_principal.addWidget(self.botao_devolver)
        layout_principal.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.botao_sair = self.criar_botao("Sair", self.sair_aplicacao)
        layout_principal.addWidget(self.botao_sair)

        self.setLayout(layout_principal)

    def criar_botao(self, texto, funcao):
        botao = QPushButton(texto)
        botao.setFont(QFont("Arial", 12))
        botao.setStyleSheet("color: #000000; border: 2px solid #000080; border-radius: 8px; padding: 8px;")
        botao.clicked.connect(funcao)
        return botao

    def abrir_tela_cadastro(self):
        self.cadastro = TelaCadastro(self.biblioteca, self)
        self.cadastro.show()
        self.close()

    def abrir_tela_aluguel(self):
        self.aluguel = TelaAluguel(self.biblioteca, self)
        self.aluguel.show()
        self.close()

    def abrir_tela_devolucao(self):
        self.devolucao = TelaDevolucao(self.biblioteca, self)
        self.devolucao.show()
        self.close()

    def sair_aplicacao(self):
        resposta = QMessageBox.question(self, "Sair", "Deseja realmente sair?", QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            QApplication.instance().quit()

class TelaCadastro(QWidget):
    """
    TelaCadastro é uma classe que representa uma interface gráfica para o cadastro de bicicletas.
    Atributos:
    ----------
    biblioteca : Biblioteca
        Instância da classe Biblioteca que gerencia os dados das bicicletas.
    tela_inicial : QWidget
        Instância da tela inicial para retornar após o cadastro.
    Métodos:
    --------
    __init__(self, biblioteca, tela_inicial):
        Inicializa a interface de cadastro de bicicletas.
    cadastrar_bicicleta(self):
        Realiza o cadastro de uma bicicleta com os dados fornecidos pelo usuário.
    voltar(self):
        Retorna à tela inicial e fecha a tela de cadastro.
    """
    def __init__(self, biblioteca, tela_inicial):
        super().__init__()
        self.biblioteca = biblioteca
        self.tela_inicial = tela_inicial
        self.setWindowTitle("Cadastro de Bicicleta")
        self.setGeometry(200, 200, 400, 200)
        self.setStyleSheet("background-color: #007C92;")

        layout = QVBoxLayout()
        self.input_modelo = QLineEdit()
        self.input_modelo.setPlaceholderText("Modelo da Bicicleta")
        self.input_tarifa = QLineEdit()
        self.input_tarifa.setPlaceholderText("Tarifa por Hora")
        self.botao_confirmar = QPushButton("Confirmar Cadastro")
        self.botao_confirmar.clicked.connect(self.cadastrar_bicicleta)
        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.clicked.connect(self.voltar)

        layout.addWidget(self.input_modelo)
        layout.addWidget(self.input_tarifa)
        layout.addWidget(self.botao_confirmar)
        layout.addWidget(self.botao_voltar)
        self.setLayout(layout)

    def cadastrar_bicicleta(self):
        modelo = self.input_modelo.text()
        tarifa = self.input_tarifa.text()
        if modelo and tarifa.isdigit():
            self.biblioteca.cadastrar_bicicleta(modelo, float(tarifa))
            QMessageBox.information(self, "Cadastro", "Bicicleta cadastrada com sucesso!")
            self.voltar()
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos corretamente.")

    def voltar(self):
        self.tela_inicial.show()
        self.close()

class TelaAluguel(QWidget):
    """
    TelaAluguel é uma classe que representa a interface gráfica para alugar bicicletas.
    Atributos:
        biblioteca (Biblioteca): Instância da classe Biblioteca que gerencia as bicicletas.
        tela_inicial (QWidget): Instância da tela inicial para retornar após o aluguel.
    Métodos:
        __init__(biblioteca, tela_inicial):
            Inicializa a interface de aluguel de bicicletas.
        atualizar_lista_bicicletas():
            Atualiza a lista de bicicletas disponíveis no combo box.
        alugar_bicicleta():
            Realiza o processo de aluguel de uma bicicleta, calculando o custo e exibindo uma mensagem de confirmação.
        voltar():
            Retorna para a tela inicial e fecha a tela de aluguel.
    """
    def __init__(self, biblioteca, tela_inicial):
        super().__init__()
        self.biblioteca = biblioteca
        self.tela_inicial = tela_inicial
        self.setWindowTitle("Alugar Bicicleta")
        self.setGeometry(200, 200, 400, 200)
        self.setStyleSheet("background-color: #007C92;")

        layout = QVBoxLayout()
        self.combo_bicicletas = QComboBox()
        self.atualizar_lista_bicicletas()
        self.input_horas = QLineEdit()
        self.input_horas.setPlaceholderText("Número de Horas")
        self.botao_confirmar = QPushButton("Confirmar Aluguel")
        self.botao_confirmar.clicked.connect(self.alugar_bicicleta)
        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.clicked.connect(self.voltar)

        layout.addWidget(self.combo_bicicletas)
        layout.addWidget(self.input_horas)
        layout.addWidget(self.botao_confirmar)
        layout.addWidget(self.botao_voltar)
        self.setLayout(layout)

    def atualizar_lista_bicicletas(self):
        self.combo_bicicletas.clear()
        for bicicleta in self.biblioteca.listar_disponiveis():
            self.combo_bicicletas.addItem(bicicleta.modelo, bicicleta)

    def alugar_bicicleta(self):
        bicicleta = self.combo_bicicletas.currentData()
        horas = self.input_horas.text()
        if bicicleta and horas.isdigit():
            custo = bicicleta.tarifa_por_hora * int(horas)
            bicicleta.alugar()
            QMessageBox.information(self, "Aluguel", f"Aluguel confirmado! Total: R${custo:.2f}")
            self.voltar()
        else:
            QMessageBox.warning(self, "Erro", "Selecione uma bicicleta e informe um número válido de horas.")

    def voltar(self):
        self.tela_inicial.show()
        self.close()

class TelaDevolucao(QWidget):
    """
    TelaDevolucao é uma classe que representa a interface gráfica para a devolução de bicicletas.
    Atributos:
    ----------
    biblioteca : Biblioteca
        Instância da classe Biblioteca que contém as bicicletas alugadas.
    tela_inicial : QWidget
        Instância da tela inicial para retornar após a devolução.
    Métodos:
    --------
    __init__(biblioteca, tela_inicial):
        Inicializa a interface de devolução de bicicletas.
    atualizar_lista_bicicletas():
        Atualiza a lista de bicicletas alugadas no combo box.
    devolver_bicicleta():
        Realiza a devolução da bicicleta selecionada.
    voltar():
        Retorna para a tela inicial.
    """
    def __init__(self, biblioteca, tela_inicial):
        super().__init__()
        self.biblioteca = biblioteca
        self.tela_inicial = tela_inicial
        self.setWindowTitle("Devolver Bicicleta")
        self.setGeometry(200, 200, 400, 200)
        self.setStyleSheet("background-color: #007C92;")

        layout = QVBoxLayout()
        self.combo_bicicletas = QComboBox()
        self.atualizar_lista_bicicletas()
        self.botao_confirmar = QPushButton("Confirmar Devolução")
        self.botao_confirmar.clicked.connect(self.devolver_bicicleta)
        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.clicked.connect(self.voltar)

        layout.addWidget(self.combo_bicicletas)
        layout.addWidget(self.botao_confirmar)
        layout.addWidget(self.botao_voltar)
        self.setLayout(layout)

    def atualizar_lista_bicicletas(self):
        self.combo_bicicletas.clear()
        for bicicleta in self.biblioteca.listar_alugadas():
            self.combo_bicicletas.addItem(bicicleta.modelo, bicicleta)

    def devolver_bicicleta(self):
        bicicleta = self.combo_bicicletas.currentData()
        if bicicleta:
            bicicleta.devolver()
            QMessageBox.information(self, "Devolução", "Bicicleta devolvida com sucesso!")
            self.voltar()
        else:
            QMessageBox.warning(self, "Erro", "Selecione uma bicicleta alugada para devolver.")

    def voltar(self):
        self.tela_inicial.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    biblioteca = BibliotecaBicicletas()
    tela_inicial = TelaInicial(biblioteca)
    tela_inicial.show()
    sys.exit(app.exec_())
