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
main_canva.pack(side=TOP, fill=BOTH, expand=1)

scrollbar.config(command=main_canva)


label1 = Label(master=main_canva, text="Atividade 1")

x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=1400), caso2=Function(acrescentador=5, fixo=2000))[0]
y1 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[1]
y2 = equilibrioDeDuasFuncoes(caso1=Function(15, fixo=1400), caso2=Function(5, 2000))[2]

figure1 = Figure(figsize=(5,2))
ax = figure1.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.plot(x, y1, y2)
ax.legend(["Agência A", "Agência B"])
ax.get_title()

canvas1 = FigureCanvasTkAgg(figure1, master=main_canva)  # A tk.DrawingArea.
canvas1.draw()


label2 = Label(master=main_canva, text="Atividade 2")

x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[0]
y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[1]
y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=15, fixo=35), caso2=Function(acrescentador=18, fixo=20))[2]

figure4 = Figure(figsize=(5,2))
ax = figure4.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.plot(x, y1, y2)
ax.legend(["Agência A", "Agência B"])

canvas4 = FigureCanvasTkAgg(figure4, master=main_canva)  # A tk.DrawingArea.
canvas4.draw()


label3 = Label(master=main_canva, text="Atividade 3 a")

x = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[0]
y1 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[1]
y2 = equilibrioDeDuasFuncoes(caso1=Function(acrescentador=100), caso2=Function(acrescentador=50, fixo=6000))[2]

figure2 = Figure(figsize=(5,2))
ax = figure2.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.plot(x, y1, y2)
ax.legend(["Agência A", "Agência B"])

canvas2 = FigureCanvasTkAgg(figure2, master=main_canva)  # A tk.DrawingArea.
canvas2.draw()


label4 = Label(master=main_canva, text="Atividade 3 b")

x = calcularLucro(receita=Function(acrescentador=100), custo=Function(acrescentador=50, fixo=6000))[0]
y1 = calcularLucro(receita=Function(acrescentador=100), custo=Function(acrescentador=50, fixo=6000))[1]

figure3 = Figure(figsize=(5,3))
ax = figure3.add_subplot()
ax.margins(x=0, y=0, tight=True)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.plot(x, y1)
ax.legend(["Agência A"])

canvas3 = FigureCanvasTkAgg(figure3, master=main_canva)  # A tk.DrawingArea.
canvas3.draw()

label1_atividade = Label(master=main_canva, text="""
Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
""")
label2_atividade = Label(master=main_canva, text="""
Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
""")
label3_atividade = Label(master=main_canva, text="""
Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
""")
label4_atividade = Label(master=main_canva, text="""
Até antes do 60km compensa a empresa A, depois disso compensa comprar da empresa B
""")

label1.pack(side=TOP)
label1_atividade.pack(side=TOP)
canvas1.get_tk_widget().pack(side=TOP, expand=True)
label2.pack(side=TOP)
label2_atividade.pack(side=TOP)
canvas4.get_tk_widget().pack(side=TOP, expand=True)
label3.pack(side=TOP)
label3_atividade.pack(side=TOP)
canvas2.get_tk_widget().pack(side=TOP, expand=True)
label4.pack(side=TOP)
label4_atividade.pack(side=TOP)
canvas3.get_tk_widget().pack(side=TOP, expand=True)

mainloop()