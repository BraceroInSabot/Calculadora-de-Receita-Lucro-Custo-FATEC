import matplotlib.pyplot as plt

from typing import List

calculo = lambda acrescentador, variavel, fixo: acrescentador*variavel + fixo

def equilibrio(c1: List[float], c2: List[float]) -> object:
  """
  Realiza calculos até achar o ponto de equilibro entre duas funções semelhantes
  de primeiro grau.

  :param:
  c1 -> Lista com dois itens contendo: valor acrescentador e valor fixo
  c2 -> Lista com dois itens contendo: valor acrescentador e valor fixo
  """
  contador: int = 0
  valor1, valor2 = [c1[1]], [c2[1]]
  eixoX: List[float] = [0]

  while (contador != 100):
    contador+=1
    eixoX.append(contador)
    valor1.append(
        calculo(
            acrescentador=c1[0],
            variavel=contador,
            fixo=c1[1]
            )
        )
    valor2.append(
        calculo(
            acrescentador=c2[0],
            variavel=contador,
            fixo=c2[1]
            )
        )
  """
  print(contador)
  print(eixoX)
  print(valor1)
  print(valor2)
  """
  plt.plot(eixoX, valor1, valor2)


