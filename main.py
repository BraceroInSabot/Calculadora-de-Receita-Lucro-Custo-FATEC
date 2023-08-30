from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from processamento.calculos import Function, equilibrioDeDuasFuncoes, calcularLucro

#print(y1, type(y1), y2, type(y2))


root = Tk()
root.wm_title("Calculator")
root.config(height=900, width=800)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

main_canva = Canvas(root, yscrollcommand=scrollbar.set)
main_canva.pack(side=TOP, fill=BOTH, expand=True)

scrollbar.config(command=main_canva)

x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=1400), caso2=Function(acrescentador=5, fixo=2000))[0]
y1 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[1]
y2 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[2]

figure1 = Figure(figsize=(5,2))
ax = figure1.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.plot(x, y1, y2)

canvas1 = FigureCanvasTkAgg(figure1, master=main_canva)  # A tk.DrawingArea.
canvas1.draw()


x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[0]
y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[1]
y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[2]

figure2 = Figure(figsize=(5,2))
ax = figure2.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.plot(x, y1, y2)

canvas2 = FigureCanvasTkAgg(figure2, master=main_canva)  # A tk.DrawingArea.
canvas2.draw()


x = calcularLucro(receita=Function(acrescentador=100), custo=Function(acrescentador=50, fixo=6000))[0]
y1 = calcularLucro(receita=Function(acrescentador=100), custo=Function(acrescentador=50, fixo=6000))[1]

figure3 = Figure(figsize=(5,3))
ax = figure3.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.plot(x, y1)

canvas3 = FigureCanvasTkAgg(figure3, master=main_canva)  # A tk.DrawingArea.
canvas3.draw()


canvas1.get_tk_widget().pack(side=TOP, expand=True)
canvas2.get_tk_widget().pack(side=TOP, expand=True)
canvas3.get_tk_widget().pack(side=TOP, expand=True)

mainloop()