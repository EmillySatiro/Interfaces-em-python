class Jogo:
    """
    Classe que representa um jogo.
    Atributos:
        titulo (str): O título do jogo.
        genero (str): O gênero do jogo.
        avaliacao (float): A avaliação do jogo, deve estar entre 0 e 10.
    Métodos:
        __init__(titulo, genero, avaliacao):
            Inicializa uma nova instância da classe Jogo.
        get_titulo():
            Retorna o título do jogo.
        set_titulo(titulo):
            Define o título do jogo.
        get_genero():
            Retorna o gênero do jogo.
        set_genero(genero):
            Define o gênero do jogo.
        get_avaliacao():
            Retorna a avaliação do jogo.
        set_avaliacao(avaliacao):
            Define a avaliação do jogo. Levanta um ValueError se a avaliação não estiver entre 0 e 10.
    """
    def __init__(self, titulo, genero, avaliacao):
        self.__titulo = titulo
        self.__genero = genero
        self.__avaliacao = None
        self.set_avaliacao(avaliacao)

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_avaliacao(self):
        return self.__avaliacao

    def set_avaliacao(self, avaliacao):
        if 0 <= avaliacao <= 10:
            self.__avaliacao = avaliacao
        else:
            raise ValueError("A avaliação deve estar entre 0 e 10.")


class BibliotecaJogos:
    """
    Classe que representa uma biblioteca de jogos.
    
    Métodos:
        adicionar_jogo(jogo): 
            Adiciona um novo jogo à biblioteca.
        listar_jogos_por_genero(genero): 
            Lista todos os jogos de um determinado gênero.
        calcular_media_avaliacoes(genero): 
            Calcula a média das avaliações dos jogos de um determinado gênero.
        listar_jogos(): 
            Lista todos os jogos da biblioteca.
        remover_jogo(titulo): 
            Remove um jogo da biblioteca pelo título.
        buscar_jogo_por_titulo(titulo): 
            Busca um jogo na biblioteca pelo título.
        atualizar_avaliacao_jogo(titulo, nova_avaliacao): 
            Atualiza a avaliação de um jogo pelo título.
    """
    def __init__(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def listar_jogos_por_genero(self, genero):
        return [jogo for jogo in self.jogos if jogo.get_genero() == genero]

    def calcular_media_avaliacoes(self, genero):
        jogos_genero = self.listar_jogos_por_genero(genero)
        if not jogos_genero:
            return 0
        soma_avaliacoes = sum(jogo.get_avaliacao() for jogo in jogos_genero)
        return soma_avaliacoes / len(jogos_genero)

    def listar_jogos(self):
        return self.jogos

    def remover_jogo(self, titulo):
        self.jogos = [jogo for jogo in self.jogos if jogo.get_titulo() != titulo]

    def buscar_jogo_por_titulo(self, titulo):
        for jogo in self.jogos:
            if jogo.get_titulo() == titulo:
                return jogo
        return None

    def atualizar_avaliacao_jogo(self, titulo, nova_avaliacao):
        jogo = self.buscar_jogo_por_titulo(titulo)
        if jogo:
            jogo.set_avaliacao(nova_avaliacao)
        else:
            raise ValueError("Jogo não encontrado.")
