class Imovel:
    def __init__(self, tipo: str, quartos: int, tem_criancas: bool):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.tem_criancas = tem_criancas