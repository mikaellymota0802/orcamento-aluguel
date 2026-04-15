from imovel import Imovel
from calculadora import CalculadoraAluguel

imovel = Imovel("apartamento", 2, False)
calc = CalculadoraAluguel()

resultado = calc.calcular(imovel)

assert resultado == 855.0
print("Teste passou!")