from imovel import Imovel

class CalculadoraAluguel:
    def calcular(self, imovel: Imovel) -> float:
        if imovel.tipo == "apartamento":
            valor = 700
        elif imovel.tipo == "casa":
            valor = 900
        else:
            raise ValueError("Tipo inválido")

        if imovel.quartos == 2:
            valor += 200

        if not imovel.tem_criancas:
            valor *= 0.95

        return round(valor, 2)