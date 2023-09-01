class Function():
    def __init__(self, acrescentador: float, fixo: float = 0):
        self.a = acrescentador
        self.b = fixo

    def calculo(self, variavel: float = 0) -> float:
        """
        Representa o modelo da função de 1º grau

        :param:
        variavel: float -> Número real que representam um valor variável
        """
        x = variavel
        posY = self.a*x + self.b
        return posY

def equilibrioDeDuasFuncoes(caso1: Function, caso2: Function) -> object:
    """
    Realiza calculos até achar o ponto de equilibro entre duas funções semelhantes
    de primeiro grau.

    :param:
    caso1: Function -> Lista com dois itens contendo: valor acrescentador e valor fixo
    caso2: Function -> Lista com dois itens contendo: valor acrescentador e valor fixo
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

def calcularLucro(receita: Function, custo: Function) -> tuple:
    """
    Realiza cálculos para chegar ao lucro do negócio

    :param:
    receita: Function -> lista com valores ordenados representando a receita de uma empresa
    custo: Function -> lista com valores ordenados representando o custo de uma empresa
    """
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

def calcXApartirDeY(funcao: Function, yValor: float) -> float:
    """
    Encontra o valor de X a partir do valor de Y

    :param:
    yValor: float -> valor de Y
    funcao: Function -> lista ordenada contendo números reais
    """

    xvalor = (yValor -(funcao.b))/funcao.a

    return xvalor

def calcYapartirX(funcao: Function, xValor: float) -> float:
    """
    Encontra o valor de Y a partir do valor de X

    :param:
    xValor: float -> número real variavel
    funcao: Function -> lista ordenada contendo números reais
    """
    valorY = funcao.calculo(xValor)

    return valorY
