
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from processamento.calculos import Function, equilibrioDeDuasFuncoes, calcularLucro
from canva import canva
import grafico

if __name__ == "__main__":
    canva.canvaConfig()
    grafico.atividade1()
    grafico.atividade2()

    grafico.atividade2()
    grafico.atividade2()
    grafico.atividade2()
    
    grafico.atividade3a()
    grafico.atividade3b()
    canva.loopCanva()
