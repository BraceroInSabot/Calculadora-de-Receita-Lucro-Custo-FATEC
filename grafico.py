from canva.canva import *
from processamento.calculos import Function, equilibrioDeDuasFuncoes, calcularLucro
from matplotlib.figure import Figure

def atividade1():
    label1 = Label(master=main_canva, text="Atividade 1")
    label1_atividade = Label(master=main_canva, text="""
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
    ax.get_title()

    atividadeLabel(label=label1,
                     label_atividade=label1_atividade,
                       canvas=canvaDraw(figure=figure)
                       )
    

def atividade2():
    label2 = Label(master=main_canva, text="Atividade 2")
    label2_atividade = Label(master=main_canva, text="""
    Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
    """)
    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Agência A", "Agência B"])

    atividadeLabel(label=label2,
                     label_atividade=label2_atividade,
                       canvas=canvaDraw(figure=figure)
                       )


def atividade3a():
    label3 = Label(master=main_canva, text="Atividade 3 a")
    label3_atividade = Label(master=main_canva, text="""
    Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
    """)
    x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[0]
    y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[1]
    y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[2]

    figure = Figure(figsize=(5,2))
    ax = figure.add_subplot()
    ax.margins(x=0, y=0, tight=True)
    ax.plot(x, y1, y2)
    ax.legend(["Agência A", "Agência B"])

    atividadeLabel(label=label3,
                     label_atividade=label3_atividade,
                       canvas=canvaDraw(figure=figure)
                       )
    
def atividade3b():
    label4 = Label(master=main_canva, text="Atividade 3 b")    
    label4_atividade = Label(master=main_canva, text="""
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

    atividadeLabel(label=label4,
                     label_atividade=label4_atividade,
                       canvas=canvaDraw(figure=figure)
                       )

    