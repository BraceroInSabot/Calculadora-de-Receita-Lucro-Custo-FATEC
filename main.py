import matplotlib.pyplot as plt
from processamento.calculos import equilibrio

plt.margins(x=0, y=0, tight=True)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

def exercicios() -> bool:
  equilibrio(c1=[15, 1400], c2=[5, 2000])

exercicios()