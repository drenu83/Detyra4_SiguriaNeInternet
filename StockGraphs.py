from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import style

style.use('fivethirtyeight')

fig = Figure(figsize=(100, 100),
             dpi=70)


ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)


def animate(i):
    df = pd.read_csv('real time stock data.csv')
    ys = df.iloc[1:, 2].values
    xs = list(range(1, len(ys) + 1))
    ax1.clear()
    ax1.plot(xs, ys)
    ax1.set_title('CKH Holdings', fontsize=12)

    ys = df.iloc[1:, 3].values
    ax2.clear()
    ax2.plot(xs, ys)
    ax2.set_title('CLP Holdings', fontsize=12)

    ys = df.iloc[1:, 4].values
    ax3.clear()
    ax3.plot(xs, ys)
    ax3.set_title('HK & China Gas', fontsize=12)

    ys = df.iloc[1:, 5].values
    ax4.clear()
    ax4.plot(xs, ys)
    ax4.set_title('HSBC Holdings', fontsize=12)


window = Tk()

window.title('Stock Prices')

window.geometry('500x500')

canvas = FigureCanvasTkAgg(fig, master=window)

toolbar = NavigationToolbar2Tk(canvas,
                               window)
toolbar.update()

canvas.get_tk_widget().pack()

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.tight_layout()

window.mainloop()
