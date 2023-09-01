from canva.canva import *
from processamento.calculos import Function, equilibrioDeDuasFuncoes, calcularLucro
from matplotlib.figure import Figure

def atividade1():
    """
    Gera o gráfico do enunciado a seguir: "O aluguel mensal de um carro numa agência é de R$1400,00 mais
    R$15,00 por km rodado.  Uma segunda agência cobra R$2000,00 mais R$5,00 por km rodado.  Qual agência
    oferece o melhor plano de aluguel?"
    """
    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=1400), caso2=Function(acrescentador=5, fixo=2000))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Agência A", "Agência B"])
    ax.set_title("Exercício 1")

    atividadeLabel(canvas=canvaDraw(figure=figure),
                    dimension=[0, 0])
    
def atividade2():
    """
    Gera o gráfico do enunciado a seguir: "Um encanador cobra uma taxa de R$ 35,00 e mais R$ 15,00 a
    cada hora de trabalho.  Um outro cobra R$ 20,00 e mais R$ 18,00 a cada hora.  Ache um critério
    para decidir que encanador chamar, se forem levadas em conta apenas considerações de ordem financeiras."
    """
    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Encanador A", "Encanador B"])
    ax.set_title("Exercício 2")

    atividadeLabel(canvas=canvaDraw(figure=figure), 
                   dimension=[1, 0])

def atividade3a():
    """
    Gera o gráfico para o enunciado a seguir: "Um fabricante vende a unidade de certo produto por R$100,00.
    O custo total consiste em uma taxa fixa de R$6.000,00 somada ao custo de produção de R$50,00 por
    unidade.
    
    (a) Quantas unidades o fabricante precisa vender para atingir o ponto de equilíbrio?"
    """
    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Receita", "Custo"])
    ax.set_title("Exercício 3 a)")

    atividadeLabel(canvas=canvaDraw(figure=figure), 
                   dimension=[0, 1])
    
def atividade3b():
    """
    Gera o gráfico para o enunciado a seguir: "Um fabricante vende a unidade de certo produto por R$100,00.
    O custo total consiste em uma taxa fixa de R$6.000,00 somada ao custo de produção de R$50,00 por
    unidade.
    
    (b) Se forem vendidas 100 unidades, qual será o lucro ou o prejuízo do fabricante?
    """
    x = calcularLucro(receita=Function(acrescentador=100), custo=Function(acrescentador=50, fixo=6000))[0]
    y1 = calcularLucro(receita=Function(acrescentador=100), custo=Function(acrescentador=50, fixo=6000))[1]

    figure = Figure(figsize=(5,3))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.plot(x, y1)
    ax.legend(["Agência A"])
    ax.set_title("Exercício 3 b)")

    atividadeLabel(canvas=canvaDraw(figure=figure), 
                   dimension=[1, 1])

    