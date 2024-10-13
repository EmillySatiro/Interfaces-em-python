import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QWidget, QMessageBox, QVBoxLayout, QLineEdit, QListWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from back import Jogo, BibliotecaJogos  


biblioteca_jogos = BibliotecaJogos()

class MainWindow(QMainWindow):
    """ 
     Classe MainWindow que herda de QMainWindow e representa a janela principal da aplicação.
    Métodos:
        __init__(): Inicializa a janela principal, define o título, geometria, fundo e botão de início.
        ir_para_tela_jogos(): Navega para a tela de jogos, ocultando a janela principal.
        update_background(): Atualiza o fundo da janela principal com uma imagem redimensionada.
        resizeEvent(event): Sobrescreve o evento de redimensionamento para atualizar o fundo.
        botao_style(): Retorna a folha de estilo para o botão de início.
    """
    def __init__(self):
   
        super().__init__()
        self.setWindowTitle("Tela Inicial")
        self.setGeometry(100, 100, 800, 600)
        
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)
        
        self.pixmap = QPixmap("Quest1/imagem/fundo.jpg")
        self.update_background()
        self.background_label.lower()

        self.inicio_button = QPushButton("Início", self)
        self.inicio_button.clicked.connect(self.ir_para_tela_jogos)
        self.inicio_button.setFixedSize(250, 50)
        self.inicio_button.setStyleSheet(self.botao_style())

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.inicio_button)
        button_layout.addStretch()

        container = QWidget(self)
        layout = QVBoxLayout(container)
        layout.addLayout(button_layout)

        self.setCentralWidget(container)

    def ir_para_tela_jogos(self):
        self.tela_jogos = TelaJogos(self.pixmap)
        self.tela_jogos.show()
        self.hide()

    def update_background(self):
        scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def botao_style(self):
        return """
            background-color: #003366;  /* Cor de fundo azul escuro */
            color: white;                /* Cor do texto branco */
            border: 2px solid white;     /* Borda branca de 2 pixels */
            border-radius: 10px;         /* Bordas arredondadas */
            font-size: 20px;             /* Tamanho da fonte */
        """


