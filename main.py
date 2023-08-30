import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from processamento.calculos import equilibrio

x = equilibrio(c1=[15, 1400], c2=[5, 2000])[0]
y1 = equilibrio(c1=[15, 1400], c2=[5, 2000])[1]
y2 = equilibrio(c1=[15, 1400], c2=[5, 2000])[2]

root = tkinter.Tk()
root.wm_title("Calculator")

figure = Figure(figsize=(5,4), dpi=100)
ax = figure.add_subplot()
ax.plot(x, y1, y2)

canvas = FigureCanvasTkAgg(figure, master=root)  # A tk.DrawingArea.
canvas.draw()

canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

tkinter.mainloop()