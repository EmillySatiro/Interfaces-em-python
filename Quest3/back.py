from datetime import datetime, timedelta

class EstoqueMedicamentos:
    """
    Classe para gerenciar o estoque de medicamentos.
    Atributos:
        nome (str): Nome do medicamento.
        quantidade (int): Quantidade disponível do medicamento.
        data_vencimento (datetime.date): Data de vencimento do medicamento.
    Métodos:
        get_nome(): Retorna o nome do medicamento.
        get_quantidade(): Retorna a quantidade disponível do medicamento.
        get_data_vencimento(): Retorna a data de vencimento do medicamento.
        set_nome(nome): Define o nome do medicamento.
        set_quantidade(quantidade): Define a quantidade disponível do medicamento.
        set_data_vencimento(data_vencimento): Define a data de vencimento do medicamento.
        verificar_vencimento(dias=30): Verifica se o medicamento está próximo do vencimento.
        adicionar_quantidade(quantidade): Adiciona uma quantidade ao estoque do medicamento.
        remover_quantidade(quantidade): Remove uma quantidade do estoque do medicamento.
    """
    def __init__(self, nome, quantidade, data_vencimento):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__data_vencimento = data_vencimento

    # Getters
    def get_nome(self):
        return self.__nome

    def get_quantidade(self):
        return self.__quantidade

    def get_data_vencimento(self):
        return self.__data_vencimento

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_quantidade(self, quantidade):
        if quantidade < 0:
            print("Quantidade não pode ser negativa.")
        else:
            self.__quantidade = quantidade

    def set_data_vencimento(self, data_vencimento):
        self.__data_vencimento = data_vencimento

    def verificar_vencimento(self, dias=30):
        
        hoje = datetime.now().date()
        return self.__data_vencimento <= hoje + timedelta(days=dias)

    def adicionar_quantidade(self, quantidade):
        
        if quantidade > 0:
            self.__quantidade += quantidade
            print(f"{quantidade} unidades de {self.__nome} adicionadas ao estoque.")
        else:
            print("A quantidade a ser adicionada deve ser positiva.")

    def remover_quantidade(self, quantidade):
       
        if quantidade < 0:
            print("A quantidade a ser removida deve ser positiva.")
        elif quantidade > self.__quantidade:
            print("Quantidade a ser removida excede a quantidade disponível.")
        else:
            self.__quantidade -= quantidade
            print(f"{quantidade} unidades de {self.__nome} removidas do estoque.")


estoque = []

def adicionar_medicamento(nome, quantidade, data_vencimento):
    novo_medicamento = EstoqueMedicamentos(nome, quantidade, data_vencimento)
    estoque.append(novo_medicamento)
    print(f"Medicamento {nome} adicionado ao estoque.")

def listar_medicamentos():
    if estoque:
        print("Medicamentos no estoque:")
        for medicamento in estoque:
            status_vencimento = "perto do vencimento" if medicamento.verificar_vencimento() else "ok"
            print(f"Nome: {medicamento.get_nome()}, Quantidade: {medicamento.get_quantidade()}, "
                  f"Data de Vencimento: {medicamento.get_data_vencimento()}, Status: {status_vencimento}")
    else:
        print("Nenhum medicamento cadastrado no estoque.")