class TelaJogos(QMainWindow):
    """
      Classe TelaJogos
    Esta classe representa a tela principal do aplicativo de jogos, onde os usuários podem adicionar novos jogos, filtrar jogos existentes e sair da aplicação.
    Atributos:
        background_label (QLabel): Rótulo para exibir o fundo da tela.
        pixmap (QPixmap): Imagem de fundo da tela.
        adicionar_jogo_button (QPushButton): Botão para adicionar um novo jogo.
        filtrar_jogos_button (QPushButton): Botão para filtrar os jogos existentes.
        sair_button (QPushButton): Botão para sair da aplicação.
        cadastro_jogo (CadastroJogo): Tela de cadastro de novo jogo.
        filtrar_jogos_screen (FiltrarJogos): Tela de filtragem de jogos.
    Métodos:
        __init__(pixmap, parent=None): Inicializa a tela principal com a imagem de fundo e configura os botões.
        adicionar_novo_jogo(): Abre a tela de cadastro de novo jogo e esconde a tela principal.
        filtrar_jogos(): Abre a tela de filtragem de jogos e esconde a tela principal.
        sair_aplicacao(): Encerra a aplicação.
        update_background(): Atualiza a imagem de fundo da tela conforme o redimensionamento da janela.
        resizeEvent(event): Sobrescreve o evento de redimensionamento para atualizar a imagem de fundo.
        botao_style(): Retorna a folha de estilo para os botões.
    """
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tela de Jogos")
        self.setGeometry(100, 100, 800, 600)
        
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)
        self.pixmap = pixmap
        self.update_background()
        self.background_label.lower()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        self.adicionar_jogo_button = QPushButton("Adicionar jogo", self)
        self.adicionar_jogo_button.clicked.connect(self.adicionar_novo_jogo)
        self.adicionar_jogo_button.setFixedSize(250, 50)
        self.adicionar_jogo_button.setStyleSheet(self.botao_style())
        layout.addWidget(self.adicionar_jogo_button)

        self.filtrar_jogos_button = QPushButton("Filtrar os jogos", self)
        self.filtrar_jogos_button.clicked.connect(self.filtrar_jogos)
        self.filtrar_jogos_button.setFixedSize(250, 50)
        self.filtrar_jogos_button.setStyleSheet(self.botao_style())
        layout.addWidget(self.filtrar_jogos_button)

        self.sair_button = QPushButton("Sair", self)
        self.sair_button.clicked.connect(self.sair_aplicacao)
        self.sair_button.setFixedSize(250, 50)
        self.sair_button.setStyleSheet(self.botao_style())
        layout.addWidget(self.sair_button)

        container = QWidget(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

    def adicionar_novo_jogo(self):
        self.cadastro_jogo = CadastroJogo(self.pixmap, self)
        self.cadastro_jogo.show()
        self.hide()

    def filtrar_jogos(self):
        self.filtrar_jogos_screen = FiltrarJogos(self.pixmap, self)
        self.filtrar_jogos_screen.show()
        self.hide()

    def sair_aplicacao(self):
        QApplication.quit()

    def update_background(self):
        scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def botao_style(self):
        return """
            background-color: #003366;  /* Cor de fundo azul escuro */
            color: white;                /* Cor do texto branco */
            border: 2px solid white;     /* Borda branca de 2 pixels */
            border-radius: 10px;         /* Bordas arredondadas */
            font-size: 20px;             /* Tamanho da fonte */
        """


class CadastroJogo(QMainWindow):
    """
    Classe CadastroJogo representa uma janela de cadastro de jogos.
    Atributos:
    ----------
    pixmap : QPixmap
        Imagem de fundo da janela.
    background_label : QLabel
        Rótulo para exibir a imagem de fundo.
    nome_jogo_input : QLineEdit
        Campo de entrada para o título do jogo.
    genero_jogo_input : QLineEdit
        Campo de entrada para o gênero do jogo.
    avaliacao_jogo_input : QLineEdit
        Campo de entrada para a avaliação do jogo.
    salvar_jogo_button : QPushButton
        Botão para salvar o jogo.
    voltar_button : QPushButton
        Botão para voltar à tela anterior.
    Métodos:
    --------
    __init__(self, pixmap, parent=None):
        Inicializa a janela de cadastro de jogos.
    initUI(self):
        Configura a interface gráfica da janela de cadastro de jogos.
    salvar_jogo(self):
        Salva o jogo na biblioteca de jogos.
    voltar(self):
        Retorna à tela anterior.
    update_background(self):
        Atualiza a imagem de fundo da janela.
    resizeEvent(self, event):
        Evento de redimensionamento da janela.
    botao_style(self):
        Retorna o estilo CSS para os botões.
    input_style(self):
        Retorna o estilo CSS para os campos de entrada.
"""
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cadastro de Jogo")
        self.setGeometry(100, 100, 800, 600)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)

        self.pixmap = pixmap
        self.update_background()
        self.background_label.lower()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addStretch()

        self.nome_jogo_input = QLineEdit(self)
        self.nome_jogo_input.setPlaceholderText("Título do Jogo")
        self.nome_jogo_input.setStyleSheet(self.input_style())
        self.nome_jogo_input.setFixedWidth(350)
        layout.addWidget(self.nome_jogo_input, alignment=Qt.AlignHCenter)

        self.genero_jogo_input = QLineEdit(self)
        self.genero_jogo_input.setPlaceholderText("Gênero do Jogo")
        self.genero_jogo_input.setStyleSheet(self.input_style())
        self.genero_jogo_input.setFixedWidth(350)
        layout.addWidget(self.genero_jogo_input, alignment=Qt.AlignHCenter)

        self.avaliacao_jogo_input = QLineEdit(self)
        self.avaliacao_jogo_input.setPlaceholderText("Avaliação do Jogo")
        self.avaliacao_jogo_input.setStyleSheet(self.input_style())
        self.avaliacao_jogo_input.setFixedWidth(350)
        layout.addWidget(self.avaliacao_jogo_input, alignment=Qt.AlignHCenter)

        layout.addSpacing(20)

        self.salvar_jogo_button = QPushButton("Salvar Jogo", self)
        self.salvar_jogo_button.clicked.connect(self.salvar_jogo)
        self.salvar_jogo_button.setFixedSize(250, 50)
        self.salvar_jogo_button.setStyleSheet(self.botao_style())
        layout.addWidget(self.salvar_jogo_button, alignment=Qt.AlignHCenter)

        self.voltar_button = QPushButton("Voltar", self)
        self.voltar_button.clicked.connect(self.voltar)
        self.voltar_button.setFixedSize(250, 50)
        self.voltar_button.setStyleSheet(self.botao_style())
        layout.addWidget(self.voltar_button, alignment=Qt.AlignHCenter)

        layout.addStretch()

        container = QWidget(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

    def salvar_jogo(self):
        try:
            titulo = self.nome_jogo_input.text()
            genero = self.genero_jogo_input.text()
            avaliacao = float(self.avaliacao_jogo_input.text())

            # Criando uma instância do jogo
            novo_jogo = Jogo(titulo, genero, avaliacao)

            # Adicionando o jogo à biblioteca
            biblioteca_jogos.adicionar_jogo(novo_jogo)

            QMessageBox.information(self, "Sucesso", "Jogo cadastrado com sucesso!")
            self.voltar()  # Retorna à tela anterior

        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))

    def voltar(self):
        self.tela_jogos = TelaJogos(self.pixmap)
        self.tela_jogos.show()
        self.hide()

    def update_background(self):
        scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def botao_style(self):
        return """
            background-color: #003366;  /* Cor de fundo azul escuro */
            color: white;                /* Cor do texto branco */
            border: 2px solid white;     /* Borda branca de 2 pixels */
            border-radius: 10px;         /* Bordas arredondadas */
            font-size: 20px;             /* Tamanho da fonte */
        """

    def input_style(self):
        return """
            padding: 10px;
            font-size: 18px;
            border: 2px solid #003366;  /* Borda azul escuro */
            border-radius: 5px;         /* Bordas arredondadas */
        """

