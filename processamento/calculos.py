#calculo = lambda acrescentador, variavel, fixo: acrescentador*variavel + fixo

class Function():
    def __init__(self, acrescentador: float, fixo: float):
        self.a = acrescentador
        self.b = fixo

    def calculo(self, variavel: float) -> float:
        x = variavel
        posY = self.a*x + self.b
        return posY

def equilibrioDeDuasFuncoes(caso1: Function, caso2: Function) -> object:
    """
    Realiza calculos até achar o ponto de equilibro entre duas funções semelhantes
    de primeiro grau.

    :param:
    c1 -> Lista com dois itens contendo: valor acrescentador e valor fixo
    c2 -> Lista com dois itens contendo: valor acrescentador e valor fixo
    """
    contador: int = 0
    valor1, valor2 = [caso1.calculo(0)], [caso2.calculo(0)]
    eixoX = [0]

    while (contador != 100):
        contador+=1
        eixoX.append(contador)
        valor1.append(float(caso1.calculo(variavel=contador)))
        valor2.append(float(caso2.calculo(variavel=contador)))

    return (eixoX, valor1, valor2)


