import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                             QWidget, QVBoxLayout, 
                             QLabel, QListWidget, 
                             QPushButton, QMessageBox, 
                             QLineEdit, QDateEdit, 
                             QHBoxLayout)
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta
from back import EstoqueMedicamentos

estoque = []  

class TelaInicial(QMainWindow):
    """   
    Classe TelaInicial
    Esta classe representa a tela inicial do Sistema de Estoque de Medicamentos. 
    Ela herda de QMainWindow e configura a interface gráfica inicial do sistema.
    Métodos:
        __init__(): Inicializa a tela inicial, configurando o título, geometria e estilo.
        initUI(): Configura o layout principal da tela inicial, incluindo os widgets e seus estilos.
        style_button(): Retorna uma string com o estilo CSS para os botões.
        abrir_tela_cadastro(): Abre a tela de cadastro de medicamentos e fecha a tela inicial.
        abrir_tela_reposicao(): Abre a tela de reposição de medicamentos e fecha a tela inicial.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Estoque de Medicamentos")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f9f9f9;")  

        self.initUI()

    def initUI(self):
        # Configuração do layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Label de título
        self.title_label = QLabel("Sistema de Estoque de Medicamentos")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #d55d98;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Botões
        self.cadastrar_btn = QPushButton("Cadastrar Medicamento")
        self.cadastrar_btn.setStyleSheet(self.style_button())
        self.cadastrar_btn.clicked.connect(self.abrir_tela_cadastro)
        self.layout.addWidget(self.cadastrar_btn)

        self.reposicao_btn = QPushButton("Ver Medicamentos para Reposição")
        self.reposicao_btn.setStyleSheet(self.style_button())
        self.reposicao_btn.clicked.connect(self.abrir_tela_reposicao)
        self.layout.addWidget(self.reposicao_btn)

        self.sair_btn = QPushButton("Sair")
        self.sair_btn.setStyleSheet(self.style_button())
        self.sair_btn.clicked.connect(self.close)
        self.layout.addWidget(self.sair_btn)

        self.layout.setAlignment(Qt.AlignCenter)
        self.central_widget.setLayout(self.layout)

    def style_button(self):
        return """
            QPushButton {
                background-color: #d55d98; 
                border: 2px solid #a0526e; 
                border-radius: 10px; 
                font-size: 18px; 
                color: white;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #a0526e;
            }
        """

    def abrir_tela_cadastro(self):
        self.tela_cadastro = TelaCadastro()
        self.tela_cadastro.show()
        self.close()  # Fecha a tela inicial

    def abrir_tela_reposicao(self):
        self.tela_reposicao = TelaReposicao()
        self.tela_reposicao.show()
        self.close()  # Fecha a tela inicial

class TelaCadastro(QMainWindow):
    """
    Classe TelaCadastro
    Esta classe representa uma janela de cadastro de medicamentos, permitindo ao usuário inserir informações sobre novos medicamentos e adicioná-los ao estoque.
    Métodos:
        __init__(): Inicializa a janela de cadastro, configurando o título, dimensões e estilo.
        initUI(): Configura a interface do usuário, incluindo campos de entrada e botões.
        style_button(): Retorna uma string com o estilo CSS para os botões.
        adicionar_medicamento(): Adiciona um novo medicamento ao estoque e atualiza a lista.
        voltar(): Retorna à tela inicial, fechando a tela de cadastro atual.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastrar Medicamento")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f9f9f9;")  

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

      
        self.title_label = QLabel("Cadastrar Novo Medicamento")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #d55d98;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Campos para adicionar novo medicamento
        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Nome do medicamento")
        self.layout.addWidget(self.nome_input)

        self.quantidade_input = QLineEdit(self)
        self.quantidade_input.setPlaceholderText("Quantidade")
        self.layout.addWidget(self.quantidade_input)

        self.data_vencimento_input = QDateEdit(self)
        self.data_vencimento_input.setDisplayFormat("dd/MM/yyyy")
        self.data_vencimento_input.setCalendarPopup(True)
        self.layout.addWidget(self.data_vencimento_input)

        # Botão para adicionar medicamento
        self.adicionar_btn = QPushButton("Adicionar Medicamento")
        self.adicionar_btn.setStyleSheet(self.style_button())
        self.adicionar_btn.clicked.connect(self.adicionar_medicamento)
        self.layout.addWidget(self.adicionar_btn)

        self.voltar_btn = QPushButton("Voltar")
        self.voltar_btn.setStyleSheet(self.style_button())
        self.voltar_btn.clicked.connect(self.voltar)
        self.layout.addWidget(self.voltar_btn)

        self.central_widget.setLayout(self.layout)

    def style_button(self):
        return """
            QPushButton {
                background-color: #d55d98; 
                border: 2px solid #a0526e; 
                border-radius: 10px; 
                font-size: 18px; 
                color: white;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #a0526e;
            }
        """

    def adicionar_medicamento(self):
        """Adiciona um novo medicamento ao estoque e atualiza a lista."""
        nome = self.nome_input.text()
        quantidade = self.quantidade_input.text()
        data_vencimento = self.data_vencimento_input.date().toPyDate()

        if nome and quantidade.isdigit() and int(quantidade) > 0:
            novo_medicamento = EstoqueMedicamentos(nome, int(quantidade), data_vencimento)
            estoque.append(novo_medicamento)
            QMessageBox.information(self, "Sucesso", "Medicamento adicionado com sucesso!")
            self.nome_input.clear()
            self.quantidade_input.clear()
            self.data_vencimento_input.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos corretamente.")

    def voltar(self):
        self.tela_inicial = TelaInicial()
        self.tela_inicial.show()
        self.close()  

