import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
import PySimpleGUI as sg
import math
import matplotlib as mt
import numpy as np
h = 12
w = 2
dt = 0.001
m = 6.695
z = 2
xx = 1
xn = -3
yx = 2
yn = 0
vx = 3
vy = 0.1
class Canvas(FigureCanvasTkAgg):
  """
    Create a canvas for matplotlib pyplot under tkinter/PySimpleGUI canvas
    """

  def __init__(self, figure=None, master=None):
    super().__init__(figure=figure, master=master)
    self.canvas = self.get_tk_widget()
    self.canvas.pack(side='top', fill='both', expand=1)
def cm_to_inch(value):
  return value / 2.54
def f(u,x,y):
    k = (x*x + y*y)**0.5
    return (u/(k*k*k))
def plot_figure(m,z,xx,xn,yx,yn,vx,vy):
    if True:
    # try:
        ax.cla()
        m = float(m) * 10**(-27)
        z = float(z)
        xx = float(xx)
        xn = float(xn)
        yx = float(yx)
        yn = float(yn)
        vx = float(vx)
        vy = float(vy)
        k = 8.987551777 * 10**(9)
        e = 1.6021892 * 10**(-19)
        x = [xn]
        y = [yn]
        i = 0
        t = dt
        a = 2*k*z*e*e/m
        while True:
            vx = vx + a*f(x[i],x[i],y[i])*dt
            vy = vy + a*f(y[i],x[i],y[i])*dt
            x.append(x[i]+vx*dt)
            y.append(y[i]+vy*dt)
            i = i + 1
            t = t + dt
            if x[i] > xx or x[i] < xn or y[i] > yx or y[i] < yn:
                break
        ax.set_aspect('equal')
        circle1 = plt.Circle((0, 0), 0.05, color='r')
        ax.add_patch(circle1)
        ax.set_title(r'Модель опыта Резерфорда', fontsize=16)
        ax.plot(x, y, color='g')
        canvas.draw()
    # except:
    #     print("err")
    #     ax.cla()
    #     return
sg.theme('DefaultNoMoreNagging')
layout = [
    [sg.Canvas(size=(640, 480), key='Canvas')],
    [sg.Text('M'), sg.Input(6.695,enable_events=True,k='-M-',size=(9, 1)),sg.Text('^(-27)'),
    sg.Text('Z'), sg.Input(2,enable_events=True,k='-Z-',size=(7, 1)),
    sg.Text('V0x'), sg.Input(3,enable_events=True,k='-VX-',size=(7, 1)),
    sg.Text('V0y'), sg.Input(0.1,enable_events=True,k='-VY-',size=(7, 1))
    ],
    [sg.Text('X0 = Xmin'), sg.Input(-3,enable_events=True,k='-XN-',size=(7, 1)),
    sg.Text('Xmax'), sg.Input(1,enable_events=True,k='-XX-',size=(7, 1)),
    sg.Text('Y0 = Ymin'), sg.Input(0,enable_events=True,k='-YN-',size=(7, 1)),
    sg.Text('Ymax'), sg.Input(2,enable_events=True,k='-YX-',size=(7, 1))],
    # sg.Text('tk'),
    # sg.Spin([i for i in range(1, 2000)],
    #         initial_value=40,
    #         enable_events=True,
    #         k='-TK-')],
    #
    [[sg.Push(), sg.Button('go'), sg.Push()]]
    ]
window = sg.Window('Модель опыта Резерфорда',
                   layout,
                   finalize=True,
                   resizable=True)

fig = Figure(figsize=(cm_to_inch(16), cm_to_inch(10)))

ax = fig.add_subplot()
canvas = Canvas(fig, window['Canvas'].Widget)
def launch():
    plot_figure(m,z,xx,xn,yx,yn,vx,vy)
while True:
  event, values = window.read()
  # print(event)
  if event in (sg.WIN_CLOSED, 'Exit'):
    break
  elif event == '-M-':
      m = values[event]
  elif event == '-Z-':
      z = values[event]
  elif event == '-XN-':
      xn = values[event]
  elif event == '-XX-':
      xx = values[event]
  elif event == '-YN-':
      yn = values[event]
  elif event == '-YX-':
      yx = values[event]
  elif event == '-VX-':
      vx = values[event]
  elif event == '-VY-':
      vy = values[event]
  elif event == 'go':
      launch()
