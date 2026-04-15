from imovel import Imovel
from calculadora import CalculadoraAluguel

def main():
    print("=== ORÇAMENTO DE ALUGUEL ===")

    tipo = input("Tipo (casa/apartamento): ").lower()
    quartos = int(input("Quartos: "))
    criancas = input("Tem crianças? (s/n): ").lower()

    imovel = Imovel(tipo, quartos, criancas == "s")
    calc = CalculadoraAluguel()

    valor = calc.calcular(imovel)

    print(f"\nValor final: R$ {valor}")

if __name__ == "__main__":
    main()