class TelaReposicao(QMainWindow):
    """
    Classe TelaReposicao
    Esta classe representa uma janela de interface gráfica para gerenciar a reposição de medicamentos. 
    Ela permite visualizar, adicionar e remover quantidades de medicamentos em estoque.
    Métodos:
        __init__(): Inicializa a janela principal e define suas propriedades.
        initUI(): Configura os elementos da interface gráfica, como labels, botões e campos de entrada.
        style_button(): Retorna uma string de estilo CSS para os botões.
        atualizar_lista(): Atualiza a lista de medicamentos exibida na interface.
        adicionar_quantidade(): Adiciona a quantidade especificada ao medicamento escolhido.
        remover_quantidade(): Remove a quantidade especificada do medicamento escolhido.
        voltar(): Retorna à tela inicial e fecha a tela de reposição.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Medicamentos para Reposição")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f9f9f9;")  

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Label de título
        self.title_label = QLabel("Medicamentos para Reposição")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #d55d98;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Lista para exibir medicamentos
        self.lista_medicamentos = QListWidget()
        self.layout.addWidget(self.lista_medicamentos)

        # Campos para adicionar ou remover quantidade
        self.medicamento_input = QLineEdit(self)
        self.medicamento_input.setPlaceholderText("Nome do medicamento")
        self.layout.addWidget(self.medicamento_input)

        self.adicionar_quantidade_input = QLineEdit(self)
        self.adicionar_quantidade_input.setPlaceholderText("Quantidade a adicionar")
        self.layout.addWidget(self.adicionar_quantidade_input)

        self.adicionar_btn = QPushButton("Adicionar Quantidade")
        self.adicionar_btn.setStyleSheet(self.style_button())
        self.adicionar_btn.clicked.connect(self.adicionar_quantidade)
        self.layout.addWidget(self.adicionar_btn)

        self.remover_quantidade_input = QLineEdit(self)
        self.remover_quantidade_input.setPlaceholderText("Quantidade a remover")
        self.layout.addWidget(self.remover_quantidade_input)

        self.remover_btn = QPushButton("Remover Quantidade")
        self.remover_btn.setStyleSheet(self.style_button())
        self.remover_btn.clicked.connect(self.remover_quantidade)
        self.layout.addWidget(self.remover_btn)

        self.voltar_btn = QPushButton("Voltar")
        self.voltar_btn.setStyleSheet(self.style_button())
        self.voltar_btn.clicked.connect(self.voltar)
        self.layout.addWidget(self.voltar_btn)

        self.central_widget.setLayout(self.layout)

        self.atualizar_lista()

    def style_button(self):
        return """
            QPushButton {
                background-color: #d55d98; 
                border: 2px solid #a0526e; 
                border-radius: 10px; 
                font-size: 18px; 
                color: white;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #a0526e;
            }
        """

    def atualizar_lista(self):
        """Atualiza a lista de medicamentos na interface."""
        self.lista_medicamentos.clear()
        for medicamento in estoque:
            if medicamento.verificar_vencimento():
                info = f"{medicamento.get_nome()} - Qtd: {medicamento.get_quantidade()} - Venc: {medicamento.get_data_vencimento()}"
                self.lista_medicamentos.addItem(info)

    def adicionar_quantidade(self):
        """Adiciona a quantidade especificada ao medicamento escolhido."""
        nome = self.medicamento_input.text()
        quantidade = self.adicionar_quantidade_input.text()

        if nome and quantidade.isdigit() and int(quantidade) > 0:
            for medicamento in estoque:
                if medicamento.get_nome() == nome:
                    medicamento.adicionar_quantidade(int(quantidade))
                    QMessageBox.information(self, "Sucesso", "Quantidade adicionada com sucesso!")
                    self.atualizar_lista()
                    self.medicamento_input.clear()
                    self.adicionar_quantidade_input.clear()
                    return

            QMessageBox.warning(self, "Erro", "Medicamento não encontrado.")
        else:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos corretamente.")

    def remover_quantidade(self):
        """Remove a quantidade especificada do medicamento escolhido."""
        nome = self.medicamento_input.text()
        quantidade = self.remover_quantidade_input.text()

        if nome and quantidade.isdigit() and int(quantidade) > 0:
            for medicamento in estoque:
                if medicamento.get_nome() == nome:
                    if medicamento.get_quantidade() >= int(quantidade):
                        medicamento.remover_quantidade(int(quantidade))
                        QMessageBox.information(self, "Sucesso", "Quantidade removida com sucesso!")
                        self.atualizar_lista()
                        self.medicamento_input.clear()
                        self.remover_quantidade_input.clear()
                        return
                    else:
                        QMessageBox.warning(self, "Erro", "Quantidade insuficiente para remoção.")

            QMessageBox.warning(self, "Erro", "Medicamento não encontrado.")
        else:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos corretamente.")

    def voltar(self):
        self.tela_inicial = TelaInicial()
        self.tela_inicial.show()
        self.close()  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TelaInicial()
    janela.show()
    sys.exit(app.exec_())
