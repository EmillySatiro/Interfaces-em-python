from back import AulaDeIngles, AulaDeEspanhol
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox, QMainWindow

class MainWindow(QMainWindow):
    """
    Classe MainWindow que representa a janela principal da aplicação.
    Métodos:
        __init__(): Inicializa a janela principal, define o título, geometria e layout.
        get_button_style(): Retorna o estilo CSS para os botões.
        selecionar_dificuldade(idioma): Abre uma nova janela para seleção de dificuldade com base no idioma selecionado.
        sair(): Exibe uma mensagem de confirmação para sair da aplicação.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Seleção de Aulas')
        self.setGeometry(100, 100, 400, 300)

        # Dicionário para manter o registro de aulas e palavras concluídas
        self.aulas_concluidas = {
            'Inglês': 0,
            'Espanhol': 0
        }

        layout = QVBoxLayout()

        # Frase inicial
        self.label_frase = QLabel("Escolha sua aula:", self)
        self.label_frase.setStyleSheet("font-size: 20px; color: #B22222;")  # Aumenta o tamanho da fonte e muda a cor
        layout.addWidget(self.label_frase)

        # Botão para Aula de Inglês
        self.botao_ingles = QPushButton("Aula de Inglês", self)
        self.botao_ingles.setStyleSheet(self.get_button_style())
        self.botao_ingles.clicked.connect(lambda: self.selecionar_dificuldade("Inglês"))
        layout.addWidget(self.botao_ingles)

        # Botão para Aula de Espanhol
        self.botao_espanhol = QPushButton("Aula de Espanhol", self)
        self.botao_espanhol.setStyleSheet(self.get_button_style())
        self.botao_espanhol.clicked.connect(lambda: self.selecionar_dificuldade("Espanhol"))
        layout.addWidget(self.botao_espanhol)

        # Botão de Sair
        self.botao_sair = QPushButton("Sair", self)
        self.botao_sair.setStyleSheet(self.get_button_style())
        self.botao_sair.clicked.connect(self.sair)
        layout.addWidget(self.botao_sair)

        # Widget principal da janela
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Define o estilo da janela
        self.setStyleSheet("background-color: white;")  # Fundo branco

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #B22222;
                color: #8B0000;
                font-size: 18px;
                border-radius: 15px;  /* Ar#B22222ondar os cantos */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: dark#B22222;  /* Cor ao passar o mouse */
            }
        """

    def selecionar_dificuldade(self, idioma):
        # Nova janela para seleção de dificuldade
        self.dificuldade_window = DificuldadeWindow(idioma, self.aulas_concluidas)
        self.dificuldade_window.show()
        self.close()

    def sair(self):
        reply = QMessageBox.question(self, 'Sair', "Você deseja sair?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()


class DificuldadeWindow(QMainWindow):
    """
    Janela de seleção de nível de dificuldade para aulas de idiomas.
    Atributos:
        idioma (str): Idioma selecionado pelo usuário.
        aulas_concluidas (int): Número de aulas concluídas pelo usuário.
        label_dificuldade (QLabel): Rótulo que exibe a mensagem de seleção de dificuldade.
        botao_fácil (QPushButton): Botão para selecionar o nível de dificuldade "Fácil".
        botao_médio (QPushButton): Botão para selecionar o nível de dificuldade "Médio".
        botao_difícil (QPushButton): Botão para selecionar o nível de dificuldade "Difícil".
        aula_window (QMainWindow): Janela da aula iniciada.
    Métodos:
        __init__(idioma, aulas_concluidas):
            Inicializa a janela de seleção de nível de dificuldade.
        get_button_style():
            Retorna o estilo CSS para os botões de seleção de dificuldade.
        iniciar_aula(dificuldade):
            Inicia a aula com o nível de dificuldade selecionado.
    """
    def __init__(self, idioma, aulas_concluidas):
        super().__init__()

        self.idioma = idioma
        self.aulas_concluidas = aulas_concluidas
        self.setWindowTitle('Seleção de Nível de Dificuldade')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_dificuldade = QLabel(f"Escolha o nível de dificuldade para {idioma}:", self)
        self.label_dificuldade.setStyleSheet("font-size: 20px; color: #B22222;")
        layout.addWidget(self.label_dificuldade)

        # Botões para Níveis de Dificuldade
        self.botao_fácil = QPushButton("Fácil", self)
        self.botao_fácil.setStyleSheet(self.get_button_style())
        self.botao_fácil.clicked.connect(lambda: self.iniciar_aula("Fácil"))
        layout.addWidget(self.botao_fácil)

        self.botao_médio = QPushButton("Médio", self)
        self.botao_médio.setStyleSheet(self.get_button_style())
        self.botao_médio.clicked.connect(lambda: self.iniciar_aula("Médio"))
        layout.addWidget(self.botao_médio)

        self.botao_difícil = QPushButton("Difícil", self)
        self.botao_difícil.setStyleSheet(self.get_button_style())
        self.botao_difícil.clicked.connect(lambda: self.iniciar_aula("Difícil"))
        layout.addWidget(self.botao_difícil)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("background-color: white;")

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #B22222;
                color: #8B0000;
                font-size: 18px;
                border-radius: 15px;  /* Ar#B22222ondar os cantos */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: dark#B22222;  /* Cor ao passar o mouse */
            }
        """

    def iniciar_aula(self, dificuldade):
        if self.idioma == "Inglês":
            self.aula_window = AulaWindow(AulaDeIngles("Inglês Básico", dificuldade), self.aulas_concluidas, self.idioma)
        else:
            self.aula_window = AulaWindow(AulaDeEspanhol("Espanhol Básico", dificuldade), self.aulas_concluidas, self.idioma)

        self.aula_window.show()
        self.close()


class AulaWindow(QMainWindow):
    """
    Classe que representa a janela de uma aula.
    Args:
        aula (Aula): Objeto que contém as informações da aula.
        aulas_concluidas (dict): Dicionário que armazena o progresso das aulas concluídas por idioma.
        idioma (str): Idioma da aula.
    Atributos:
        aula (Aula): Armazena o objeto da aula.
        aulas_concluidas (dict): Armazena o progresso das aulas concluídas por idioma.
        idioma (str): Armazena o idioma da aula.
        label_aula (QLabel): Rótulo que exibe o título e nível de dificuldade da aula.
        label_progresso (QLabel): Rótulo que exibe o progresso das aulas concluídas.
        label_palavra (QLabel): Rótulo que exibe a palavra atual ou mensagem de conclusão.
        botao_concluir (QPushButton): Botão para concluir a aula.
        palavra_atual (str): Armazena a palavra atual da aula.
    Métodos:
        get_button_style(): Retorna o estilo CSS para o botão de concluir aula.
        concluir_aula(): Atualiza o progresso das aulas concluídas e exibe mensagens de conclusão.
        voltar_para_tela_principal(): Retorna para a tela principal da aplicação.
    """
    def __init__(self, aula, aulas_concluidas, idioma):
        super().__init__()

        self.aula = aula
        self.aulas_concluidas = aulas_concluidas
        self.idioma = idioma
        self.setWindowTitle(f'Aula de {self.aula.get_titulo()} - {self.aula.get_nivel_dificuldade()}')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_aula = QLabel(f"Aula de {self.aula.get_titulo()} - {self.aula.get_nivel_dificuldade()}", self)
        self.label_aula.setStyleSheet("font-size: 20px; color: #B22222;")
        layout.addWidget(self.label_aula)

        # Exibe progresso de aulas concluídas
        total_palavras = len(self.aula.exibir_palavras_chave())
        palavras_concluidas = self.aulas_concluidas[self.idioma]
        self.label_progresso = QLabel(f"Aulas concluídas: {palavras_concluidas}/{total_palavras}", self)
        self.label_progresso.setStyleSheet("font-size: 18px; color: #B22222;")
        layout.addWidget(self.label_progresso)

        self.label_palavra = QLabel("", self)
        layout.addWidget(self.label_palavra)

        if palavras_concluidas < total_palavras:
            # Mostra a próxima palavra da lista
            self.palavra_atual = self.aula.exibir_palavras_chave()[palavras_concluidas]
            self.label_palavra.setText(f"Palavra: {self.palavra_atual}")
        else:
            self.label_palavra.setText("Todas as palavras foram concluídas!")

        # Botão para Concluir Aula
        self.botao_concluir = QPushButton("Concluir Aula", self)
        self.botao_concluir.setStyleSheet(self.get_button_style())
        self.botao_concluir.clicked.connect(self.concluir_aula)
        layout.addWidget(self.botao_concluir)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("background-color: white;")

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #B22222;
                color: #8B0000;
                font-size: 18px;
                border-radius: 15px;  /* Ar#B22222ondar os cantos */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: dark#B22222;  /* Cor ao passar o mouse */
            }
        """

    def concluir_aula(self):
        total_palavras = len(self.aula.exibir_palavras_chave())
        palavras_concluidas = self.aulas_concluidas[self.idioma]

        if palavras_concluidas < total_palavras:
            # Atualiza o número de palavras concluídas
            self.aulas_concluidas[self.idioma] += 1
            QMessageBox.information(self, "Palavra Concluída", f"Você concluiu a palavra: {self.palavra_atual}")
        else:
            QMessageBox.information(self, "Aula Concluída", f"Você concluiu todas as palavras da aula de {self.aula.get_titulo()}!")

        self.voltar_para_tela_principal()

    def voltar_para_tela_principal(self):
        self.main_window = MainWindow()
        self.main_window.aulas_concluidas = self.aulas_concluidas  # Mantém o registro de aulas concluídas
        self.main_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