class FiltrarJogos(QMainWindow):
    """
    Classe FiltrarJogos
    Esta classe representa uma janela de filtragem de jogos, permitindo ao usuário filtrar jogos por gênero e visualizar a média das avaliações dos jogos filtrados.
    Métodos
    -------
    __init__(self, pixmap, parent=None)
        Inicializa a janela de filtragem de jogos.
    initUI(self)
        Inicializa a interface do usuário, configurando os widgets e layouts.
    filtrar_jogos(self)
        Filtra os jogos com base no gênero fornecido pelo usuário e exibe a lista de jogos filtrados e a média das avaliações.
    voltar(self)
        Retorna à tela anterior.
    update_background(self)
        Atualiza o plano de fundo da janela com a imagem fornecida.
    resizeEvent(self, event)
        Evento de redimensionamento da janela, que atualiza o plano de fundo.
    botao_style(self)
        Retorna a folha de estilo para os botões.
    input_style(self)
        Retorna a folha de estilo para os campos de entrada.
        """
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Filtrar Jogos")
        self.setGeometry(100, 100, 800, 600)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)

        self.pixmap = pixmap
        self.update_background()
        self.background_label.lower()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.genero_filtro_input = QLineEdit(self)
        self.genero_filtro_input.setPlaceholderText("Digite o gênero para filtrar")
        self.genero_filtro_input.setStyleSheet(self.input_style())
        layout.addWidget(self.genero_filtro_input, alignment=Qt.AlignHCenter)

        self.filtrar_button = QPushButton("Filtrar", self)
        self.filtrar_button.clicked.connect(self.filtrar_jogos)
        self.filtrar_button.setFixedSize(250, 50)
        self.filtrar_button.setStyleSheet(self.botao_style())
        layout.addWidget(self.filtrar_button, alignment=Qt.AlignHCenter)

        self.lista_jogos = QListWidget(self)
        layout.addWidget(self.lista_jogos, alignment=Qt.AlignHCenter)

        self.media_avaliacao_label = QLabel(self)
        self.media_avaliacao_label.setStyleSheet("color: yellow; font-size: 18px; font-weight: bold;")
        layout.addWidget(self.media_avaliacao_label, alignment=Qt.AlignHCenter)

        self.voltar_button = QPushButton("Voltar", self)
        self.voltar_button.clicked.connect(self.voltar)
        self.voltar_button.setFixedSize(250, 50)
        self.voltar_button.setStyleSheet(self.botao_style())
        layout.addWidget(self.voltar_button, alignment=Qt.AlignHCenter)

        container = QWidget(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

    def filtrar_jogos(self):
        genero_filtro = self.genero_filtro_input.text()
        self.lista_jogos.clear()

        # Obtém os jogos filtrados da biblioteca
        jogos_filtrados = biblioteca_jogos.listar_jogos_por_genero(genero_filtro)

        if jogos_filtrados:
            for jogo in jogos_filtrados:
                self.lista_jogos.addItem(f"{jogo.get_titulo()} - Avaliação: {jogo.get_avaliacao()}")

            # Calcular a média das avaliações
            avaliacoes = [jogo.get_avaliacao() for jogo in jogos_filtrados]
            media_avaliacao = sum(avaliacoes) / len(avaliacoes)
            self.media_avaliacao_label.setText(f"Média das avaliações: {media_avaliacao:.2f}")
        else:
            self.media_avaliacao_label.setText("Nenhum jogo encontrado para este gênero.")

    def voltar(self):
        self.tela_jogos = TelaJogos(self.pixmap)
        self.tela_jogos.show()
        self.hide()

    def update_background(self):
        scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def botao_style(self):
        return """
            background-color: #003366;  /* Cor de fundo azul escuro */
            color: white;                /* Cor do texto branco */
            border: 2px solid white;     /* Borda branca de 2 pixels */
            border-radius: 10px;         /* Bordas arredondadas */
            font-size: 20px;             /* Tamanho da fonte */
        """

    def input_style(self):
        return """
            padding: 10px;
            font-size: 18px;
            border: 2px solid #003366;  /* Borda azul escuro */
            border-radius: 5px;         /* Bordas arredondadas */
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
