from canva.canva import *

def respostaDasAtividades():
    resposta = """ATIVIDADE 1: O aluguel mensal do carro da Agência A compensa somente se fossemos andar menos de 60km\n
com o carro, a partir disso, compensa alugar o carro da Agência B.
\n\n
ATIVIDADE 2: Caso o serviço seja feito em até 5 horas, compensa chamar o Encanador B. Pelo contrário,\n
se o serviço durar mais que 5 horas, o encanador que mais vale em conta é o Encanador B
\n\n
ATIVIDADE 3 a): O Fabricante precisa vender 120 unidades de seu produto para conseguir\n
alcançar o ponto de equilíbrio.
\n\n
ATIVIDADE 3 b): Caso ele venha vender 100 unidades, o fabricante terá um prejuízo de R$1000,00.\n
\n\n
ATIVIDADE 3 c): Para obter um lucro de R$4000,00 o fabricante precisa vender 200 unidades.\n"""
    label = Label(master=main_canva, text=resposta)
    label.grid(row=2, column=0, pady=2, padx=100)
    