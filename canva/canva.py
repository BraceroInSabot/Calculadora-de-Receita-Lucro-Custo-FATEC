from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.wm_title("Calculator")
root.geometry("1600x1000")

main_canva = Canvas(root)
main_canva.pack(side=TOP, fill=BOTH, expand=1)

atividade = Frame(root)


def canvaDraw(figure: object) -> object:
    """
    Retorna um gráfico desenhado em um Frame do Tkinter

    :param:
    figure: Figure -> figura de um gráfico gerada pelo Matplotlib
    """
    canvas = FigureCanvasTkAgg(figure, master=main_canva)
    canvas.draw()


    return canvas

def atividadeLabel(canvas: object, dimension: object) -> object:
    """
    Retorna o um frame posicionado na tela do executavel

    :param:
    canvas: object -> Gráfico armazenado em uma figura
    """
    canvas.get_tk_widget().grid(row=dimension[0], column=dimension[1], pady=2)

    return atividade

def loopCanva():
    """
    Retorna valor nulo, necessário para o funcionamento do Tkinter
    """
    root.mainloop()