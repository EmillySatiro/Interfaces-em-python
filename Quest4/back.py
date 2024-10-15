class Aula:
    """
    Classe Aula representa uma aula com um título e um nível de dificuldade.
    Atributos:
        titulo (str): O título da aula.
        nivel_dificuldade (str): O nível de dificuldade da aula.
    Métodos:
        get_titulo(): Retorna o título da aula.
        get_nivel_dificuldade(): Retorna o nível de dificuldade da aula.
        exibir_info(): Retorna uma string com o título e o nível de dificuldade da aula.
    """
    def __init__(self, titulo, nivel_dificuldade):
        self.__titulo = titulo
        self.__nivel_dificuldade = nivel_dificuldade

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_nivel_dificuldade(self):
        return self.__nivel_dificuldade

    def exibir_info(self):
        return f"Título: {self.__titulo}, Nível de Dificuldade: {self.__nivel_dificuldade}"

class AulaDeIngles(Aula):
    """
    Classe que representa uma aula de inglês, herdando da classe Aula.
    Atributos:
    titulo : str
        O título da aula.
    nivel_dificuldade : str
        O nível de dificuldade da aula.
    palavras_chave : list
        Lista de palavras-chave relacionadas à aula de inglês.
        
    Métodos:
    exibir_palavras_chave():
        Retorna a lista de palavras-chave da aula de inglês.
    """
    def __init__(self, titulo, nivel_dificuldade):
        super().__init__(titulo, nivel_dificuldade)
        self.palavras_chave = [
    "hello", "world", "language", "study",
    "teacher", "student", "classroom", "book",
    "computer", "homework", "family", "friend",
    "school", "lesson", "exam", "practice"
]

    def exibir_palavras_chave(self):
        return self.palavras_chave

class AulaDeEspanhol(Aula):
    """
    Representa uma aula de espanhol, herdando da classe Aula.
    Atributos:
        titulo (str): O título da aula.
        nivel_dificuldade (str): O nível de dificuldade da aula.
        palavras_chave (list): Lista de palavras-chave relacionadas à aula de espanhol.
    Métodos:
        exibir_palavras_chave():
            Retorna a lista de palavras-chave relacionadas à aula de espanhol.
    """
    def __init__(self, titulo, nivel_dificuldade):
        super().__init__(titulo, nivel_dificuldade)
        self.palavras_chave = [
    "hola", "mundo", "idioma", "estudiar",
    "palabra", "aprendizaje", "conocimiento", "escribir",
    "leer", "escuchar", "hablar", "practicar",
    "gramática", "vocabulario", "cultura", "clase",
    "maestro", "alumno"
]


    def exibir_palavras_chave(self):
        return self.palavras_chave
