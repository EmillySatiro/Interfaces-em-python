class Item:
    """
    Classe Item representa um item com nome, preço e quantidade.
    Atributos:
        __nome (str): O nome do item.
        __preco (float): O preço do item.
        __quantidade (int): A quantidade do item em estoque.
    Métodos:
        get_nome(): Retorna o nome do item.
        get_preco(): Retorna o preço do item.
        get_quantidade(): Retorna a quantidade do item em estoque.
        set_quantidade(quantidade): Define a quantidade do item em estoque, se for não-negativa.
        calcular_total(): Calcula o valor total do item com base no preço e quantidade.
    """
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        if quantidade < 0:
            print("Quantidade não pode ser negativa.")
        else:
            self.__quantidade = quantidade

    def calcular_total(self):
        return self.__preco * self.__quantidade

class CarrinhoDeCompras:
    """
    Classe que representa um carrinho de compras.
    Métodos:
        __init__(): Inicializa uma nova instância do carrinho de compras.
        adicionar_item(item): Adiciona um item ao carrinho de compras.
        calcular_total(): Calcula o valor total dos itens no carrinho de compras.
        aplicar_desconto(desconto, valor_minimo): Aplica um desconto ao valor total do carrinho se o valor mínimo for atingido.
    Atributos:
        itens (list): Lista de itens no carrinho de compras.
    """
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        total = sum(item.calcular_total() for item in self.itens)
        return total

    def aplicar_desconto(self, desconto, valor_minimo):
        total = self.calcular_total()
        if total >= valor_minimo:
            total_com_desconto = total - (total * desconto / 100)
            return total_com_desconto
        else:
            return total


    
class GerenciadorCupons:
    """
    Classe para gerenciar cupons de desconto.
    Atributos:
    ----------
    cupons : list
        Lista de cupons armazenados.
    Métodos:
    --------
    __init__():
        Inicializa uma nova instância da classe GerenciadorCupons.
    adicionar_cupom(codigo, desconto):
        Adiciona um novo cupom à lista de cupons.
    listar_cupons():
        Retorna a lista de cupons armazenados.
    get_cupom(codigo):
        Retorna o cupom correspondente ao código fornecido, se existir.
    """
    def __init__(self):
        self.cupons = []

    def adicionar_cupom(self, codigo, desconto):
        # Adiciona um novo cupom à lista
        cupom = {"codigo": codigo, "desconto": desconto}
        self.cupons.append(cupom)

    def listar_cupons(self):
        # Retorna a lista de cupons
        return self.cupons

    def get_cupom(self, codigo):
        # Retorna o cupom correspondente ao código, se existir
        for cupom in self.cupons:
            if cupom["codigo"] == codigo:
                return cupom
        return None  # Retorna None se o cupom não for encontrado

