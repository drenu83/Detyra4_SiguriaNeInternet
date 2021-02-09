import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')

fig= plt.figure()
ax1=fig.addsubplot(2,2,1)
ax2=fig.addsubplot(2,2,2)
ax3=fig.addsubplot(2,2,3)
ax4=fig.addsubplot(2,2,4)


def animate(i):
    df = pd.read_csv('real time stock data.csv')
    ys = df.iloc[1:, 2].values
    xs = list(range(1, len(ys)))
    ax1.clear()
    ax1.plot(xs, ys)
    ax1.set_title('CKH Holdings', fontsize=12)
