from canva.canva import *
from processamento.calculos import Function, equilibrioDeDuasFuncoes, calcularLucro
from matplotlib.figure import Figure

def atividade1():
    label1 = Label(master=atividade, text="Atividade 1")
    label1_atividade = Label(master=atividade, text="""
    Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
    """)

    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=1400), caso2=Function(acrescentador=5, fixo=2000))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Agência A", "Agência B"])
    ax.set_title("Exercício 1")

    atividadeLabel(label=label1,
                    canvas=canvaDraw(figure=figure),
                      dimension=[0, 0]
                    )
    
def atividade2():
    label2 = Label(master=atividade, text="Atividade 2")
    label2_atividade = Label(master=atividade, text="""
    Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
    """)
    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Encanador A", "Encanador B"])
    ax.set_title("Exercício 2")

    atividadeLabel(label=label2,
                    canvas=canvaDraw(figure=figure),
                      dimension=[1, 0]
                    )

def atividade3a():
    label3 = Label(master=atividade, text="Atividade 3 a")
    label3_atividade = Label(master=atividade, text="""
    Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
    """)
    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Receita", "Custo"])
    ax.set_title("Exercício 3 a)")

    atividadeLabel(label=label3,
                    canvas=canvaDraw(figure=figure),
                      dimension=[0, 1]
                    )
    
def atividade3b():
    label4 = Label(master=atividade, text="Atividade 3 b")    
    label4_atividade = Label(master=atividade, text="""
    Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
    """)

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

    atividadeLabel(label=label4,
                    canvas=canvaDraw(figure=figure),
                      dimension=[1, 1]
                    )

    