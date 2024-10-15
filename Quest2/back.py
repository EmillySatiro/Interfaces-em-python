class Bicicleta:
    """
    Classe que representa uma bicicleta para aluguel.
    
    Atributos:
        modelo (str): O modelo da bicicleta.
        tarifa_por_hora (float): A tarifa de aluguel por hora.
        alugada (bool): Indica se a bicicleta está alugada ou não.
    """
    def __init__(self, modelo, tarifa_por_hora):
        self.modelo = modelo
        self.tarifa_por_hora = tarifa_por_hora
        self.alugada = False

    def alugar(self):
        """
        Aluga a bicicleta se ela não estiver alugada.
        Retorna True se a operação for bem-sucedida, caso contrário, retorna False.
        """
        if not self.alugada:
            self.alugada = True
            return True
        return False

    def devolver(self):
        """
        Devolve a bicicleta se ela estiver alugada.
        Retorna True se a operação for bem-sucedida, caso contrário, retorna False.
        """
        if self.alugada:
            self.alugada = False
            return True
        return False


class BibliotecaBicicletas:
    """
    Classe que representa uma biblioteca de bicicletas.

    Métodos:
        cadastrar_bicicleta(modelo, tarifa_por_hora):
            Cadastra uma nova bicicleta na biblioteca.
        listar_disponiveis():
            Retorna uma lista com todas as bicicletas disponíveis para aluguel.
        listar_alugadas():
            Retorna uma lista com todas as bicicletas atualmente alugadas.
        encontrar_bicicleta(modelo):
            Encontra e retorna uma bicicleta pelo seu modelo. Retorna None se a bicicleta não for encontrada.
    """
    def __init__(self):
        self.bicicletas = []

    def cadastrar_bicicleta(self, modelo, tarifa_por_hora):
        """
        Cadastra uma nova bicicleta na biblioteca.

        Parâmetros:
            modelo (str): O modelo da bicicleta.
            tarifa_por_hora (float): A tarifa de aluguel por hora da bicicleta.
        """
        bicicleta = Bicicleta(modelo, tarifa_por_hora)
        self.bicicletas.append(bicicleta)

    def listar_disponiveis(self):
        """
        Retorna uma lista com todas as bicicletas disponíveis para aluguel.
        """
        return [bicicleta for bicicleta in self.bicicletas if not bicicleta.alugada]

    def listar_alugadas(self):
        """
        Retorna uma lista com todas as bicicletas atualmente alugadas.
        """
        return [bicicleta for bicicleta in self.bicicletas if bicicleta.alugada]

    def encontrar_bicicleta(self, modelo):
        """
        Encontra e retorna uma bicicleta pelo seu modelo.

        Parâmetros:
            modelo (str): O modelo da bicicleta a ser procurada.

        Retorna:
            Bicicleta: A bicicleta encontrada, ou None se não for encontrada.
        """
        for bicicleta in self.bicicletas:
            if bicicleta.modelo == modelo:
                return bicicleta
        return None
