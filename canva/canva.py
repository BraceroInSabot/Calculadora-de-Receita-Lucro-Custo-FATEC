from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.wm_title("Calculator")
root.geometry("1600x1000")

main_canva = Canvas(root)
main_canva.pack(side=TOP, fill=BOTH, expand=1)

atividade = Frame(root)
"""def canvaConfig(): 
    scrollbar = Scrollbar(main_canva, orient=VERTICAL, command=main_canva.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    main_canva.configure(yscrollcommand=scrollbar.register, scrollregion=main_canva.bbox("all"))
    # main_canva.bind("<Configure>", lambda event: main_canva.configure(scrollregion=main_canva.bbox("all")))

    return root"""

def canvaDraw(figure):
    canvas = FigureCanvasTkAgg(figure, master=main_canva)  # A tk.DrawingArea.
    canvas.draw()


    return canvas

def atividadeLabel(label, canvas, dimension):
    label.grid(row=dimension[0], column=dimension[1], pady=2)
    canvas.get_tk_widget().grid(row=dimension[0], column=dimension[1], pady=2)

    return atividade

def repostasLabel(label, label_atividade):
    label.pack()
    label_atividade.pack()

    return 1

def loopCanva():
    root.mainloop()