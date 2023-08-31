class Function():
    def __init__(self, acrescentador: float, fixo: float = 0):
        self.a = acrescentador
        self.b = fixo

    def calculo(self, variavel: float = 0) -> float:
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
    valorY1, valorY2 = [caso1.calculo()], [caso2.calculo()]
    eixoX = [0]

    while (valorY1[-1] != valorY2[-1]):
        contador+=1
        eixoX.append(contador)
        valorY1.append(float(caso1.calculo(variavel=contador)))
        valorY2.append(float(caso2.calculo(variavel=contador)))

    for x in range(0, contador):
        contador+=1
        eixoX.append(contador)
        valorY1.append(float(caso1.calculo(variavel=contador)))
        valorY2.append(float(caso2.calculo(variavel=contador)))

    return (eixoX, valorY1, valorY2)

def calcularLucro(receita: Function, custo: Function):
    contador: int = 0
    eixoX = [0]

    resultado = [float(receita.calculo(variavel=0) - custo.calculo(variavel=0))]

    while (resultado[-1] != 0):
        contador+=1
        eixoX.append(contador)
        resultado.append(float(receita.calculo(variavel=contador) - custo.calculo(variavel=contador)))

    for x in range(0, contador):
        contador+=1
        eixoX.append(contador)
        resultado.append(float(receita.calculo(variavel=contador) - custo.calculo(variavel=contador)))

    return (eixoX, resultado)
