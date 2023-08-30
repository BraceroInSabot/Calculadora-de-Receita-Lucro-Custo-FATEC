import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from processamento.calculos import Function, equilibrioDeDuasFuncoes

x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=1400), caso2=Function(acrescentador=5, fixo=2000))[0]
y1 = equilibrioDeDuasFuncoes(caso1=Function(15, 1400), caso2=Function(5, 2000))[1]
y2 = equilibrioDeDuasFuncoes(caso1=Function(15, 1400), caso2=Function(5, 2000))[2]

print(y1, type(y1), y2, type(y2))

root = tkinter.Tk()
root.wm_title("Calculator")

figure = Figure(figsize=(5,4), dpi=100)
ax = figure.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.plot(x, y1, y2)

canvas = FigureCanvasTkAgg(figure, master=root)  # A tk.DrawingArea.
canvas.draw()

canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

tkinter.mainloop()