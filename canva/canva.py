from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.wm_title("Calculator")
root.config(height=900, width=800)
main_canva = Canvas(root)

def canvaConfig():
    main_canva.pack(side=TOP, fill=BOTH, expand=1)

    scrollbar = Scrollbar(main_canva, orient=VERTICAL, command=main_canva.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    main_canva.configure(yscrollcommand=scrollbar.register)
    main_canva.bind("<Configure>", lambda event: main_canva.configure(scrollregion=main_canva.bbox("all")))

    second_frame = Frame(main_canva)
    main_canva.create_window((0,0), window=second_frame, anchor="sw")

    return root

def canvaDraw(figure):
    canvas = FigureCanvasTkAgg(figure, master=main_canva)  # A tk.DrawingArea.
    canvas.draw()

    return canvas

def atividadeLabel(label, label_atividade, canvas):
    label.pack(side=TOP)
    label_atividade.pack(side=TOP)
    canvas.get_tk_widget().pack(side=TOP, expand=True)

def loopCanva():
    root.mainloop()